import os
import re
from termcolor import colored
from main_logic import *

# from prompt import *
import time

red = "\033[0;31m"
white_and_red_background = "\033[4;37;41m"

class Menu_Logic: 
    def __init__(self):
        pass

    def menu(self):
        print("Type " + white_and_red_background + " roll  " + color_end + " to continue play")
        print("Type " + white_and_red_background + " rules " + color_end + " to view the brief")
        print("Type " + white_and_red_background + " hand  " + color_end + " to view your leads")
        print("Type " + white_and_red_background + " room  " + color_end + " to be reminded of where you are")
        print("Type " + white_and_red_background + " quit  " + color_end + " to leave John's death a mystery")
        print("  ")
        # response = normalize(input("> "))
    
    def menu_validation(self, user_choice):
        available_choices = ["roll", "rules", "hand", "room", "quit"]
        if user_choice in available_choices:
            return True
        else: 
            return False    
    
        
        
    def rules(self): 
        rules = """
            Solve the murder of John Cokos:
            1. Roll the dice to move from room to room
            
            2. Your practice and final whiteboards will ask for a suspect, a gadget, and a room
                - You must move to a room to complete any whiteboard
                        AND
                - Whiteboards can only reference the room you are standing in
            
            3. Practice your whiteboarding skills
                - You'll start the game with 6 cards to eliminate suspects, gadgets and rooms
                - Use the cards and the front-end website to develop your algorithm
                - Make eliminations by suggesting a suspect, a gadget, and the room you are in
                - The TA will give you a hint if they have one
                - Use the feedback to make corrections to your practice whiteboard
                - You can practice as many times as you want
            
            4. Your final whiteboard
                - For your final whiteboard, move to the room you'd like to solve in
                - Schedule some time with an instructor and present your final solution 
                - The instructor will give you feedback and a passing or failing grade
                - The game ends once you receive your grade
                
            5. You've only got one chance at your final whiteboard, so study hard"""
        # clear screen and re-display menu
        print(colored(rules, "green"))
        time.sleep(5)
        os.system('cls' if os.name == 'nt' else 'clear')
        



