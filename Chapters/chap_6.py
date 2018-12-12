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
    glossary = {
        'append': 'Adding a item to the end of a list',
        'strip': 'Take away all blank space',
        'print': 'Print out something in the console',
        'for': 'Loop through items',
        'variable': 'Holds elements'
    }
    for k,v in glossary.items():
        print(k.title()+": "+v+"\n")

    # Rivers 6-5
    rivers = {
        'nile': 'egypt',
        'vättern': 'sweden',
        'mississippi': 'america'
    }
    for k,v in rivers.items():
        print("River "+k+" runs through "+v+"\n")
    
    for k in rivers.keys():
        print("River: "+k)

    for v in rivers.values():
        print(v)
    
    # People 6-7
    person_0 = {
        'first_name': 'Felix',
        'last_name': 'Hörnfeldt',
        'age': 18,
        'city': 'Gothenburg'
    }

    person_1 = {
        'first_name': 'Felix',
        'last_name': 'Tornfeldt',
        'age': 19,
        'city': 'Tothenburg'
    }

    person_2 = {
        'first_name': 'Felix',
        'last_name': 'Cornfeldt',
        'age': 12,
        'city': 'Cothenburg'
    }

    persons = [person_0, person_1, person_2]

    for person in persons:
        print(person['first_name']+" "+person['last_name']+" is "+str(person['age'])+" years old and lives in "+person['city'])

    
    # Cities 6-11
    cities = {
        'Gothenburg': {
            'country': 'Sweden',
            'population': 800000,
            'fact': 'Best city in the world, period'
        },

        'Stockholm': {
            'country': 'Sweden',
            'population': 1000001,
            'fact': 'Worst city in the world, period'
        },

        'Copenhagen': {
            'country': 'Denmark',
            'population': 550005,
            'fact': "Don't understand what the hell they are saying"
        }
    }

    for city, city_info in cities.items():
        city_name = "City name: "+city+" \n"
        city_country = "\tCountry: "+city_info['country']+"\n"
        city_population = "\tPopulation: approximatly "+str(city_info['population'])+" people\n"
        city_fact = "\tFact: "+city_info['fact']+"\n"

        print(city_name+city_country+city_population+city_fact)

func_dictionary()