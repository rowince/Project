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