from ascii_func import print_ascii
from ascii_func import animate_ascii
from termcolor import colored
import time
# from playsound import playsound
import random
import re

# *********** ASCII Variables ************
dice_animation = "assets_animation/animation"

#***********color/color-combos***********
white_and_red_background = "\033[4;37;41m"
blue = "\033[1;34m"
red = "\033[0;31m"
color_end = "\033[0m"
green = "\033[1;32m"
aqua = "\033[1;36m"
#******************************

class Clue_Logic: 

    suspects = ['Roger Huba', 'Robin Apparicio', 'Phil Werner', 'Heather Cherewaty', 'Dario Thornhill', 'Teri Pfeffer']
    perma_suspects = ['Roger Huba', 'Robin Apparicio', 'Phil Werner', 'Heather Cherewaty', 'Dario Thornhill', 'Teri Pfeffer']
    gadgets = ['Death by Whiteboard', 'Apple Pencil shiv', 'Bludgeoned by Keyboard', 'Electrocuted by Laptop', 'Strangled by Ethernet', 'Poisoned Donuts']
    perma_gadgets = ['Death by Whiteboard', 'Apple Pencil shiv', 'Bludgeoned by Keyboard', 'Electrocuted by Laptop', 'Strangled by Ethernet', 'Poisoned Donuts']
    rooms = ['Student Kitchen', 'Katherine G. Johnson Ballroom', 'Co-working Hall', 'Lovelace', 'Babbage', 'Hopper', 'Johns Study']
    move_rooms = ['Student Kitchen', 'Katherine G. Johnson Ballroom', 'Co-working Hall', 'Lovelace', 'Babbage', 'Hopper', 'Johns Study']
    solution_list = [] # call start_game_deal_cards on each list_from 
    player_hand = [] # call start_game_deal_cards 2x each list_from
    available_rooms_check = []

    def __init__(self, rounds=0, current_room=['the Front Desk - Roll the dice to explore campus']):
        #moving rounds
        self.rounds = rounds
        self.current_room = current_room

    def normalize(self, string):
        return string.lower()

    def start_game_deal_cards(self, list_from, list_to):
        """ Called for solution and pass s/g/r as list_from with list_to = solution; 
        Called as player hand and pass 2x s/g/r as list-from with list_to = player_hand """
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
                print(colored(f"Not this time we have {L1}", "green"))
                
            elif L2 in self.gadgets:
                print(colored(f"Not this time we have {L2}", "green"))
                
            elif L3 in self.rooms:
                print(colored(f"Not this time we have {L3}", "green"))
            else:
                print(red + "The TA's can't help and are going to take the next ticket in the queue" + color_end)
        if check == 2:
            if L2 in self.gadgets:
                print(colored(f"Not this time we have {L2}", "green"))
                
            elif L3 in self.rooms:
                print(colored(f"Not this time we have {L3}", "green"))
                
            elif L1 in self.suspects:
                print(colored(f"Not this time we have {L1}", "green"))
                
            else:
                print(red + "The TA's can't help and are going to take the next ticket in the queue" + color_end)
        if check == 3:
            if L3 in self.rooms:
                print(colored(f"Not this time we have {L3}", "green"))
                
            elif L1 in self.suspects:
                print(colored(f"Not this time we have {L1}", "green"))
                
            elif L2 in self.gadgets:
                print(colored(f"Not this time we have {L2}", "green"))
                
            else:
                print(red + "The TA's can't help and are going to take the next ticket in the queue" + color_end)


    def roll_dice(self):
        roll = self.random_helper(1,6)
        animate_ascii(dice_animation, 6, 3)
        for k in range(9):
            print("\033[A\033[A")
        path = f"assets_animation/animation_{roll - 1}.txt"
        print(print_ascii(path))
        return roll

    def eligible_rooms(self):
        perma_roll = self.roll_dice()
        roll = perma_roll
        poss_move = []
        index = 0
        #edge case - if roll is 6, can pick from any room
        if roll == 6:
            poss_move = self.move_rooms
            #remove current room from list
            if self.current_room[0] != "the Front Desk - Roll the dice to explore campus":
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
        self.suspects = ['Roger Huba', 'Robin Apparicio', 'Phil Werner', 'Heather Cherewaty', 'Dario Thornhill', 'Teri Pfeffer']
        self.gadgets = ['Death by Whiteboard', 'Apple Pencil shiv', 'Bludgeoned by Keyboard', 'Electrocuted by Laptop', 'Strangled by Ethernet', 'Poisoned Donuts']
        self.rooms = ['Student Kitchen', 'Katherine G. Johnson Ballroom', 'Co-working Hall', 'Lovelace', 'Babbage', 'Hopper', 'Johns Study']
        self.current_room = ["the Front Desk - Roll the dice to explore campus"]

        


