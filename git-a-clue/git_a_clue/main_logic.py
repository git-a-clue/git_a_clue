import time
# from playsound import playsound
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




class Clue_Logic: 

    suspects = ['s1', 's2', 's3', 's4', 's5', 's6']
    perma_suspects = ['s1', 's2', 's3', 's4', 's5', 's6']
    gadgets = ['g1', 'g2', 'g3', 'g4', 'g5', 'g6']
    perma_gadgets = ['g1', 'g2', 'g3', 'g4', 'g5', 'g6']
    rooms = ['r1', 'r2', 'r3', 'r4', 'r5', 'r6', 'r7']
    move_rooms = ['r1', 'r2', 'r3', 'r4', 'r5', 'r6', 'r7']
    solution_list = [] # call start_game_deal_cards on each list_from 
    player_hand = [] # call start_game_deal_cards 2x each list_from
    available_rooms_check = []

    def __init__(self, rounds=0, current_room='Front Desk - Roll the dice to explore campus'):
        #moving rounds
        self.rounds = rounds
        self.current_room = current_room

    def normalize(self, string):
        return string.lower()

    def start_game_deal_cards(self, list_from, list_to):
        """ Called for solution and pass s/w/r as list_from with list_to = solution; 
        Called as player hand and pass 2x s/w/r as list-from with list_to = player_hand """
        random_number = self.random_helper(0, len(list_from) - 1)
        card = list_from[random_number]
        list_to.append(card)
        list_from.remove(card)



    def random_helper(self, start, stop):
        random_number = random.randint(start, stop)
        return random_number

    def solution_deal(self):
        self.start_game_deal_cards(self.suspects, self.solution_list)
        self.start_game_deal_cards(self.gadgets, self.solution_list)
        self.start_game_deal_cards(self.rooms, self.solution_list)
        print("CHEAT", self.solution_list)
    
    def player_hand_deal(self):
        for i in range(1,4):
            for j in range(2):
                if i == 1:
                    self.start_game_deal_cards(self.suspects, self.player_hand)
                if i == 2:
                    self.start_game_deal_cards(self.gadgets, self.player_hand)
                if i == 3:
                    self.start_game_deal_cards(self.rooms, self.player_hand)
    

    def check_guess(self, L1, L2, L3):
        """ randomize order of comparing lists; remember to pass in (suspect, gadget, room) """
        check = self.random_helper(1,3)
        
        if check == 1:
            if L1 in self.suspects:
                print(f"Not this time we have {L1}")
                # display menu for next option
                
            elif L2 in self.gadgets:
                print(f"Not this time we have {L2}")
                # display menu for next option
                
            elif L3 in self.rooms:
                print(f"Not this time we have {L3}")
                # display menu for next option
            else:
                print("Sorry no help here!")
        if check == 2:
            if L2 in self.gadgets:
                print(f"Not this time we have {L2}")
                # display menu for next option
                
            elif L3 in self.rooms:
                print(f"Not this time we have {L3}")
                # display menu for next option
                
            elif L1 in self.suspects:
                print(f"Not this time we have {L1}")
                # display menu for next option
                
            else:
                print("Sorry no help here!")
        if check == 3:
            if L3 in self.rooms:
                print(f"Not this time we have {L3}")
                # display menu for next option
                
            elif L1 in self.suspects:
                print(f"Not this time we have {L1}")
                # display menu for next option
                
            elif L2 in self.gadgets:
                print(f"Not this time we have {L2}")
                # display menu for next option
                
            else:
                print("Sorry no help here!")
        # self.prompt.type_of_guess()


    def roll_dice(self):
        roll = self.random_helper(1,6)
        return roll

    def eligible_rooms(self):
        perma_roll = self.roll_dice()
        roll = perma_roll
        # print("ROLL", roll)
        #store variables
        alpha = ['a', 'b', 'c', 'd', 'e','f','g']
        poss_move = []
        index = 0
        #edge case - if roll is 6, can pick from any room
        if roll == 6:
            poss_move = self.move_rooms
            #remove current room from list
            if self.current_room != "Front Desk - Roll the dice to explore campus":
                poss_move.remove(self.current_room[0])
                available_rooms_check = []
                available_rooms_check.append(poss_move)
                return poss_move, roll      
        #happy path - if roll is 1-5, generate random rooms
        else:
            # generate same number of random indices as the dice roll
            while len(poss_move) < roll:
                rand_idx = self.random_helper(0, len(self.move_rooms)-1)
                if self.move_rooms[rand_idx] == self.current_room[0] or self.move_rooms[rand_idx] in poss_move:
                    continue
                else: 
                    poss_move.append(self.move_rooms[rand_idx])
        available_rooms_check = []
        return poss_move, roll
    
    def reset_tables(self):
        self.solution_list.clear()
        self.player_hand.clear()
        self.available_rooms_check.clear()
        self.suspects = ['s1', 's2', 's3', 's4', 's5', 's6']
        self.gadgets = ['g1', 'g2', 'g3', 'g4', 'g5', 'g6']
        self.rooms = ['r1', 'r2', 'r3', 'r4', 'r5', 'r6', 'r7']
        self.current_room = "Front Desk - Roll the dice to explore campus"

        



# if __name__ == "__main__":
#     test_logic = Clue_Logic()
#     test_logic.eligible_rooms(5)