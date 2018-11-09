def func_message_2_1():
    # Personal message 2-3
    name = "Aphirapat"
    print("Hello " + name + " you sweet bastard")

    # Name Case 2-4
    name = "Hanson"
    print(name.upper()+"\n"+name.lower()+"\n"+name.title())

    # Famous quote 2-5
    quote = '"I had a dream about chickens"'
    author = "Klebert Yothenhan"
    print(author.title()+" once said, "+quote)

    # Famous quote 2-6
    quote = '"I had a dream about cows"'
    author = "Herbert kirschteiger"
    msg = author.title()+" once said, "+quote
    print(msg)

    # Stripping names 2-7
    name = "          \t   Bich \n\t\n     "
    print(name+"\n"+name.lstrip()+"\n"+name.rstrip()+"\n"+name.strip())

func_message_2_1()

def func_integers_2_2():
    # Number 8 2-8
    print(str(5+3)+"\n"+str(10-2)+"\n"+str(4*2)+"\n"+str(4.0/0.5))

    # Favorite number 2-9
    fav_num = 25
    print(str(fav_num)+" is my favorite number")

func_integers_2_2()