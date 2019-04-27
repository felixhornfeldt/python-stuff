# a = ["Hello", "world", "from", "array"]


# def msg():
#     op = 0
#     for b in a:
#         op += 1
#         print(b)
#     print(str(op))

# msg()

def arr_sum(arr, n):
    e = []
    for x in arr:
        if x in e:
            return True
        elif (n-x) in e:
            continue
        else:
            e.append(n-x)
    
    return False

print(arr_sum([9,1,1,0], 9))