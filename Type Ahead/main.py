'''###########################################################################
This is a program that will predict what the user will say based on the Mary
had a little lamb song. The code takes the word(s) that the user is saying and
predicts what word the user will type next. In order to use the program, the
 user create a text file called strings in the same directory as the program.
 Then, each line must contains a number followed by a string, separated by a
 comma: number,letter. The number is the n-gram length. The string is the text
 printed by the user and whose prediction you have to print out.

Andres Felipe Vargas                                                   10/2/16
###########################################################################'''
import operator
import string
import re

file = open("Strings.txt") # File must be on the root of the project folder

# Text that will be used to predict the next words.
text = 'Mary had a little lamb its fleece was white as snow; '
text += 'And everywhere that Mary went, the lamb was sure to go. '
text += 'It followed her to school one day, which was against the rule; '
text += 'It made the children laugh and play, to see a lamb at school. '
text += 'And so the teacher turned it out, but still it lingered near, '
text += 'And waited patiently about till Mary did appear. '
text += '"Why does the lamb love Mary so?" the eager children cry; "Why, Mary '
text += 'loves the lamb, you know" the teacher did reply."'

# Stripping the punctuation from the text
strippedText = text.translate(string.maketrans('', ''), string.punctuation)

# Split the text into an array. Where each value of the array is a word.
textArray = re.compile("\w+").findall(strippedText)

# Loop through all of the lines in the file
# for tempString in file:
for tempString in file:
    # Check to see if the line is a \n. If so, skip it
    if(len(tempString) == 1):
        if(not tempString.isalpha()):
            continue

    # split string
    userInput = tempString.split(',')
    length = int(userInput[0]) - 1
    userWord = userInput[1].rstrip()

    # Create a dictionary that will store the predictive text as a key and the number of appearances as the value
    # A totalPredcitionWords variable that will store the number of words in the preditonText and finalPrediction
    # variable that will store the final prediction along with their predictability values, all in order.
    predictionText = {}
    totalPredictionWords = 0
    finalPrediction = []

    for indexOfWord in range(len(textArray) - length):
        # Get the word from the array of words that matches the input text length
        preWord = textArray[indexOfWord:indexOfWord + length]
        preWord = " ".join(preWord)

        # Check to see if the preWord matches the pre-prediction word
        if (preWord == userWord):
            predictionWord = textArray[indexOfWord + length]
            # If the word matches, check to see if the word is  already in the predictionText dictionary.
            # If it is, then add a tally to the value in the dictionary.
            if (predictionWord in  predictionText.keys()):
                predictionText[predictionWord] += 1.000

            # Else, add the word as a dictionary key and initialize the value as 1
            else:
                predictionText[predictionWord] = 1.000

            totalPredictionWords += 1.000   # Increase the value of total words in the predictionText

    # Find the probability that the predicted word is the likely choice to the thousandth decimal value
    for userWord in  predictionText:
        predictionText[userWord] = "%.3f" % float(predictionText[userWord] / totalPredictionWords)


    # Sort the dictionary alphabetically and then based on the predicted words that appear more often
    predictionText = sorted(predictionText.items(), key = operator.itemgetter(0))
    predictionText.sort(key = lambda score: score[1], reverse=True)

    # Join the predicted word to a list that follows the required format
    for index in range(len(predictionText)):
        finalPrediction.append(predictionText[index][0] + "," + predictionText[index][1])

    # Print the required words with a ';' in between each word in order to match the required format
    print ";".join(finalPrediction)