file = open("Strings.txt") # File must be on the root of the project folder

#*********Quick sort*********#
# Array will be sorted in descending order
def quickSort(charArray):
   quickSortHelper(charArray,0,len(charArray)-1)

def quickSortHelper(charArray, left, right):
    if(left < right):
        pivotIndex = partition(charArray, left, right)

        quickSortHelper(charArray, left, pivotIndex-1)
        quickSortHelper(charArray, pivotIndex+1, right)

def partition(alist, left, right):
    pivotIndex = left
    pivotvalue = alist[pivotIndex][1]

    leftmark = left
    rightmark = right

    done = False
    while leftmark < rightmark:

        while leftmark <= rightmark and alist[leftmark][1] >= pivotvalue:
            leftmark += 1

        while rightmark >= leftmark and alist[rightmark][1] <= pivotvalue:
            rightmark -= 1

        if(leftmark < rightmark):
            swap(alist, leftmark, rightmark)

    swap(alist, left, rightmark)
    return rightmark

def swap(charArray, index1, index2):
    temp = charArray[index1]
    charArray[index1] = charArray[index2]
    charArray[index2] = temp
#*********Quick sort*********#

# Loop through all of the lines in the file
for tempString in file:

    # Check to see if the line is a \n. If so, skip it
    if(len(tempString) == 1):
        if(not tempString.isalpha()):
            continue

    popularChar = {}    # Empty dictionary that will be used to store the char in the string
    points = 0
    beauty = 26

    # Remove the spaces in the string, make all characters lowercase, and loop through each character
    for char in tempString.lower().replace(" ", ""):
        if (char.isalpha()):
            # Check to see if the char is already in the dictionary
            # If it is, then add a tally to the char, else, create a new entry
            if (char in popularChar.keys()):
                popularChar[char] += 1
            else:
                popularChar[char] = 1

    # Convert the hash table into an array and sort the array
    popularCharArray = popularChar.items()
    quickSort(popularCharArray)

    #Loop through the reversed array and assign the appropriate beauty points
    for char, val in popularCharArray:
        points += (val * beauty)
        beauty -= 1

    print points