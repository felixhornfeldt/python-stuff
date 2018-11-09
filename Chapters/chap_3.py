def func_lists_3():
    # Names 3-1
    friends = ["Emil", "Karl", "Sebastian"]
    print(friends[0]+"\n"+friends[1]+"\n"+friends[2])

    # Greetings 3-2
    print("Hello "+friends[0]+"\n"+"Hello "+friends[1]+"\n"+"Hello "+friends[2])

    # Your own list 3-3
    cars = ["Audi", "Porsche", "Volvo"]
    print("I would like to have a "+cars[-1])

    # Guest list 3-4
    guests = ["Myself", "Andi", "Ballony", "Hell"]
    for x in guests:
        print(x+", would you like to have dinner with some friends")
    
    # Changing Guest List 3-5
    not_coming_guest = guests.pop()
    print(not_coming_guest+" is not coming to dinner")
    coming_guest = "Blet"
    guests.append(coming_guest)
    for x in guests:
        print(x+", is commmmmmming")

    # More Guests 3-6
    print("I found a bigger table")
    guests.insert(0, "biget")
    guests.insert(3, "Yatmon")
    guests.append("Telloytok")
    for x in guests:
        print(x+", Would you like to come to dinner")
    
    # Shrinking Guest List 3-7
    print("My new table didn't come, I only have space for two")
    print(len(guests))
    while len(guests) > 2:
        a = guests.pop()
        print(a+", I'm sorry but i have to infrom you that you can't come to dinner")
    for x in guests:
        print(x+", You are still invited to dinner with me")
    del guests[0]
    del guests[0]
    print(guests)

    # Seeing the World 3-8
    places = ["New York", "Hawaii", "Liverpool", "Glasgow", "Hong Kong"]
    print(places)
    print(sorted(places))
    print(places)
    places.reverse()
    print(places)
    places.reverse()
    print(places)
    places.sort()
    print(places)
    places.sort(reverse=True)
    print(places)

    # Dinner Guests 3-9
    print(len(guests))
    print(len(places))

    # Every Function 3-10
    countries = ["Botswana", "Sweden", "Denmark", "Finland", "Norway"]
    countries.append("Russia")
    countries.insert(1, "Scotland")
    del countries[2]
    countries.pop(0)
    countries.remove("Russia")
    print(sorted(countries))
    countries.reverse()
    print(countries)
    countries.sort()
    print(countries)
    print(len(countries))

func_lists_3()