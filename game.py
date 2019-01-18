gridLength = 28
gridWidth = 19
soccerBootsPickedUp = False
soccerBallPickedUp = False
defender1Fought = False
defender2Fought = False
defender3Fought = False
defender4Fought = False
goalieFought = False
goalScored = False


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
for x in range(gridLength):
    for y in range(gridWidth):
        gridSquare = GridSquare(x, y)
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
soccerBall = GridSquare(25, 9)
soccerBoots = GridSquare(15, 8)

player = Player(13, 10)


def gridCompare(grid, p=player):
    for i in grid:
        if p.xPos == i.xPos and p.yPos == i.yPos:
            return True
    return False


def locationOfPlayer(p=player):
    num = 8
    for i in [H1, H2, H3, H4, H5, H6, H7, H8, H9, H10, H11, H12]:
        num += 1
        if gridCompare(i, p):
            return num
    if gridCompare(room1, p):
        return 1
    if gridCompare(room2, p):
        return 2
    if gridCompare(room3, p):
        return 3
    if gridCompare(room4, p):
        return 4
    if gridCompare(room5, p):
        return 5
    if gridCompare(endZone1, p):
        return 6
    if gridCompare(endZone2, p) and not gridCompare(goal, p):
        return 7
    if gridCompare(goal, p):
        return 8
    else:
        return num + 1


def locationEquals(gridSquareObj):
    if player.xPos == gridSquareObj.xPos and player.yPos == gridSquareObj.yPos:
        return True
    else:
        return False


def verifyMove(usr_in):
    if usr_in == 'e':
        playerFutureState = Player(player.xPos + 1, player.yPos)
        return locationOfPlayer(playerFutureState)
    if usr_in == 'w':
        playerFutureState = Player(player.xPos - 1, player.yPos)
        return locationOfPlayer(playerFutureState)
    if usr_in == 'n':
        playerFutureState = Player(player.xPos, player.yPos + 1)
        return locationOfPlayer(playerFutureState)
    if usr_in == 's':
        playerFutureState = Player(player.xPos, player.yPos - 1)
        return locationOfPlayer(playerFutureState)


def getRoomInfo():
    if locationOfPlayer() in range(8, 22):
        print('You entered a new hallway')
    if locationOfPlayer() == 1:
        print('This is room 1')
    if locationOfPlayer() == 2:
        print('You are in room 2')
    if locationOfPlayer() == 3:
        print('You are in room 3')
    if locationOfPlayer() == 4:
        print('You are in room 4')
    if locationOfPlayer() == 5:
        print('You are in room 5')
    if locationOfPlayer() == 6:
        print('You are in end zone 1')
    if locationOfPlayer() == 7:
        print('You are in end zone 2')
    if locationOfPlayer() == 8:
        print('in goal')


previousLocation = locationOfPlayer()
currentLocation = locationOfPlayer()


def movePlayer(usrIn):
    if usrIn == 'e':
        player.moveEast()
    if usrIn == 'w':
        player.moveWest()
    if usrIn == 'n':
        player.moveNorth()
    if usrIn == 's':
        player.moveSouth()


def enteredNewRoom():
    global previousLocation
    global currentLocation
    if currentLocation != previousLocation:
        getRoomInfo()
        previousLocation = currentLocation
        return True
    else:
        return False

def gameObjectsPickedUp():
    global soccerBootsPickedUp
    global soccerBallPickedUp
    if locationEquals(soccerBall) and soccerBallPickedUp == False and soccerBootsPickedUp == True:
        print('You have come across the soccer ball. You now have possession of the ball.')
        soccerBallPickedUp = True
    if locationEquals(soccerBall) and soccerBallPickedUp == False and soccerBootsPickedUp == False:
        print('You have come across the soccer ball, but you can not get it because you don\'t have soccer boots.')
    if locationEquals(soccerBoots) and soccerBootsPickedUp == False:
        print('You have come across some soccer boots. You have now put on the soccer boots')
        soccerBootsPickedUp = True


def fightDefender():
    if locationEquals(defender1) and defender1Fought == False:
        usrIn = str(input('You have come across a defender. Do you choose to fight him? Enter \'y\' or \'n\'')).strip()
        if usrIn == 'y':
            return True
        else:
            return False
    if locationEquals(defender2) and defender2Fought == False:
        usrIn = str(input('You have come across a defender. Do you choose to fight him? Enter \'y\' or \'n\'')).strip()
        if usrIn == 'y':
            return True
        else:
            return False
    if locationEquals(defender3) and defender3Fought == False:
        usrIn = str(input('You have come across a defender. Do you choose to fight him? Enter \'y\' or \'n\'')).strip()
        if usrIn == 'y':
            return True
        else:
            return False
    if locationEquals(defender4) and defender4Fought == False:
        usrIn = str(input('You have come across a defender. Do you choose to fight him? Enter \'y\' or \'n\'')).strip()
        if usrIn == 'y':
            return True
        else:
            return False
    if locationEquals(goalie) and goalieFought == False:
        usrIn = str(input('You have come across the goalie. Do you choose to fight him? Enter \'y\' or \'n\'')).strip()
        if usrIn == 'y':
            return True
        else:
            return False
    return True


def move(usrIn):
    global goalScored
    global currentLocation
    if verifyMove(usrIn) == 21:
        print('Oh no. You have just hit a wall. Try Again')
        return
    if verifyMove(usrIn) == 7 and soccerBallPickedUp == True and enteredNewRoom() == True:
        print('You have the soccer ball. You are able to go to the Second End Zone.')
        movePlayer(usrIn)
        currentLocation = locationOfPlayer()
        enteredNewRoom()
    if verifyMove(usrIn) == 7 and soccerBallPickedUp == False and enteredNewRoom() == False:
        print('You don\'t have the soccer ball. You are unable to go to the Second End Zone.')
    if verifyMove(usrIn) == 8 and enteredNewRoom() == True:
        print('You have scored the goal. You have won the game.')
        movePlayer(usrIn)
        goalScored = True
    else:
        if fightDefender():
            movePlayer(usrIn)
            currentLocation = locationOfPlayer()
            enteredNewRoom()
        else:
            print('The defender is blocking your way. You have to fight to get past him or go around.')


while goalScored == False:
    print('__________________________________')
    print("Move Options: 'n', 's', 'e', 'w'")
    userIn = str(input('Enter a move: ')).strip()
    print('')
    move(userIn)
    print('Position: (' + str(player.xPos) + ', ' + str(player.yPos) + ')')
