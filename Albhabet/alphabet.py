print('Enter your Alphabet:-', end=' ')
x = input()
y = x.upper()


def fun(alpha):
    if alpha == 'A':
        for row in range(7):
            for col in range(5):
                if (row in (0, 3)) and (col in (1, 2, 3)):
                    print('*', end=' ')
                elif (row != 0) and (col in (0, 4)):
                    print('*', end=' ')
                else:
                    print(' ', end=' ')
            print()
    elif alpha == 'B':
        for row in range(7):
            for col in range(5):
                if (row in (0, 3, 6)) and (col != 4):
                    print('*', end=' ')
                elif (row in (1, 2, 4, 5)) and (col in (0, 4)):
                    print('*', end=' ')
                else:
                    print(' ', end=' ')
            print()
    elif alpha == 'C':
        for row in range(7):
            for col in range(5):
                if (row in (0, 6)) and (col in (1, 2, 3)):
                    print('*', end=' ')
                elif (row in (1, 5)) and (col in (0, 4)):
                    print('*', end=' ')
                elif (row in (2, 3, 4)) and (col == 0):
                    print('*', end=' ')
                else:
                    print(' ', end=' ')
            print()
    elif alpha == 'D':
        for row in range(7):
            for col in range(5):
                if (row in (1, 2, 3, 4, 5)) and (col in (0, 4)):
                    print('*', end=' ')
                elif (row in (0, 6)) and (col in (0, 1, 2, 3)):
                    print('*', end=' ')
                else:
                    print(' ', end=' ')
            print()
    elif alpha == 'E':
        for row in range(7):
            for col in range(5):
                if (row in (0, 3, 6)):
                    print('*', end=' ')
                elif (row not in (0, 3, 6)) and (col == 0):
                    print('*', end=' ')
                else:
                    print(' ', end=' ')
            print()
    elif alpha == 'F':
        for row in range(7):
            for col in range(5):
                if (row in (0, 3)):
                    print('*', end=' ')
                elif(row not in (0, 3)) and (col == 0):
                    print('*', end=' ')
                else:
                    print(' ', end=' ')
            print()
    elif alpha == 'G':
        for row in range(7):
            for col in range(5):
                if (row in (0, 6)) and (col in (1, 2, 3)):
                    print('*', end=' ')
                elif (row in (1, 2, 3)) and (col == 0):
                    print('*', end=' ')
                elif(row in (1, 4, 5)) and (col in (0, 4)):
                    print('*', end=' ')
                elif(row == 3) and (col in (2, 3)):
                    print('*', end=' ')
                else:
                    print(' ', end=' ')
            print()
    elif alpha == 'H':
        for row in range(7):
            for col in range(5):
                if(col in (0, 4)):
                    print('*', end=' ')
                elif (row == 3) and (col in (1, 2, 3)):
                    print('*', end=' ')
                else:
                    print(' ', end=' ')
            print()
    elif alpha == 'I':
        for row in range(7):
            for col in range(5):
                if (row in (0, 6)) or (col == 2):
                    print('*', end=' ')
                else:
                    print(' ', end=' ')
            print()
    elif alpha == 'J':
        for row in range(7):
            for col in range(5):
                if (row in (0, 6)) and (col in (1, 2, 3)):
                    print('*', end=' ')
                elif (row != 6) and (col == 4):
                    print('*', end=' ')
                elif (row in (0, 5)) and (col == 0):
                    print('*', end=' ')
                else:
                    print(' ', end=' ')
            print()
    elif alpha == 'K':
        for row in range(7):
            for col in range(5):
                if (col == 0):
                    print('*', end=' ')
                elif (row == 3) and (col == 1):
                    print('*', end=' ')
                elif (row in (2, 4)) and (col == 2):
                    print('*', end=' ')
                elif (row in (1, 5)) and (col == 3):
                    print('*', end=' ')
                elif (row in (0, 6)) and (col == 4):
                    print('*', end=' ')
                else:
                    print(' ', end=' ')
            print()
    elif alpha == 'L':
        for row in range(7):
            for col in range(5):
                if (row == 6) or (col == 0):
                    print('*', end=' ')
                else:
                    print(' ', end=' ')
            print()

    elif alpha == 'M':
        for row in range(7):
            for col in range(5):
                if (col in (0, 4)):
                    print('*', end=' ')
                elif (row == 1) and (col in (1, 3)):
                    print('*', end=' ')
                elif (row == 2) and (col == 2):
                    print('*', end=' ')
                else:
                    print(' ', end=' ')
            print()
    elif alpha == 'N':
        for row in range(7):
            for col in range(5):
                if (col in (0, 4)):
                    print('*', end=' ')
                elif (row == 2) and (col == 1):
                    print('*', end=' ')
                elif (row == 3) and (col == 2):
                    print('*', end=' ')
                elif (row == 4) and (col == 3):
                    print('*', end=' ')
                else:
                    print(' ', end=' ')
            print()
    elif alpha == 'O':
        for row in range(7):
            for col in range(5):
                if (row in (0, 6)) and (col in (1, 2, 3)):
                    print('*', end=' ')
                elif (row not in (0, 6)) and (col in (0, 4)):
                    print('*', end=' ')
                else:
                    print(' ', end=' ')
            print()
    elif alpha == 'P':
        for row in range(7):
            for col in range(5):
                if (row in (1, 2)) and (col in (0, 4)):
                    print('*', end=' ')
                elif (row in (3, 4, 5, 6)) and (col == 0):
                    print('*', end=' ')
                elif (row in (0, 3)) and (col in (1, 2, 3)):
                    print('*', end=' ')
                else:
                    print(' ', end=' ')
            print()

    elif alpha == 'Q':
        for row in range(7):
            for col in range(5):
                if (row not in (0, 6)) and (col in (0, 4)):
                    print('*', end=' ')
                elif (row in (0, 6)) and (col not in (0, 4)):
                    print('*', end=' ')
                elif (row == 5) and (col == 3):
                    print('*', end=' ')
                elif (row == 4) and (col == 2):
                    print('*', end=' ')
                else:
                    print(' ', end=' ')
            print()
    elif alpha == 'R':
        for row in range(7):
            for col in range(5):
                if (col == 0):
                    print('*', end=' ')
                elif (row in (1, 2, 6)) and (col == 4):
                    print('*', end=' ')
                elif (row in (0, 3)) and (col in (1, 2, 3)):
                    print('*', end=' ')
                elif (row == 4) and (col == 2):
                    print('*', end=' ')
                elif (row == 5) and (col == 3):
                    print('*', end=' ')
                else:
                    print(' ', end=' ')
            print()
    elif alpha == 'S':
        for row in range(7):
            for col in range(5):
                if (row in (0, 6)):
                    print('*', end=' ')
                elif (row in (1, 5)) and (col in (0, 4)):
                    print('*', end=' ')
                elif (row == 2) and (col == 1):
                    print('*', end=' ')
                elif (row == 3) and (col == 2):
                    print('*', end=' ')
                elif (row == 4) and (col == 3):
                    print('*', end=' ')
                else:
                    print(' ', end=' ')
            print()
    elif alpha == 'T':
        for row in range(7):
            for col in range(5):
                if (row == 0):
                    print('*', end=' ')
                elif (col == 2):
                    print('*', end=' ')
                else:
                    print(' ', end=' ')
            print()
    elif alpha == 'U':
        for row in range(7):
            for col in range(5):
                if (row != 6) and (col in (0, 4)):
                    print('*', end=' ')
                elif (row == 6) and (col not in (0, 4)):
                    print('*', end=' ')
                else:
                    print(' ', end=' ')
            print()
    elif alpha == 'V':
        for row in range(7):
            for col in range(5):
                if (row in (0, 1, 2, 3, 4)) and (col in (0, 4)):
                    print('*', end=' ')
                elif (row == 5) and (col in (1, 3)):
                    print('*', end=' ')
                elif (row == 6) and (col == 2):
                    print('*', end=' ')
                else:
                    print(' ', end=' ')
            print()
    elif alpha == 'W':
        for row in range(7):
            for col in range(5):
                if (col in (0, 4)):
                    print('*', end=' ')
                elif (row == 5) and (col in (1, 3)):
                    print('*', end=' ')        
                elif (row == 4) and (col == 2):
                    print('*', end=' ')
                else:
                    print(' ', end=' ')
            print()
    elif alpha == 'X':
        for row in range(7):
            for col in range(5):
                if (row in (0, 6)) and (col in (0, 4)):
                    print('*', end=' ')
                elif (row in (1, 5)) and (col in (1, 3)):
                    print('*', end=' ')
                elif (row in (2, 4)) and (col == 2):
                    print('*', end=' ')
                elif (row == 3) and (col == 2):
                    print('*', end=' ')
                else:
                    print(' ', end=' ')
            print()
    elif alpha == 'Y':
        for row in range(7):
            for col in range(5):
                if (row == 0) and (col in (0, 4)):
                    print('*', end=' ')
                elif (row == 1) and (col in (1, 3)):
                    print('*', end=' ')
                elif (row not in (0, 1)) and (col == 2):
                    print('*', end=' ')
                else:
                    print(' ', end=' ')
            print()
    elif alpha == 'Z':
        for row in range(7):
            for col in range(5):
                if (row in (0, 6)):
                    print('*', end=' ')
                elif (row == 1) and (col == 4):
                    print('*', end=' ')
                elif (row == 2) and (col == 3):
                    print('*', end=' ')
                elif (row == 3) and (col == 2):
                    print('*', end=' ')
                elif (row == 4) and (col == 1):
                    print('*', end=' ')
                elif (row == 5) and (col == 0):
                    print('*', end=' ')
                else:
                    print(' ', end=' ')
            print()
    else:
        print('Please Enter The Valid Alphabet')


fun(y)
