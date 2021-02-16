import time
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

suspects = [s1,s2, s3, s4, s5, s6]
weapons = [w1, w2,w3, w4, w5, w6]
rooms = [r1, r2, r3, r4, r5, r6, r7]

solution_list = [s,w, r] # call start_game_deal_cards on each list_from 
player_hand = [s1, s2, w1, w2, r1, r2] # call start_game_deal_cards 2x each list_from


# courtyard: just prompt

start_game_deal_cards(list_from, list_to):
    """ Called for solution and pass s/w/r as list_from with list_to = solution; 
    Called as player hand and pass 2x s/w/r as list-from with list_to = player_hand """
    generate a random number length of list_from
    card = find list[random number]
    list_to.append(card)
    list_from.remove(card)
    
check_guess(L1, L2, L3):
    """ randomize order of comparing lists; remember to pass in (suspect, weapon, room) """
    generate random (1,3): number = list to check
    
    if random = 1 check is in list1 = suspects:
        tell player suspect is in list
        if not random = 2
        if not random = 3
    else:
        sorry, no help here
        # make sure you go to other lists if random = 1 but card is not in L1
        
    if random = 2 check is in list2 = weapons:
        tell player suspect is in list
        make sure you go to other lists if random = 2 but card is not in L2
        
    if random = 3 check is in list3 = rooms:
        tell player suspect is in list
        make sure you go to other lists if random = 3 but card is not in L3
    

# Some stuffffffff


# Do you want to quit?

end of game = reset all lists 

