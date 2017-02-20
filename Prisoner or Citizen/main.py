import sys

# Check to see if person is on prison wall
def onXLine(point0, point1, personPoint):
    if point0[0] <= point1[0]:
        return point0[0] <= personPoint[0] and personPoint[0] <= point1[0]

    return point0[0] >= personPoint[0] and personPoint[0] >= point1[0]

# Return which side of the wall the prisoner is in
def clockOrCounterClock(point0, point1, personPoint):
    return (((personPoint[0] - point0[0])*(point1[1] - point0[1])) - ((personPoint[1]-point0[1])*(point1[0]-point0[0])))

def checkIfPrisoner(prisonCoords, personPoint):
    sideOfWall = 0  # Keep track of which side of the wall the person is. -1 is clockwise, +1 is counter clockwise

    for i in range(len(prisonCoords) - 1):
        point0, point1 = prisonCoords[i], prisonCoords[i + 1]

        # Check if person is between the wall points in the y-axis
        if point1[1] >= personPoint[1] and personPoint[1] > point0[1] or point0[1] >= personPoint[1] and personPoint[1] > point1[1]:
            side = clockOrCounterClock(point0, point1, personPoint)
            if side > 0:
                sideOfWall -= 1
            elif side < 0:
                    sideOfWall += 1
            elif side == 0:
                return True # If on wall, the person is prisoner. Return true

        # If person is on the same level as the wall. Check if on the wall.
        elif point0[1] == personPoint[1] and onXLine(point0, point1, personPoint):
            return True # If on wall, the person is prisoner. Return true

    return sideOfWall != 0  # If the prisoner is not between the walls, then sideOfWall will be zero and return false


def main():
    for case in test_cases:

        # Grab the prison and the person's coordinates
        prisonCoordinates, personCoordinates = case.split('|')

        # Seperate the prison's coordinates
        prisonCoords = list()
        for xy in prisonCoordinates.split(','):
            x, y = xy.split()
            prisonCoords.append((int(x), int(y)))

        # Close the prison by adding the first coordinate to the end
        prisonCoords.append(prisonCoords[0])

        # Split the person's coordinate
        x, y = personCoordinates.split()
        personPoint = (int (x), int (y))

        # Check if person is a prisoner
        isPrisoner = checkIfPrisoner(prisonCoords, personPoint)

        if(isPrisoner):
            print "Prisoner"
        else:
            print "Citizen"


# test_cases = open(sys.argv[1], 'r')
test_cases = ["1 1, 1 4, 3 4, 3 2 | 2 3", "1 1, 3 2, 1 4, 3 4 | 3 3"]
main()