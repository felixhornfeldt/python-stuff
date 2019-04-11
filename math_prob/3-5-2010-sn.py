import math
import matplotlib.pyplot as plt

def master(t,n):
    l = [t**x for x in range(1,4)]
    def calc():
        return (l[-1]+l[-3])/(l[-2])
    
    for z in range(4, n+1):
        l.append(calc())
    
    s = l[-1]+l[-2]+l[-3]+l[-4]
    return s

n = 123456
a = -100
b = 100
y_val_1 = []
def abc(n):
    if n == 0:
        return False
    elif n == -1:
        return False
    else:
        return True

x_val = [x for x in range(a,b+1,) if abc(x)]
y_val_2 = [x**3 for x in x_val]
for x in x_val:
    if x != 0:
        y_val_1.append(master(x,n))
        print("S"+str(x))

plt.plot(x_val, y_val_1, label="s", color="purple")
plt.plot(x_val, y_val_2, label="x3", color="orange")
plt.show()