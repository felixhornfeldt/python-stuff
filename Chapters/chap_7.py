def while_input():
    # # Rental Car 7-1
    # inp = input("What type of car would you like to rent? ")

    # print("I will see if we have a "+inp+" available.")

    # # Resturant Service 7-2
    # people = int(input("How many people wil be dining? "))

    # if people > 8:
    #     print("Your table will be ready soon.")
    #     pass
    # else:
    #     print("Your table is ready.")
    #     pass
    
    # # Multiples of Ten 7-3
    # number = int(input("Please input a number: "))

    # if number % 10 == 0:
    #     print(str(number)+" is a multiple of ten")
    #     pass
    # else:
    #     print(str(number)+" is not a multiple of ten")
    #     pass

    # Pizza Toppings 7-4
    message = "Write a topping and we'll add it or write quit to quit: "
    while True:
        topping = input(message)
        if topping == "quit":
            break
        else:
            print("Let me get that "+topping+" for you")
            pass
    pass

    # Movie Tickets 7-5
    message = "Please declare your age: "
    while True:
        age = input(message)
        if age == "quit":
            break
        if int(age) < 3:
            print("Ticket is free")
        elif int(age) > 3 and int(age) <= 12:
            print("10$")
        elif int(age) > 12:
            print("15$")
        pass
    
    # 

while_input()