def q_sort(arr):
    if len(arr) == 0:
        return []

    left = []
    right = []
    pivot = arr[len(arr) - 1]
    x = 0

    while x < (len(arr) - 1):
        if pivot > arr[x]:
            left.append(arr[x])
        else:
            right.append(arr[x])

        x += 1
    
    output = q_sort(left) + [pivot] + q_sort(right)
    return output

print(q_sort([12312,44,535345,35,6423,436543,234,265,32,32,4,4,4,2,34,232,2,3,434,2,2,11,1,412,25,2,52,5]))