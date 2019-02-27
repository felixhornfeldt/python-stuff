def classes():
    # Restaurant 9-1
    class Restaurant_9_1():
        def __init__(self, restaurant_name, cuisine_type):
            self.name = restaurant_name
            self.ctype = cuisine_type
        
        def describe_restaurant(self):
            print(self.name + "\n" + self.ctype + "\n")
        
        def open_restaurant(self):
            print(self.name + " is now open!")
    
    restaurant_0 = Restaurant_9_1('Indi Resturant', 'indian')

    # Three Restaurants 9-2
    restaurant_1 = Restaurant_9_1('Test Res', 'Test')
    restaurant_2 = Restaurant_9_1('Thai Chi', 'Thai')

    restaurants = [restaurant_0, restaurant_1, restaurant_2]

    for x in restaurants:
        x.describe_restaurant()
    
    # Users 9-3
    class User_9_3():
        def __init__(self, first_name, last_name, email, age):
            self.first_name = first_name
            self.last_name = last_name
            self.full_name = first_name + " " + last_name
            self.email = email
            self.age = age

        def describe_user(self):
            print(self.full_name + "\n" + self.first_name + " is " + str(self.age) + " years old and.\n" + self.email)
        
        def great_user(self):
            print("Hello and welcome " + self.first_name.title() + "\n")

    user_0 = User_9_3("Felix", "Hörnfeldt", "felix.hornfeldt@outlook.com", 18)
    user_1 = User_9_3("Test", "Testesson", "test.testesson@outlook.com", 18)
    user_2 = User_9_3("Yrodl", "Jfjsk", "yrodl.jfjsk@company.com", 18)

    users = [user_0, user_1, user_2]

    for x in users:
        x.describe_user()
        x.great_user()

    ###########################
    class CarExampelClass():
        def __init__(self, brand, model, year, rating):
            self.brand = brand
            self.model = model
            self.year = year
            self.rating = rating
        
        # Given Information
        def g_info(self):
            print("This is the information given:\n\t" + self.brand + "\n\t" + self.model + "\n\t" + str(self.year) + "\n\t" +str(self.rating) + "\n")
    

    CarExampelClass("Volvo", "V40", 2018, 7.5).g_info()
    ###########################

    # Number Served 9-4
    class Restaurant_9_4():
        def __init__(self, restaurant_name, cuisine_type, number_served=0):
            self.name = restaurant_name
            self.ctype = cuisine_type
            self.nserved = number_served

        def describe_restaurant(self):
            print(self.name + "\n" + self.ctype + "\n" + str(self.nserved))
        
        def open_restaurant(self):
            print(self.name + " is now open!")

        def set_number_served(self, new_nserved=0):
            self.nserved = new_nserved
            print(str(self.nserved))
        
        def increment_number_served(self, served_customers=0):
            self.nserved += served_customers
            print(str(self.nserved))

    Restaurant_9_4('Test', 'cyTest').describe_restaurant()
    Restaurant_9_4('Test', 'cyTest', 63).set_number_served(437)
    Restaurant_9_4('Test', 'cyTest', 437).increment_number_served(63)

    # Login Attempts 9-5
    class User_9_5():
        def __init__(self, first_name, last_name, email, age, login_attempts=0):
            self.first_name = first_name
            self.last_name = last_name
            self.full_name = first_name + " " + last_name
            self.email = email
            self.age = age
            self.lattempts = login_attempts

        def describe_user(self):
            print(self.full_name + "\n" + self.first_name + " is " + str(self.age) + " years old and.\n" + self.email)
        
        def great_user(self):
            print("Hello and welcome " + self.first_name.title() + "\n")

        def increment_login_attempts(self):
            self.lattempts += 1
            print(str(self.lattempts))
        
        def reset_login_attempts(self):
            self.lattempts = 0
            print(str(self.lattempts))
    
    user_90 = User_9_5('test', 'testesson', 'test@email.se', 89)
    i = 0
    while i < 5:
        user_90.increment_login_attempts()
        i += 1
        pass
    
    user_90.reset_login_attempts()
    
    # Ice Cream Stand 9-6
    class IceCreamStand(Restaurant_9_4):
        
        def __init__(self, restaurant_name, cuisine_type, number_served=0):
            super().__init__(restaurant_name, cuisine_type, number_served)
            self.flavors = ["Vanilla", "Coco", "Rasberry", "Strawberry", "Oreo"]
        
        def show_flavors(self):
            for i in self.flavors:
                print(i+" flavor is really tasty")
            
    hornen_ice = IceCreamStand("HorNen Ice", "Ice Cream")
    hornen_ice.show_flavors()

    # Admin 9-7
    class Admin(User_9_5):
        def __init__(self, first_name, last_name, email, age, login_attempts=0):
            super().__init__(first_name, last_name, email, age, login_attempts)
            self.privileges = ["can see everything", "can delete user", "rules this site"]

        def show_privileges(self):
            for i in self.privileges:
                print("Admin has this privilege: "+i)
        
    hornen = Admin("Felix", "Hörnfeldt", "hornen@boss.se", 18, 9)
    hornen.show_privileges()

    # Privileges 9-8
    class Privileges():
        def __init__(self):
            self.privileges = ["can see everything", "can delete user", "rules this site"]

        def show_privileges(self):
            for i in self.privileges:
                print("Admin has this privilege: "+i)
    
    class Admin_9_8(User_9_5):
        def __init__(self, first_name, last_name, email, age, login_attempts=0):
            super().__init__(first_name, last_name, email, age, login_attempts)
            self.privileges = Privileges()
    
    hornenAdmin = Admin_9_8("Felix", "Hörnfeldt", "hornen@boss.se", 18, 9)
    hornenAdmin.privileges.show_privileges()

    # Dice 9-14
    from random import randint as ri

    class Die():
        def __init__(self, sides=6):
            self.sides = sides
        
        def roll_die(self):
            r = ri(1, self.sides)
            print(str(r)+": The die has "+str(self.sides)+" sides")

    six_sided = Die(6)
    ten_sided = Die(10)
    twenty_sided = Die(20)
    for i in range(10):
        six_sided.roll_die()
        ten_sided.roll_die()
        twenty_sided.roll_die()

classes()