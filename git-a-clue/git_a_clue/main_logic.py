import time
from playsound import playsound
import random
# time adds suspense...

# Welcome message

# Start option
# Rules in logistics.py

# pick avatar

# deal solution
## call the card classes and remove 6 with random index of one of each (0-6)

# deal player cards
## call the card classes and remove 6 with random index of two of each s/w/r
## remaining is computer hints

suspects = ['s1', 's2', 's3', 's4', 's5', 's6']
gadgets = ['g1', 'g2', 'g3', 'g4', 'g5', 'g6']
rooms = ['r1', 'r2', 'r3', 'r4', 'r5', 'r6', 'r7']
move_rooms = ['r1', 'r2', 'r3', 'r4', 'r5', 'r6', 'r7']
solution_list = [] # call start_game_deal_cards on each list_from 
player_hand = [] # call start_game_deal_cards 2x each list_from

# courtyard: just prompt

def start_game_deal_cards(list_from, list_to):
    """ Called for solution and pass s/w/r as list_from with list_to = solution; 
    Called as player hand and pass 2x s/w/r as list-from with list_to = player_hand """
    random_number = random_helper(0, len(list_from) - 1)
    card = list_from[random_number]
    list_to.append(card)
    list_from.remove(card)

def random_helper(start, stop):
    random_number = random.randint(start, stop)
    return random_number


def check_guess(L1, L2, L3):
    """ randomize order of comparing lists; remember to pass in (suspect, gadget, room) """
    check = random_helper(1,3)
    
    if check == 1:
        if L1 in suspects:
            print(f"Not this time we have {L1}")
            # display menu for next option
            
        elif L2 in gadgets:
            print(f"Not this time we have {L2}")
            # display menu for next option
            
        elif L3 in rooms:
            print(f"Not this time we have {L3}")
            # display menu for next option

        else:
            print("Sorry no help here!")

    if check == 2:
        if L2 in gadgets:
            print(f"Not this time we have {L2}")
            # display menu for next option
            
        elif L3 in rooms:
            print(f"Not this time we have {L3}")
            # display menu for next option
            
        elif L1 in suspects:
            print(f"Not this time we have {L1}")
            # display menu for next option
            
        else:
            print("Sorry no help here!")

    if check == 3:
        if L3 in rooms:
            print(f"Not this time we have {L3}")
            # display menu for next option
            
        elif L1 in suspects:
            print(f"Not this time we have {L1}")
            # display menu for next option
            
        elif L2 in gadgets:
            print(f"Not this time we have {L2}")
            # display menu for next option
            
        else:
            print("Sorry no help here!")



# def menu():
#     print("Type (rules) to view the brief")
#     print("Type (hand) to view your leads")
#     print("Type (quit) to leave John's death a mystery")
#     # response = normalize(input("> "))
#     # return response

def normalize(string):
    return string.lower()

# Some stuffffffff

# Play sounds

# def play(file):
#     playsound((file))

# Do you want to quit?

# end of game = reset all lists 

