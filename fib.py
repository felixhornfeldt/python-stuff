import math
import matplotlib.pyplot as plt

def fib_f(n):
    f = [1,1]
    for x in range(2,n+1):
        f.append(f[x-1] + f[x-2])
    return f

def fib_r(l,n):
    def r_calc(x):
        return l[x]/l[x-1]
    r = r_calc(n)
    r_1 = r_calc(n-1)
    return abs(r-r_1)

class Fib():
    def __init__(self, n):
        self.n = n
        self.f = fib_f(n)
        self.r = fib_r(self.f,n)

n = 41
y_val = []
x_val = [x for x in range(2,n)]
for x in range(2,n):
    v = math.log(Fib(x).r)
    y_val.append(v)
    print("R"+str(x)+": "+str(v))

plt.plot(x_val, y_val)
plt.show()
