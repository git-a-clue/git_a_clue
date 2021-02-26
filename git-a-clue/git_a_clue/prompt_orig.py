from .main_logic import Clue_Logic
from .menu_logic import Menu_Logic
from .ascii_func import print_ascii
from .ascii_func import animate_ascii
# from termcolor import colored
# from playsound import playsound
import time
import os
# display welcome laptop

# display greeting
# prompt to hit enter

# *********** ASCII Variables ************

computer_cf = "git_a_clue/assets_ascii/clue_comp.txt"
floorplan = "git_a_clue/assets_ascii/cf_floorplan.txt"
dice_animation = "git_a_clue/assets_animation/animation"
walk_hall = "git_a_clue/assets_ascii/walk_down_hall.txt"

ascii_murder = "git_a_clue/assets_ascii/murder.txt"

john_outline = "git_a_clue/assets_ascii/john_outline.txt"

#*********** you are here.... *******

you_front_desk = "git_a_clue/assets_ascii/you_are_here_frontd.txt"

#*********** GADGETS ***************
ascii_gadgets = "git_a_clue/assets_ascii/gadgets.txt"

keyboard = "git_a_clue/assets_ascii/keyboard.txt"
laptop = "git_a_clue/assets_ascii/laptop.txt"
whiteboard = "git_a_clue/assets_ascii/killer_whiteboard.txt"
ethernet = "git_a_clue/assets_ascii/ethernet_cord.txt"

#***********color/color-combos***********
white_and_red_background = "\033[4;37;41m"
white_and_green_bkgrnd = "\033[4;30;42m"
blue = "\033[1;34m"
red = "\033[0;31m"
color_end = "\033[0m"
green = "\033[1;32m"
aqua = "\033[1;36m"
#******************************





class Prompt:
    lib = {
        'a': 0,
        'b': 1,
        'c': 2,
        'd': 3,
        'e': 4,
        'f': 5,
        'g': 6,
        'check': None
    }
    accused_person = []
    gadget_accusation = []

    def __init__(self, avatar = "None"):
        self.menu = Menu_Logic()
        self.logic = Clue_Logic()
        self.avatar = avatar
        


    def start_game(self, mock_input = None):
    # display chalk outline
        greeting = """
        There's been a murrrrrrder at Code Fellows! 
        John Cokos needs your help to bring his killer to justice.
        
        """
        
        greeting_pt2 = "Type (play) to investigate, (rules) to view the brief, or (quit) to leave boddy's death a mystery."
        #TODOcenter computer a bit more!!
        print(print_ascii(computer_cf))
        time.sleep(2)
        print(print_ascii(ascii_murder))
        time.sleep(2)
        
        print(greeting)
        user_input = mock_input or input("> ")
        
        response = self.logic.normalize(input("> "))   
            
        print(white_and_red_background + greeting_pt2 + color_end)
        print("  ")
        user_input = mock_input or input("> ")
        response = self.logic.normalize(user_input)          
        def check_input(user_input):
            #Check if input is outside of people choices
            if user_input == "play" or user_input == "p":
                self.pick_a_player()
            #check input against menu prompts
            elif self.menu.menu_validation(user_input) == True:
                if user_input == "roll":
                    print("Before we play, pick an avatar.")
                    print("  ")
                    print(white_and_red_background + greeting_pt2 + color_end)
                    user_next_option = self.logic.normalize(input("> "))
                    check_input(user_next_option) 
                elif user_input == "rules":
                    self.menu.rules()
                    print("  ")
                    print(white_and_red_background + greeting_pt2 + color_end)
                    user_next_option = self.logic.normalize(input("> "))
                    check_input(user_next_option) 
                elif user_input == "hand":
                    print("No hand dealt")
                    print("  ")
                    print(white_and_red_background + greeting_pt2 + color_end)
                    user_next_option = self.logic.normalize(input("> "))
                    check_input(user_next_option) 
                elif user_input == "room":
                    print("Currently at the Front Desk, ready to play.")
                    print("  ")
                    print(white_and_red_background + greeting_pt2 + color_end)
                    user_next_option = self.logic.normalize(input("> "))
                    check_input(user_next_option) 
                elif user_input == "quit":
                    self.leave_boddy_on_read()
            else:
                print("Please enter a valid option.")

                print("Type (play) to investigate, (rules) to view the brief, or (quit) to leave boddy's death a mystery.")
                    
            
                user_next_option = self.logic.normalize(input("> "))
                print("  ")
                print(white_and_red_background + greeting_pt2 + color_end)
                user_next_option = self.logic.normalize(input("> "))
                check_input(user_next_option)
        check_input(response)


    def pick_a_player(self):
        choose_avatar = """
        Please choose you avatar from the following list.
        Type:"""
        print(choose_avatar)
        self.sus_helper()
        response = self.logic.normalize(input("> "))        

        def check_input(user_input):
            #Check if input is outside of people choices
            if user_input == 'g':
                print("Aaron was out of town, pick an avatar from the list")
                print("Type:")
                self.sus_helper()
                user_next_option = self.logic.normalize(input("> "))
                check_input(user_next_option)     
            #check to ensure input is in the available options          
            elif user_input in self.lib.keys():
                self.avatar = self.logic.perma_suspects[self.lib[user_input]]
                #CALL THE NEXT FUNCTION
                self.time_to_deal_and_pick(self.avatar)
            #checks input against menu options
            elif self.menu.menu_validation(user_input) == True:
                if user_input == "roll":
                    print("Before we play, pick an avatar.")
                    print("Type:")
                    self.sus_helper()
                    user_next_option = self.logic.normalize(input("> "))
                    check_input(user_next_option) 
                elif user_input == "rules":
                    self.menu.rules()
                    print("Before we play, pick an avatar.")
                    print("Type:")
                    self.sus_helper()
                    user_next_option = self.logic.normalize(input("> "))
                    check_input(user_next_option) 
                elif user_input == "hand":
                    print("Before we play, pick an avatar.")
                    print("Type:")
                    self.sus_helper()
                    user_next_option = self.logic.normalize(input("> "))
                    check_input(user_next_option)
                elif user_input == "room":
                    print("Currently at the Front Desk, ready to play.")
                    print("Type:")
                    self.sus_helper()
                    user_next_option = self.logic.normalize(input("> "))
                    check_input(user_next_option) 
                else:
                    self.leave_boddy_on_read()
            else:
                #Should we make this line red??
                print("Vince's alibi checked out please choose from below:")
                print("Type:")
                self.sus_helper()
                user_next_option = self.logic.normalize(input("> "))
                check_input(user_next_option)

        check_input(response)

    def time_to_deal_and_pick(self, player_avatar): 
        #deal a solution
        self.logic.solution_deal()
        
        #deal player hand
        self.logic.player_hand_deal()

        #PROMPT ACKNOWLEDGING avatar - MOVING TO NEXT OPTION
        print(colored(f"Alright Detective {player_avatar}. Welcome to Git_A_Clue. Let's go solve a murder!", "green"))
        print(print_ascii(walk_hall))
        # TODO  AMBER // POSSIBLE ASCII PLAYER CARD/S VAGUE

        print(colored("""
        
        Here are your leads. Use them wisely:
        """, "green"))
        hand_holder = self.logic.player_hand
        print(white_and_green_bkgrnd + ', '.join(hand_holder) + color_end)
        time.sleep(2)

        print("""
        What would you like to do next?
        """)
        self.menu.menu()
        response = self.logic.normalize(input("> "))

        #VALIDATES & DIRECTS BASED ON USER CHOICE, RETURNS 'ERROR' IF USER ENTERS ANYTHING OTHER THAN A MENU OPTION
        def check_input(user_input):
            #check input against menu prompts
            if self.menu.menu_validation(user_input) == True:
                if user_input == "roll":
                    #CALL THE NEXT FUNCTION
                    self.roll_and_rooms()
                elif user_input == "rules":
                    self.menu.rules()
                    print("Please choose from menu:")
                    self.menu.menu()
                    user_next_option = self.logic.normalize(input("> "))
                    check_input(user_next_option) 
                elif user_input == "hand":
                    print(white_and_green_bkgrnd + ', '.join(hand_holder) + color_end)
                    print("  ")
                    print("Please choose from menu:")
                    self.menu.menu()
                    user_next_option = self.logic.normalize(input("> "))
                    check_input(user_next_option) 
                elif user_input == "room":
                    print(self.logic.current_room)
                    print("Please choose from menu:")
                    self.menu.menu()
                    user_next_option = self.logic.normalize(input("> "))
                    check_input(user_next_option) 
                else:
                    self.leave_boddy_on_read()
            else:
                #Should we make this line red??
                print("Please choose from available menu choices.")
                print("Please choose from menu:")
                self.menu.menu()
                user_next_option = self.logic.normalize(input("> "))
                check_input(user_next_option) 
        
        check_input(response)

    def roll_and_rooms(self):
        alpha = ['a', 'b', 'c', 'd', 'e','f','g']
        print("Rolling...")
        time.sleep(1)
        rooms, roll = self.logic.eligible_rooms()
        print(f"You've rolled a {roll}")
        print ('Pick a room to move to:')
        murder_rooms = []
        for i in range(len(rooms)):
            room_loop = f'({alpha[i]}) for {rooms[i]}'
            print(room_loop)
            murder_rooms.append(room_loop)
            self.logic.available_rooms_check.append(rooms[i])
        response = self.logic.normalize(input("> "))
        # print("ROOOOOLLLLLLINNNNNNNGGGGGGGG ROOOOOMMMM", murder_rooms)
        # Response = room choice >
        #validate input > 
        #set current room
        #ask user what next

        def check_input(user_input):
            #check to ensure input is a-g
            if user_input in self.lib.keys():
                if len(rooms) < self.lib[user_input] + 1:
                    print("Please choose from available rooms:")  
                    print("Type:")      
                    print(murder_rooms)
                    user_next_option = self.logic.normalize(input("> "))
                    check_input(user_next_option)
                else:
                    room_choice = rooms[self.lib[user_input]]
                
                #Happy path - check to be sure room is AVAILABLE
                    if room_choice in self.logic.available_rooms_check:
                        self.logic.current_room = []
                        self.logic.current_room.append(rooms[self.lib[user_input]])
                        #TODO print out new location (ascii)??
                        print(f"Moving to the {self.logic.current_room[0]}...")
                        time.sleep(1)
                        #CALL THE NEXT FUNCTION
                        self.sus_accusation()
                #else re-prompt
                    else:
                        print("Please choose from available rooms:")  
                        print("Type:")      
                        print(murder_rooms)
                        user_next_option = self.logic.normalize(input("> "))
                        check_input(user_next_option)  
            #checks input against menu options
            elif self.menu.menu_validation(user_input) == True:
                if user_input == "roll":
                    print("Cannot re-roll mid turn.")
                    print("   ")
                    print("Please choose from available rooms:")                 
                    print("Type:")
                    print(murder_rooms)
                    user_next_option = self.logic.normalize(input("> "))
                    check_input(user_next_option) 
                elif user_input == "rules":
                    self.menu.rules()
                    print("   ")
                    print("Please choose from available rooms:")
                    print("Type:")
                    print(murder_rooms)
                    user_next_option = self.logic.normalize(input("> "))
                    check_input(user_next_option) 
                elif user_input == "hand":
                    print(white_and_green_bkgrnd + "This is your hand " + ', '.join(self.logic.player_hand) + color_end)
                    print("  ")
                    print("Please choose from available rooms:")
                    print("Type:")
                    print(murder_rooms)
                    user_next_option = self.logic.normalize(input("> "))
                    check_input(user_next_option) 
                elif user_input == "room":
                    print("You're current in ", str(self.logic.current_room))
                    print("   ")
                    print("Please choose from available rooms:")
                    print("Type:")
                    print(murder_rooms)
                    user_next_option = self.logic.normalize(input("> "))
                    check_input(user_next_option) 
                else:
                    self.leave_boddy_on_read()

            #If all else fails, re-print rooms & call the function recursively
            else:
                #TODOShould we make this line red??
                print("Please choose from available rooms:")  
                print("Type:")      
                print(rooms)
                user_next_option = self.logic.normalize(user_input("> "))
                check_input(user_next_option)    

        check_input(response)



    def sus_accusation(self):
        print("Time to investigate & interrogate...")
        print(f"Now that you're in the {self.logic.current_room[0]}, who do you think committed this heinous crime?!")
        print("Type:")
        self.sus_helper()
        L1 = self.logic.normalize(input("> "))

        def check_input(user_input):
            #Check if input is outside of people choices
            if user_input == 'g':
                print("John thinks your code sucks, please choose from available suspects.")
                print("Type:")
                self.sus_helper()
                user_next_option = self.logic.normalize(input("> "))
                check_input(user_next_option)     
            #check to ensure input is in the available options          
            elif user_input in self.lib.keys():
                self.accused_person = []
                self.accused_person.append(self.logic.perma_suspects[self.lib[user_input]])
                #CALL THE NEXT FUNCTION
                self.gad_accusation(self.accused_person)
            #checks input against menu options
            elif self.menu.menu_validation(user_input) == True:
                if user_input == "roll":
                    print("Cannot re-roll mid turn.")
                    print("  ")
                    print("Please choose from available suspects.")
                    print("Type:")
                    self.sus_helper()
                    user_next_option = self.logic.normalize(input("> "))
                    check_input(user_next_option) 
                elif user_input == "rules":
                    self.menu.rules()
                    print("  ")
                    print("Please choose from available suspects.")
                    print("Type:")
                    self.sus_helper()
                    user_next_option = self.logic.normalize(input("> "))
                    check_input(user_next_option) 
                elif user_input == "hand":
                    print(white_and_green_bkgrnd + "This is your hand " + ', '.join(self.logic.player_hand) + color_end)
                    print("  ")
                    print("Please choose from available suspects.")
                    print("Type:")
                    self.sus_helper()
                    user_next_option = self.logic.normalize(input("> "))
                    check_input(user_next_option) 
                elif user_input == "room":
                    print("You are currently in ", str(self.logic.current_room))
                    print("  ")
                    print("Please choose from available suspects.")
                    print("Type:")
                    self.sus_helper()
                    user_next_option = self.logic.normalize(input("> "))
                    check_input(user_next_option) 
                else:
                    self.leave_boddy_on_read()
            #If all else fails, re-print rooms & call the function recursively
            else:
                #Should we make this line red??
                print("Please choose from available suspects:")
                print("Type:")
                self.sus_helper()
                user_next_option = self.logic.normalize(input("> "))
                check_input(user_next_option)

        check_input(L1)

    def gad_accusation(self, person_accused):
        print(f"And how do you think {person_accused[0]} did it?!")
        print("Type:")
        self.gadget_helper()
        L2 = self.logic.normalize(input("> "))

        def check_input(user_input):
            #Check if input is outside of gadget choices
            if user_input == 'g':
                print("Please choose from available gadgets.")
                print("Type:")
                self.gadget_helper()
                user_next_option = self.logic.normalize(input("> "))
                check_input(user_next_option)     
            #check to ensure input is in the available options          
            elif user_input in self.lib.keys():
                self.gadget_accusation = []
                self.gadget_accusation.append(self.logic.perma_gadgets[self.lib[user_input]])
                #CALL THE NEXT FUNCTION
                hint = self.logic.check_guess(person_accused[0], self.gadget_accusation[0], self.logic.current_room[0])
                self.type_of_guess()

            #checks input against menu options
            elif self.menu.menu_validation(user_input) == True:
                if user_input == "roll":
                    print("Cannot re-roll mid turn.")
                    print("  ")
                    print("Please choose from available gadgets.")
                    print("Type:")
                    self.gadget_helper()
                    user_next_option = self.logic.normalize(input("> "))
                    check_input(user_next_option) 
                elif user_input == "rules":
                    self.menu.rules()
                    print("  ")
                    print("Please choose from available gadgets.")
                    print("Type:")
                    self.gadget_helper()
                    user_next_option = self.logic.normalize(input("> "))
                    check_input(user_next_option) 
                elif user_input == "hand":
                    print(white_and_green_bkgrnd + "This is your hand " + ', '.join(self.logic.player_hand) + color_end)
                    print("  ")
                    print("Please choose from available gadgets.")
                    print("Type:")
                    self.gadget_helper()
                    user_next_option = self.logic.normalize(input("> "))
                    check_input(user_next_option) 
                elif user_input == "room":
                    print("You're currently in ", str(self.logic.current_room))
                    print("  ")
                    print("Please choose from available gadgets.")
                    print("Type:")
                    self.gadget_helper()
                    user_next_option = self.logic.normalize(input("> "))
                    check_input(user_next_option) 
                else:
                    self.leave_boddy_on_read()
            #If all else fails, re-print rooms & call the function recursively
            else:
                #TODOShould we make this line red??
                print("Please choose from available gadgets.")
                print("Type:")
                self.gadget_helper()
                user_next_option = self.logic.normalize(input("> "))
                check_input(user_next_option)

        check_input(L2)


    def type_of_guess(self):
        roll_or_warning = """

        Would you like to (roll) again or make a (final) accusation? 

        **************** WARNING **************** 
        Making a final accusation will end the game
        """
        print(roll_or_warning)
        response = self.logic.normalize(input("> "))

        def check_input(user_input):
            if user_input == 'final': 
                self.final_guess()
            #check input against menu prompts
            elif self.menu.menu_validation(user_input) == True:
                if user_input == "roll":
                    self.roll_and_rooms()
                elif user_input == "rules":
                    self.menu.rules()
                    print(roll_or_warning)
                    user_next_option = self.logic.normalize(input("> "))
                    check_input(user_next_option) 
                elif user_input == "hand":
                    print(white_and_green_bkgrnd + "This is your hand " + ', '.join(self.logic.player_hand) + color_end)
                    print("  ")
                    print(roll_or_warning)
                    user_next_option = self.logic.normalize(input("> "))
                    check_input(user_next_option) 
                elif user_input == "room":
                    print("You're currently in ", str(self.logic.current_room))
                    print(roll_or_warning)
                    user_next_option = self.logic.normalize(input("> "))
                    check_input(user_next_option) 
                else:
                    self.leave_boddy_on_read()
            else:
                #TODO: Should we make this line red??
                print("Please choose either (final) or (roll).")
                user_next_option = self.logic.normalize(input("> "))
                check_input(user_next_option)

        check_input(response)


    def final_guess(self):
        final_accusation = []

        print(f"Alright {self.avatar}, it's time to take the final whiteboard and see if you can avenge boddy & pass the test.")

        print("Who do you think did it?")
        self.sus_helper()
        sus_response = self.logic.normalize(input("> "))

        def person_input(user_input):
            #Check if input is outside of people choices
            if user_input == 'g':
                print("Please choose from available suspects.")
                print("Type:")
                self.sus_helper()
                user_next_option = self.logic.normalize(input("> "))
                person_input(user_next_option)     
            #Happy path         
            elif user_input in self.lib.keys():
                final_accusation.append(self.logic.perma_suspects[self.lib[user_input]])
            #checks input against menu options
            elif self.menu.menu_validation(user_input) == True:
                if user_input == "roll":
                    print("Cannot re-roll mid turn.")
                    print("  ")
                    print("Please choose from available suspects.")
                    print("Type:")
                    self.sus_helper()
                    user_next_option = self.logic.normalize(input("> "))
                    person_input(user_next_option) 
                elif user_input == "rules":
                    self.menu.rules()
                    print("  ")
                    print("Please choose from available suspects.")
                    print("Type:")
                    self.sus_helper()
                    user_next_option = self.logic.normalize(input("> "))
                    person_input(user_next_option) 
                elif user_input == "hand":
                    print(white_and_green_bkgrnd + "This is your hand " + ', '.join(self.logic.player_hand) + color_end)
                    print("  ")
                    print("Please choose from available suspects.")
                    print("Type:")
                    self.sus_helper()
                    user_next_option = self.logic.normalize(input("> "))
                    person_input(user_next_option) 
                elif user_input == "room":
                    print("You're currently in ", str(self.logic.current_room))
                    print("  ")
                    print("Please choose from available suspects.")
                    print("Type:")
                    self.sus_helper()
                    user_next_option = self.logic.normalize(input("> "))
                    person_input(user_next_option) 
                else:
                    self.leave_boddy_on_read()
            #If all else fails, re-print rooms & call the function recursively
            else:
                #TODO: Should we make this line red??
                print("Please choose from available suspects:")
                print("Type:")
                self.sus_helper()
                user_next_option = self.logic.normalize(input("> "))
                person_input(user_next_option)

        person_input(sus_response)

        print("How did they do it?")
        self.gadget_helper()
        gadget_option = self.logic.normalize(input("> "))

        def gadget_input(user_input):
                #Check if input is outside of gadget choices
            if user_input == 'g':
                print("Please choose from available gadgets.")
                print("Type:")
                self.gadget_helper()
                user_next_option = self.logic.normalize(input("> "))
                gadget_input(user_next_option)     
            #Happy path         
            elif user_input in self.lib.keys():
                final_accusation.append(self.logic.perma_gadgets[self.lib[user_input]])

            #checks input against menu options
            elif self.menu.menu_validation(user_input) == True:
                if user_input == "roll":
                    print("Cannot re-roll mid turn.")
                    print("  ")
                    print("Please choose from available gadgets.")
                    print("Type:")
                    self.gadget_helper()
                    user_next_option = self.logic.normalize(input("> "))
                    gadget_input(user_next_option) 
                elif user_input == "rules":
                    self.menu.rules()
                    print("  ")
                    print("Please choose from available gadgets.")
                    print("Type:")
                    self.gadget_helper()
                    user_next_option = self.logic.normalize(input("> "))
                    gadget_input(user_next_option) 
                elif user_input == "hand":
                    print(white_and_green_bkgrnd + "This is your hand " + ', '.join(self.logic.player_hand) + color_end)
                    print("  ")
                    print("Please choose from available rooms.")
                    print("Type:")
                    self.gadget_helper()
                    user_next_option = self.logic.normalize(input("> "))
                    gadget_input(user_next_option) 
                elif user_input == "room":
                    print("You're currently in ", str(self.logic.current_room))
                    print("  ")
                    print("Please choose from available gadgets.")
                    print("Type:")
                    self.gadget_helper()
                    user_next_option = self.logic.normalize(input("> "))
                    gadget_input(user_next_option) 
                else:
                    self.leave_boddy_on_read()
            #If all else fails, re-print rooms & call the function recursively
            else:
                #TODO: Should we make this line red??
                print("Please choose from available gadgets.")
                print("Type:")
                self.gadget_helper()
                user_next_option = self.logic.normalize(input("> "))
                gadget_input(user_next_option)

        gadget_input(gadget_option)

        print("Last thing, where did this happen?")
        self.room_helper()
        place_option = self.logic.normalize(input("> "))

        def room_input(user_input):
            if user_input in self.lib.keys():
                final_accusation.append(self.logic.move_rooms[self.lib[user_input]])
            #checks input against menu options
            elif self.menu.menu_validation(user_input) == True:
                if user_input == "roll":
                    print("Cannot re-roll mid turn.")
                    print("  ")
                    print("Please choose from available rooms.")
                    print("Type:")
                    self.room_helper()
                    user_next_option = self.logic.normalize(input("> "))
                    gadget_input(user_next_option) 
                elif user_input == "rules":
                    self.menu.rules()
                    print("  ")
                    print("Please choose from available rooms.")
                    print("Type:")
                    self.room_helper()
                    user_next_option = self.logic.normalize(input("> "))
                    gadget_input(user_next_option) 
                elif user_input == "hand":
                    print(white_and_green_bkgrnd + "This is your hand " + ', '.join(self.logic.player_hand) + color_end)
                    print("  ")
                    print("Please choose from available rooms.")
                    print("Type:")
                    self.room_helper()
                    user_next_option = self.logic.normalize(input("> "))
                    gadget_input(user_next_option) 
                elif user_input == "room":
                    print("You're currently in ", str(self.logic.current_room))
                    print("  ")
                    print("Please choose from available rooms.")
                    print("Type:")
                    self.room_helper()
                    user_next_option = self.logic.normalize(input("> "))
                    gadget_input(user_next_option) 
                else:
                    self.leave_boddy_on_read()
            #If all else fails, re-print rooms & call the function recursively
            else:
                #TODO: Should we make this line red??
                print("Please choose from available rooms.")
                print("Type:")
                self.room_helper()
                user_next_option = self.logic.normalize(input("> "))
                gadget_input(user_next_option)

        room_input(place_option)

        print("Sending your report to Wadsworth for review.....")

        time.sleep(1)

        if final_accusation == self.logic.solution_list:
            print(f"You did it! You solved boddy's murder!! It was {final_accusation[0]} with the {final_accusation[1]} in the {final_accusation[2]}")
            #TODO: BRING ON THE ASCII

        else:   
            print(f"What did you learn about learning, because you didn't solve this crime! It was {self.logic.solution_list[0]} with the {self.logic.solution_list[1]} in the {self.logic.solution_list[2]}")
            #TODO: BRING ON THE ASCII

        print("What would you like to do next? Type (restart) to kill some more time, (rules) to view the brief, or (quit).")
        response = self.logic.normalize(input("> "))     
        def check_input(user_input):
            #Check if input is outside of people choices
            kill_some_time = "Type (restart) to kill some more time, (rules) to view the brief, or (quit)."
            if user_input == "restart":
                self.logic.reset_tables()
                self.accused_person = []
                self.gadget_accusation = []
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')
                self.start_game()

            elif self.menu.menu_validation(user_input) == True:
                if user_input == "roll":
                    self.logic.reset_tables()
                    self.accused_person = []
                    self.gadget_accusation = []
                    time.sleep(2)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    self.start_game()
                elif user_input == "rules":
                    self.menu.rules()
                    print(kill_some_time)
                    user_next_option = self.logic.normalize(input("> "))
                    check_input(user_next_option) 
                elif user_input == "hand":
                    print("Cannot access hand after final accusation")
                    print(kill_some_time)
                    user_next_option = self.logic.normalize(input("> "))
                    check_input(user_next_option) 
                elif user_input == "room":
                    print("Reset to the Front Desk, ready to play.")
                    print(kill_some_time)
                    user_next_option = self.logic.normalize(input("> "))
                    check_input(user_next_option) 
                else:
                    self.leave_boddy_on_read()
            else:
                #Should we make this line red??
                print(kill_some_time)
                user_next_option = self.logic.normalize(input("> "))
                check_input(user_next_option)

        check_input(response)



        #XXX Ask for s. g. r
        #XXXcheck against solution
        #xxx return true or false
        #xxx if true - you've avenged boddy'
        #xxxif false - you failed and your code sucks.

        #xxx reveal the solution with ascii?
        #xxxplay again 
        #XXX reset & start game
        #XXX quit
        #XXX leave on read
        # roll = play again
        # hand =show hand
        # room




    def leave_boddy_on_read(self):
        self.logic.reset_tables()
        self.accused_person = []
        self.gadget_accusation = []
        print("boddy hates a quitter - now his ghost will forever haunt your CSS.")
        #TODO:  ASCIIprint outline or a dead computer??
        # time.sleep(3)
        # os.system('cls' if os.name == 'nt' else 'clear')

    def sus_helper(self):
        print(f""" 
        (a) for {self.logic.perma_suspects[0]} 
        (b) for {self.logic.perma_suspects[1]}
        (c) for {self.logic.perma_suspects[2]}
        (d) for {self.logic.perma_suspects[3]}
        (e) for {self.logic.perma_suspects[4]}
        (f) for {self.logic.perma_suspects[5]}""")
        
        

    def gadget_helper(self):
        print(f"""
        (a) for {self.logic.perma_gadgets[0]} 
        (b) for {self.logic.perma_gadgets[1]}
        (c) for {self.logic.perma_gadgets[2]}
        (d) for {self.logic.perma_gadgets[3]}
        (e) for {self.logic.perma_gadgets[4]}
        (f) for {self.logic.perma_gadgets[5]}

        """)

    def room_helper(self):
        print(f"""
        (a) for {self.logic.move_rooms[0]} 
        (b) for {self.logic.move_rooms[1]}
        (c) for {self.logic.move_rooms[2]}
        (d) for {self.logic.move_rooms[3]}
        (e) for {self.logic.move_rooms[4]}
        (f) for {self.logic.move_rooms[5]}
        (g) for {self.logic.move_rooms[6]}""")


if __name__ == "__main__":
    new_clue = Prompt()
    new_clue.start_game()