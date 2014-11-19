import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# LX: the X position of the light of power
# LY: the Y position of the light of power
# TX: Thor's starting X position
# TY: Thor's starting Y position
LX, LY, TX, TY = [int(i) for i in raw_input().split()]

# Thor's current position based on starting position
X = TX
Y = TY

# game loop
while 1:
    E = int(raw_input()) # The level of Thor's remaining energy, representing the number of moves he can still make.

    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."

    # calculate Thor's current position
    directions = (LX - X, LY - Y)
    output = ''

    # check horizontal direction
    if directions[1] < 0:
        Y -= 1
        output += 'N'

    if directions[1] > 0:
        Y += 1
        output += 'S'

    # check vertical direction
    if directions[0] < 0:
        X -= 1
        output += 'W'

    if directions[0] > 0:
        X += 1
        output += 'E'

    print output
