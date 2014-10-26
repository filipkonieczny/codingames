import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


# game loop
while 1:
    highest_mountain = 0
    max_height = 0

    SX, SY = [int(i) for i in raw_input().split()]
    for i in xrange(8):
        MH = int(raw_input()) # represents the height of one mountain, from 9 to 0. Mountain heights are provided from left to right.
        if MH > max_height:
            max_height = MH
            highest_mountain = i

    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."
    if SX == highest_mountain:
        print "FIRE"
    else:
        print "HOLD" # either:  FIRE (ship is firing its phase cannons) or HOLD (ship is not firing).
