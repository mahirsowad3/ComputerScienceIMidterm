gridLength = 28
gridWidth = 19
#previousPlace =
#currentPlace=


class Player(object):
    def __init__(self, xPos, yPos):
        self.xPos = xPos
        self.yPos = yPos

    def moveEast(self):
        if self.xPos + 1 in range(gridLength):
            self.xPos += 1
            print('Successfully ran one step East')
        else:
            print('At the border of the Game Map')

    def moveWest(self):
        if self.xPos - 1 in range(gridLength):
            self.xPos -= 1
            print('Successfully ran one step West')
        else:
            print('At the West border of the Game Map')

    def moveNorth(self):
        if self.yPos + 1 in range(gridWidth):
            self.yPos += 1
            print('Successfully ran one step North')
        else:
            print('At the North border of the Game Map')

    def moveSouth(self):
        if self.yPos - 1 in range(gridWidth):
            self.yPos -= 1
            print('Successfully ran one step South')
        else:
            print('At the South border of the Game Map')


class GridSquare(object):
    def __init__(self, xPos, yPos):
        self.xPos = xPos
        self.yPos = yPos


# Adding all squares to grid
gridSquareStore = []
for i in range(gridLength):
    for j in range(gridWidth):
        gridSquare = GridSquare(i, j)
        gridSquareStore.append(gridSquare)


def assignSpace(startX, endX, startY, endY):
    space = []
    for i in gridSquareStore:
        if i.xPos in range(startX, endX + 1) and i.yPos in range(startY, endY + 1):
            space.append(i)
    return space


room1 = assignSpace(12, 15, 8, 11)
room2 = assignSpace(18, 21, 15, 18)
room3 = assignSpace(6, 9, 15, 18)
room4 = assignSpace(12,15,13,18)
room5 = assignSpace(17, 20, 0, 2)
H1 = assignSpace(1, 2, 2, 4)
H2 = assignSpace(3, 12, 2, 3)
H3 = assignSpace(13, 14, 2, 7)
H4 = assignSpace(7, 11, 9, 10)
H5 = assignSpace(16, 18, 9, 10)
H6 = assignSpace(7, 8, 11, 14)
H7 = assignSpace(19, 20, 3, 14)
H8 = assignSpace(22, 26, 16, 17)
H9 = assignSpace(25, 26, 15, 15)
H10 = assignSpace(21, 25, 0, 1)
H11 = assignSpace(10, 11, 16, 17)
H12 = assignSpace(16, 17, 16, 17)
endZone1 = assignSpace(24, 27, 5, 14)
endZone2 = assignSpace(0, 3, 5, 14)
goal = assignSpace(1, 2, 9, 10)
goalie = GridSquare(1, 7)
defender1 = GridSquare(14, 15)
defender2 = GridSquare(14, 17)
defender3 = GridSquare(25, 12)
defender4 = GridSquare(26, 12)
ball = GridSquare(25, 9)
boots = GridSquare(15, 8)

player = Player(13, 10)


def gridCompare(grid):
    for i in grid:
        if player.xPos == i.xPos and player.yPos == i.yPos:
            return True
    return False


def locationOfPlayer():
    for i in [H1, H2, H3, H4, H5, H6, H7, H8, H9, H10, H11, H12]:
        if gridCompare(i):
            return 0
    if gridCompare(room1):
        return 1
    if gridCompare(room2):
        return 2
    if gridCompare(room3):
        return 3
    if gridCompare(room4):
        return 4
    if gridCompare(room5):
        return 5
    if gridCompare(endZone1):
        return 6
    if gridCompare(endZone2) and not gridCompare(goal):
        return 7
    if gridCompare(goal):
        return 8
    else:
        return 9



def enteredNewRoom(previousLocation, currentLocation):
    if previousLocation != currentLocation:


def move(usr_in):
    if locationOfPlayer() == 10:
        print('Oh no. You have just hit a wall. Try Again')
        return
    if locationOfPlayer() == 0:
