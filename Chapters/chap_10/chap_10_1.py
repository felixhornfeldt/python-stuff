with open('l_python.txt') as file_obj:
    print(file_obj.read())
    pass

print("\n")

with open('l_python.txt') as file_obj:
    for i in file_obj:
        print(i)
    pass

print("\n")

with open('l_python.txt') as file_obj:
    arr = file_obj.readlines()
    pass

for i in arr:
    print(i.strip())