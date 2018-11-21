def func_dictionary():
    # Prac
    dic = {'color': 'GREEN', 'points': '8'}
    print(dic['color'])

    # Person 6-1
    person = {
        'first_name': 'Felix',
        'last_name': 'Hörnfeldt',
        'age': 18,
        'city': 'Gothenburg'
    }
    print(person['first_name']+"\n"+person['last_name']+"\n"+str(person['age'])+"\n"+person['city'])

    # Favorite Numbers 6-2
    favo_num = {
        'Kim': 'Blue',
        'Ki': 'Green',
        'Åsa': 'Yellow',
        'Aldrige': 'Violet',
        'Black': 'Black'
    }
    print(favo_num['Kim']+"\n"+favo_num['Ki']+"\n"+favo_num['Åsa']+"\n"+favo_num['Aldrige']+"\n"+favo_num['Black'])

    # Glossary 6-3
    glossary = {
        'append': 'Adding a item to the end of a list',
        'strip': 'Take away all blank space',
        'print': 'Print out something in the console'
    }
    print("Append: "+glossary['append']+"\n"+
        "Strip: "+glossary['strip']+"\n"+
        "Print: "+glossary['print']+"\n")

    # Glossary 2 6-4
    

func_dictionary()