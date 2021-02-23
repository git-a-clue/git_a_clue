import os
import re
# import sys
from git_a_clue.main_logic import *
# from prompt import *
import time

class Menu_Logic: 
    def __init__(self):
        pass

    def menu(self):
        print("Type (roll) to continue play")
        print("Type (rules) to view the brief")
        print("Type (hand) to view your leads")
        print("Type (room) to be reminded of where you are")
        print("Type (quit) to leave John's death a mystery")
        # response = normalize(input("> "))
    
    def menu_validation(self, user_choice):
        available_choices = ["roll", "rules", "hand", "room", "quit"]
        if user_choice in available_choices:
            return True
        else: 
            return False

    #ENTER IN NEXT FUNC TO CONTINUE AFTER MENU CHOICE??
    def menu_helper(self, user_choice, next_function=None): 
        if user_choice == ("roll"):

            self.roll_and_rooms()
            # roll_dice()
            # what to do if they look at rules in flow and not before a roll??
        elif user_choice == ("rules"):
            self.rules()
        elif user_choice == ("hand"):
            print(self.player_hand)
        elif user_choice == ("quit"):
            self.leave_john_on_read()
        elif user_choice == ("room"):
            print(self.current_room)
            pass
        else:
            print ("Please try again")
            self.menu()
            
    
    
        
        
    def rules(self): 
        # # clear screen and re-display menu
        with open('/Users/kim/codefellows/401/git_a_clue/git-a-clue/git_a_clue/assets/rules.txt', 'r') as rules:
            print(rules)
        time.sleep(5)
        os.system('cls' if os.name == 'nt' else 'clear')
        
        







