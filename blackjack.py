# Blackjack cmd game

import random as rm

card_values = [2,3,4,5,6,7,8,9,10,10,10,10]
player = 0
ai = 0

#########################################

def start_values():
    player = rm.choice(card_values) + rm.choice(card_values)
    ai = rm.choice(card_values)
    return [player,ai]

#########################################

def player_hit(p_value):
    p_value += rm.choice(card_values)
    print("You have: "+str(p_value))
    if p_value > 20:
        print("AI Won!!!")
        return "b"
    else:
        return p_value
    pass

#########################################

def player_stay(ai_value,p_value):
    print("AIs turn")
    while True:
        ai_value += rm.choice(card_values)
        print("AI have: "+str(ai_value))
        if ai_value >= 16 and ai_value <= 20:
            if ai_value > p_value:
                print("AI Won!!!")
                break
            elif ai_value == p_value:
                print("It's a tie!!!")
                break
            else:
                print("You Won!!!")
                break
            pass
        elif ai_value > 20:
            print("You Won!!!")
            break
        else:
            continue
        pass
    
#########################################

def player_ask():
    p_input = input("Would you like to play again? (y/n)\n")
    if p_input == "n":
        exit()
        pass
    elif p_input == "y":
        return "b"
    else:
        exit()
        pass
    pass

#########################################

def game():
    while True:
        p_game = start_values()[0]
        ai_game = start_values()[1]
        
        if p_game == 20:
            print("Blackjack!\nYou Won!!!")
            p_input = input("Would you like to play again? (y/n)\n")
            if p_input == "n":
                exit()
            else:
                continue
            pass
        else:
            print("You have: "+str(p_game))
            while True:
                p_input = input("What is your next move?\nHit(h) or Stay(s)\n")
                if p_input == "h":
                    p_game = player_hit(p_game)
                    if p_game == "b":
                        if player_ask() == "b":
                            break
                        pass
                    pass
                elif p_input == "s":
                    player_stay(ai_game,p_game)
                    if player_ask() == "b":
                        break
                    pass
                else:
                    exit()
                    pass
                pass
            pass
        pass
    pass

game()