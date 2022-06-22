for row in range(7):
    for col in range(5):
        if (row == 0):
            print('*', end=' ')
        elif (col == 2):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()