import os
from main_logic import *
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
            menu()
            
        # return response
    
    
        
        
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
                - 
            5. You've only got one chance at your final whiteboard, so study hard
        """
        # clear screen and re-display menu
        print(rules)
        time.sleep(5)
        os.system('cls' if os.name == 'nt' else 'clear')



# testing function calls 


# rules()
