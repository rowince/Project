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