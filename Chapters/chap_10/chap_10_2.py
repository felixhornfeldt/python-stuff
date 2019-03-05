with open('l_python.txt') as file_obj:
    arr = file_obj.readlines()
    for i in arr:
        print(i.replace('python', 'c').strip())
    pass