for row in range(7):
    for col in range(5):
        if (row in (0, 3)):
            print('*', end=' ')
        elif(row not in (0, 3)) and (col == 0):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
