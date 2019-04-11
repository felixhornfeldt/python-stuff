def uppg_3_2(n):
    i = 0
    a = int(n)
    while a > 1:
        if a%2 == 0:
            a /= 2
        else:
            a = a*3+1
        i += 1
    
    return i

print(uppg_3_2(input()))