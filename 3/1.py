fp = '3/input.txt'
dat = open(fp).read().splitlines()

route = (3, 1)

c = 0

for v in range(0, len(dat), route[1]):
    h = int(divmod((v / route[1]) * route[0], len(dat[v]))[1])
    value = dat[v][h]
    if value == '#':
        c += 1

print(c)
