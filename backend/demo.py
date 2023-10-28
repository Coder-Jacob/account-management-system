rows = 5  # 更改这个数字以调整三角形的大小
for i in range(rows, 0, -1):
    for j in range(i):
        print('*', end='')
    print()
