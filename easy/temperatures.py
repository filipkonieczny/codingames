import sys, math


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

N = int(raw_input()) # the number of temperatures to analyse

while True:
    if N == 0:
        print 0
        break

    try:
        TEMPS = raw_input() # the N temperatures expressed as integers ranging from -273 to 5526
    except EOFError:
        print 0
        break

    result = 0
    temperature = ''
    TEMPS += ' '

    for i in TEMPS:
        if i != " ":
            temperature += i
        else:
            temperature = int(temperature)

            if result == 0:
                result = temperature

            abs_temperature = abs(temperature)

            if abs_temperature <= abs(result) and abs_temperature != 0:
                result = temperature
            temperature = ''

    print result
    break
