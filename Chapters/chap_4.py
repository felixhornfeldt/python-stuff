def func_loop_list_4():
    # Pizzas 4-1
    pizzas = ["Hawaii", "Kebab", "Pastrami"]
    for pizza in pizzas:
        print(pizza)
        print("I love "+pizza+" pizza")
    print("\nI love pizza in general")

    # Animals 4-2
    animals = ["Tiger", "Lion", "Hyena"]
    for animal in animals:
        print(animal+" would not be a good pet")
    print("There all predators")

    # Counting to Twenty 4-3
    for number in range(1, 21):
        print(number)

    # One million 4-4
    arr = list(range(1,1000001))
    for x in arr:
        print(x)

    # Summing a million 4-5
    print(str(min(arr))+"\n"+str(max(arr))+"\n"+str(sum(arr)))

    # Odd numbers 4-6
    arr = list(range(1,21,2))
    for x in arr:
        print(x)

    # Threes 4-7
    arr = [x*3 for x in range(3,31)]
    for x in arr:
        print(x)
    
    # Cubes 4-8 and 4-9
    arr = [x**3 for x in range(1,11)]
    for x in arr:
        print(x)

    # Slices 4-10
    print(arr[:3])
    print(arr[4:6])
    print(arr[5:])

func_loop_list_4()