import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

R = int(raw_input()) # the length of the road before the gap.
G = int(raw_input()) # the length of the gap.
L = int(raw_input()) # the length of the landing platform.

jumped = False

# game loop
while 1:
    S = int(raw_input()) # the motorbike's speed.
    X = int(raw_input()) # the position on the road of the motorbike.

    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."

    if not jumped:
        if S == G + 1:
            if S > R - X:
                jumped = True
                print "JUMP"
            else:
                print "WAIT"
        elif S > G + 1:
            print "SLOW"
        elif S < R - X or S < g:
            print "SPEED"
        elif S >= G + R - X - 1:
            jumped = True
            print "JUMP"
        else:
            print "SLOW"
    else:
        print "SLOW"

