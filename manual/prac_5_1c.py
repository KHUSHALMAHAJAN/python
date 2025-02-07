rows = 7
for i in range(rows, 0, -2):
    print(' ' * ((rows - i) // 2) + '10' * (i // 2) + '1' * (i % 2))
