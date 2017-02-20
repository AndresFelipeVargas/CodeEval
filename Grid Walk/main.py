'''###########################################################################
This is a program that count the number of points a monkey can get while walking
on a grid. The criteria for obtaining points is the following: Points where the
sum of the digits of the absolute value of the x coordinate plus the sum of the
digits of the absolute value of the y coordinate are lesser than or equal to 19
are accessible to the monkey.

Using the above criteria, the maximum amount of distance that the monkey can travel
in the x direction is (298, 0). This will result in 2+9+8+0= 19. Same goes for the
negative x direction (-298,0) which will also result in  19. Same idea applies to
the y direction. So, the grid that can be used will be a 601x601 grid. 601 rows/cols
is done to account for a 0th row, and 300 rows in both direction of the 0th row.

Andres Felipe Vargas                                                   11/11/16
###########################################################################'''

# As told above, the grid that would be required would be a 601x601 grid.
# Since the grid is made of of 4 quadrants, and the sum is dependent on the absolute
# value of the location, we can say that all of the 4 quadrant would yield the same result.
#  _________
# |    |    |
# |_A__|_B__|
# |    |    |
# |_C__|_D__|
#
# This means that the problem can be split into 4 equal portions.
#  _____________________
# |          |        |
# |          |        |
# |____A`____|        |
# |        |_|___B`___|
# |        |          |
# |        |          |
# |____C`__|_____D`___|
#
# So, we only need to measure one portion, and multiply the result by 4 and add
# 1 point to accommodate for the origin (0,0). Each quadrant can also be made up of 9 sections.
#  ______________
# |    |    |    |
# |_3__|_6__|_9__|
# |    |    |    |
# |_2__|_5__|_8__|
# |    |    |    |
# |_1__|_4__|_7__|
#
# Due to the nature of the problem, the final result will resemble a triangle. This means that
# only 6 sections will be visited.
#
# |\
# |_3\______
# |    |\   |
# |_2__|_5\_|____
# |    |    |\   |
# |_1__|_4__|_7\_|
#
# Out of these 6 sections, they can all be derived from 3 sections:
# Case 1: Section 1 which is from x = 0 to x = 99 and y = 0 and y = 99.
# Case 2: Section 2 which is from x = 0 to x = 99 and y = 100 and y = 199.
# Case 3: Section 3 which is from x = 0 to x = 99 and y = 200 and y = 299.
# The geometry of the problem allows for the for section 2 and 4 to be identical and section 3, 5,
# and 7 to also be identical. This means that by finding the points in section 1, section 2, and
# section 3, and multiplying them by the amount of identical sections, the quadrants points can be found.
#
# In order to multiply the quadrant by 4, the origin and the longest strip must be remove. This is done to match
# the 4 equal portions mentioned above. Once this is done, then the points are multiplied by 4 and the origin is added.
# This results in the solution.

# Get the sum of the digits in the tuple
def sumOfDigits(nodes):
    n1 = abs(nodes[0])
    n2 = abs(nodes[1])
    r1 = 0
    r2 = 0

    while n1:
        r1 = r1 + n1 % 10
        n1 = n1 / 10
    while n2:
        r2 = r2 + n2 % 10
        n2 = n2 / 10

    return r1 + r2

# Get the neighboring nodes of the node passed
def neighbors(node, visitedNodes, case):
    # Since the problem is broken into 4 portion, the positive quadrant is being examined.
    # So only positive moves are valid.
    possibleMoves= [(1,0),(0,1)]
    allNeighbors = []
    for move in possibleMoves:
        neighbor = (node[0] + move[0], node[1] + move[1])

        sum = sumOfDigits(neighbor)

        # Check to see if the possible moves meet the criteria of summation and has not yet been visited.
        # If the above is true, check which case it falls under and add the list accordingly
        if (sum <= 19 and neighbor and neighbor not in visitedNodes):
            if (case == 1 and neighbor[0] < 100 and neighbor[1] < 100):
                    allNeighbors.append(neighbor)
            elif (case == 2 and neighbor[0] < 100 and neighbor[1] < 200):
                    allNeighbors.append(neighbor)
            elif (case == 3 and neighbor[0] < 100 and neighbor[1] < 300):
                    allNeighbors.append(neighbor)

    return allNeighbors

# Breadth First Search solution

def bfs(start, case):
    visitedNodes = {}   # Dictionary that will hold the nodes that were visited
    visitedNodes[start]= True
    Q = []              # List that will be used to hold nodes that need to be inspected first
    Q.append(start)
    while Q:    # Run while queue is not empty
        node = Q.pop() # Pop out the first value in the queue

        # Grab all of the neighbors of the node that have not been visited
        neighborsList = sorted(neighbors(node, visitedNodes, case))

        # Add the valid nodes to both the visitedNodes and to the Queue
        for neighbor in neighborsList:
            visitedNodes[neighbor] = True
            Q.append(neighbor)

    return len(visitedNodes)    # Return the total number of nodes visited.

# Depth First Search Solution
visitedNodes = {}   # Dictionary that will hold the nodes that were visited

def dfs(root, case):
    visitedNodes[root] = True
    sum = 1     # Set sum = 1 to get the point from the node

    # Grab all of the neighbors of the node that have not been visited
    neighborsList = sorted(neighbors(root, visitedNodes, case))

    # Do a recursive call for the nodes that have yet to be visited
    for neighbor in neighborsList:
        sum += dfs(neighbor, case)


    return sum

def main():
    # Breadth First Search Function. Take less memory and runs faster compared to DPS
    # bfs()
    points1 = bfs((0, 0), 1)        # Get the total points from section of x(0-99) and y(0-99)
    points2 = bfs((0, 100), 2)      # Get the total points from section of x(0-99) and y(100-199)
    points3 = bfs((0, 200), 3)      # Get the total points from section of x(0-99) and y(200-299)
    points = points1 + (2 * points2) + (3 * points3)

    # Depth First Search Function
    # answer1 = dfs((0,0), 1)
    # answer2 = dfs((0,100), 2)
    # answer3 = dfs((0,200), 3)
    # answer = answer1 + (2*answer2) + (3*answer3)

    points -= 1     # Remove the origin (0,0)
    points -= 298   # Remove one of the origin strips
    points *= 4     # Multiply by 4 to get the square
    points += 1     # Add the point from the origin

    print points

if __name__ == '__main__':
    main()