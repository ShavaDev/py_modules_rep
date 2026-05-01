from logging import operations as ops

lst = [(11, 4), (1, 6), (6, 0), (9, 5), (0, 3)]

if __name__ == '__main__':
    for i, j in lst:
        ops.add(i, j)
        ops.sub(i, j)
        ops.mul(i, j)
        ops.div(i, j)
