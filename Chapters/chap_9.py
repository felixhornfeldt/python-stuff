def classes():
    # Restaurant 9-1
    class Restaurant():
        def __init__(self, restaurant_name, cuisine_type):
            self.name = restaurant_name
            self.ctype = cuisine_type
        
        def describe_restaurant(self):
            print(self.name + "\n" + self.ctype + "\n")
        
        def open_restaurant(self):
            print(self.name + " is now open!")
    
    restaurant_0 = Restaurant('Indi Resturant', 'indian')

    # Three Restaurants 9-2
    restaurant_1 = Restaurant('Test Res', 'Test')
    restaurant_2 = Restaurant('Thai Chi', 'Thai')

    restaurants = [restaurant_0, restaurant_1, restaurant_2]

    for x in restaurants:
        x.describe_restaurant()
    
    # Users 9-3
    class User():
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

    user_0 = User("Felix", "Hörnfeldt", "felix.hornfeldt@outlook.com", 18)
    user_1 = User("Test", "Testesson", "test.testesson@outlook.com", 18)
    user_2 = User("Yrodl", "Jfjsk", "yrodl.jfjsk@company.com", 18)

    users = [user_0, user_1, user_2]

    for x in users:
        x.describe_user()
        x.great_user()

    ###########################
    class Car():
        def __init__(self, brand, model, year, rating):
            self.brand = brand
            self.model = model
            self.year = year
            self.rating = rating
        
        # Given Information
        def g_info(self):
            print("This is the information given:\n\t" + self.brand + "\n\t" + self.model + "\n\t" + str(self.year) + "\n\t" +str(self.rating) + "\n")
    

    Car("Volvo", "V40", 2018, 7.5).g_info()
    ###########################

classes()