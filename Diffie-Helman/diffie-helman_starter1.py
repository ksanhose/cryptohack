p = 991
g = 209
d = 1

for d in range(0, 10000):
    if (g*d) % 991 == 1:
        print(d)
    else:
        d += 1
