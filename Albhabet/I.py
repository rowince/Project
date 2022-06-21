for row in range(7):
    for col in range(5):
        if (row in (0, 6)) or (col == 2):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
