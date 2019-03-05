n = [i for i in range(1000) if i%3 == 0 or i%5 == 0]

del n[0]

o = 1

for i in n:
    o *= i

print(o)