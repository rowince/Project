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
