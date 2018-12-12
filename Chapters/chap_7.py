def while_input():
    # Rental Car 7-1
    inp = input("What type of car would you like to rent? ")

    print("I will see if we have a "+inp+" available.")

    # Resturant Service 7-2
    people = int(input("How many people wil be dining? "))

    if people > 8:
        print("Your table will be ready soon.")
        pass
    else:
        print("Your table is ready.")
        pass
    
    # Multiples of Ten 7-3
    number = int(input("Please input a number: "))

    if number % 10 == 0:
        print(str(number)+" is a multiple of ten")
        pass
    else:
        print(str(number)+" is not a multiple of ten")
        pass

    #  7-4
    

    pass

while_input()