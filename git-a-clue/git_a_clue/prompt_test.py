

# from git_a_clue.main_logic import Clue_Logic
# from git_a_clue.menu_logic import Menu_Logic
# from git_a_clue.ascii_func import print_ascii
# from git_a_clue.ascii_func import animate_ascii
# import sys
# from termcolor import colored

from .main_logic_test import Clue_Logic
from .menu_logic_test import Menu_Logic
from .ascii_func import print_ascii
from .ascii_func import animate_ascii



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
hand_o_cards = "git_a_clue/assets_ascii/hand_o_cards.txt"
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
donut = "git_a_clue/assets_ascii/donut.txt"
apple_pen = "git_a_clue/assets_ascii/apple_pen.txt"
#***********color/color-combos***********
white_and_red_background = "\033[4;37;41m"
white_and_green_bkgrnd = "\033[4;30;42m"
blue = "\033[1;34m"
red = "\033[1;31m"
color_end = "\033[0m"
green = "\033[1;32m"
aqua = "\033[1;36m"
purple = "\033[1;35m"

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
        
        greeting_pt2 = " Type (PLAY) to investigate, (RULES) to view the brief, or (QUIT) to leave John's death a mystery. "
        #TODOcenter computer a bit more!!
        print(print_ascii(computer_cf))
        time.sleep(2)
        print(print_ascii(ascii_murder))
        time.sleep(2)
        
        print(greeting)
        # user_input = mock_input or input("> ")
        
        if mock_input != None:
            response = mock_input
        else: 
            response = self.logic.normalize(input("> "))   
            
        print(white_and_red_background + greeting_pt2 + color_end)
        print("  ")
        # user_input = mock_input or input("> ")
        # response = self.logic.normalize(user_input)          
        def check_input(user_input):
            #Check if input is outside of people choices
            if user_input == "play" or user_input == "p":
                if mock_input == 'play':
                    self.pick_a_player(mock_input)
                else: 
                    self.pick_a_player()
            #check input against menu prompts
            elif self.menu.menu_validation(user_input) == True:
                if user_input == "roll":
                    print(red + "Before we play, pick an avatar." + color_end)
                    print("  ")
                    print(white_and_red_background + greeting_pt2 + color_end)
                    if mock_input == 'roll':
                        user_next_option = 'quit'
                    else: 
                        user_next_option = self.logic.normalize(input("> "))

                    # user_next_option = self.logic.normalize(input("> "))
                    check_input(user_next_option) 
                elif user_input == "rules":
                    self.menu.rules()
                    print("  ")
                    print(white_and_red_background + greeting_pt2 + color_end)
                    if mock_input == 'rules':
                        user_next_option = 'quit'
                    else: 
                        user_next_option = self.logic.normalize(input("> "))

                    # user_next_option = self.logic.normalize(input("> "))
                    check_input(user_next_option) 
                elif user_input == "hand":
                    print(red + "No hand dealt" + color_end)
                    print("  ")
                    print(white_and_red_background + greeting_pt2 + color_end)
                    if mock_input == 'hand':
                        user_next_option = 'quit'
                    else: 
                        user_next_option = self.logic.normalize(input("> "))


                    # user_next_option = self.logic.normalize(input("> "))
                    check_input(user_next_option) 
                elif user_input == "room":
                    print(red + "Currently at the Front Desk, ready to play." + color_end)
                    print("  ")
                    print(white_and_red_background + greeting_pt2 + color_end)
                    if mock_input == 'room':
                        user_next_option = 'quit'
                    else: 
                        user_next_option = self.logic.normalize(input("> "))

                    # user_next_option = self.logic.normalize(input("> "))
                    check_input(user_next_option) 
                elif user_input == "quit":
                    self.leave_boddy_on_read()
            else:
                print(red + "Please enter a valid option." + color_end)

                print("Type (play) to investigate, (rules) to view the brief, or (quit) to leave John's death a mystery.")
                    
                if mock_input != None:
                    response = mock_input
                    user_next_option = 'quit'
                else: 
                    response = self.logic.normalize(input("> "))   
                    user_next_option = self.logic.normalize(input("> "))

                print("  ")
                print(white_and_red_background + greeting_pt2 + color_end)
                # user_next_option = self.logic.normalize(input("> "))
                check_input(user_next_option)
        check_input(response)


    def pick_a_player(self, mock_input = None):
        choose_avatar = """
        Please choose you avatar from the following list.
        Type:"""
        print(choose_avatar)
        self.sus_helper()
        if mock_input != None:
            response = mock_input
        else: 
            response = self.logic.normalize(input("> "))   

        # response = self.logic.normalize(input("> "))        

        def check_input(user_input):
            #Check if input is outside of people choices
            if user_input == 'g':
                print(red + "Aaron was out of town, pick an avatar from the list" + color_end)
                print("Type:")
                self.sus_helper()
                if mock_input == 'g':
                    user_next_option = 'quit'
                else: 
                    user_next_option = self.logic.normalize(input("> "))   

                # user_next_option = self.logic.normalize(input("> "))
                check_input(user_next_option)     
            #check to ensure input is in the available options          
            elif user_input in self.lib.keys():
                self.avatar = self.logic.perma_suspects[self.lib[user_input]]
                #CALL THE NEXT FUNCTION
                self.time_to_deal_and_pick(self.avatar)
            #checks input against menu options
            elif self.menu.menu_validation(user_input) == True:
                if user_input == "roll":
                    print(red + "Before we play, pick an avatar." + color_end)
                    print("Type:")
                    self.sus_helper()
                    if mock_input == 'roll':
                        user_next_option = 'quit'
                    else: 
                        user_next_option = self.logic.normalize(input("> "))   

                    # user_next_option = self.logic.normalize(input("> "))
                    check_input(user_next_option) 
                elif user_input == "rules":
                    self.menu.rules()
                    print(red + "Before we play, pick an avatar." + color_end)
                    print("Type:")
                    self.sus_helper()
                    if mock_input == 'rules':
                        user_next_option = 'quit'
                    else: 
                        user_next_option = self.logic.normalize(input("> "))


                    # user_next_option = self.logic.normalize(input("> "))
                    check_input(user_next_option) 
                elif user_input == "hand":
                    print(red + "Before we play, pick an avatar." + color_end)
                    print("Type:")
                    self.sus_helper()
                    if mock_input == 'hand':
                        user_next_option = 'quit'
                    else: 
                        user_next_option = self.logic.normalize(input("> "))

                    # user_next_option = self.logic.normalize(input("> "))
                    check_input(user_next_option)
                elif user_input == "room":
                    print(red + "Currently at the Front Desk, ready to play." + color_end)
                    print("Type:")
                    self.sus_helper()
                    if mock_input == 'room':
                        user_next_option = 'quit'
                    else: 
                        user_next_option = self.logic.normalize(input("> "))
                    
                    # user_next_option = self.logic.normalize(input("> "))
                    check_input(user_next_option) 
                else:
                    self.leave_boddy_on_read()
            else:
                #Should we make this line red??
                print(red + "Vince's alibi checked out please choose from below:" + color_end)
                print("Type:")
                self.sus_helper()
                if mock_input != None:
                    response = mock_input
                    user_next_option = 'quit'
                else: 
                    response = self.logic.normalize(input("> ")) 
                    user_next_option = self.logic.normalize(input("> "))
                check_input(user_next_option)

        check_input(response)

    def time_to_deal_and_pick(self, player_avatar, mock_input = None): 
        #deal a solution
        # self.logic.solution_deal()
        
        #deal player hand
        # self.logic.player_hand_deal()

        #PROMPT ACKNOWLEDGING avatar - MOVING TO NEXT OPTION
        print(f"Alright Detective {player_avatar}. Welcome to Git_A_Clue. Let's go solve a murder!", "green")
        print(print_ascii(walk_hall))
        # TODO  AMBER // POSSIBLE ASCII PLAYER CARD/S VAGUE
        
        #TODO make link blue 
        print("""
        
        Here are your leads. Use the whiteboard to eliminate your suspects with this link:

        https://zealous-northcutt-ef89fd.netlify.app/scorecard.html 
        
        Use them wisely:
        """, "green")
        hand_holder = self.logic.player_hand
        print(print_ascii(hand_o_cards))
        print(white_and_green_bkgrnd + ', '.join(hand_holder) + color_end)
        time.sleep(2)

        print("""
        What would you like to do next?
        """)
        self.menu.menu()
        if mock_input != None:
            response = mock_input
        else: 
            response = self.logic.normalize(input("> "))   

        # response = self.logic.normalize(input("> "))

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
                    if mock_input == 'rules':
                        user_next_option = 'quit'
                    else: 
                        user_next_option = self.logic.normalize(input("> "))

                    # user_next_option = self.logic.normalize(input("> "))
                    check_input(user_next_option) 
                elif user_input == "hand":
                    print(print_ascii(hand_o_cards))
                    print(white_and_green_bkgrnd + ', '.join(hand_holder) + color_end)
                    print("  ")
                    print("Please choose from menu:")
                    self.menu.menu()
                    if mock_input == 'hand':
                        user_next_option = 'quit'
                    else: 
                        user_next_option = self.logic.normalize(input("> "))

                    # user_next_option = self.logic.normalize(input("> "))
                    check_input(user_next_option) 
                elif user_input == "room":
                    print(self.logic.current_room)
                    print("Please choose from menu:")
                    self.menu.menu()
                    if mock_input == 'room':
                        user_next_option = 'quit'
                    else: 
                        user_next_option = self.logic.normalize(input("> "))

                    # user_next_option = self.logic.normalize(input("> "))
                    check_input(user_next_option) 
                elif user_input == 'quit':
                    self.leave_boddy_on_read()
            else:
                #Should we make this line red??
                print(red + "Please choose from available menu choices." + color_end)
                print("Please choose from menu:")
                self.menu.menu()
                if mock_input != None:
                    user_next_option = 'quit'
                    response = mock_input
                else: 
                    user_next_option = self.logic.normalize(input("> "))

                # user_next_option = self.logic.normalize(input("> "))
                check_input(user_next_option) 
        
        check_input(response)
    #XXX make letters a color
    #TODO when ask for room, remind where you are with you are here map
    
    def roll_and_rooms(self, mock_input = None):
        alpha = [white_and_red_background + ' A ' + color_end, white_and_red_background + ' B ' + color_end, white_and_red_background + ' C ' + color_end, white_and_red_background + ' D ' + color_end, white_and_red_background + ' E ' + color_end, white_and_red_background + ' F ' + color_end, white_and_red_background + ' G ' + color_end]
        print("Rolling...")
        time.sleep(1)
        rooms, roll = self.logic.eligible_rooms()
        print(f"You've rolled a {roll}")
        print ('Pick a room to move to:')
        murder_rooms = []
        for i in range(len(rooms)):
            room_loop = f'{alpha[i]} for {rooms[i]}'
            print(room_loop)
            murder_rooms.append(room_loop)
            self.logic.available_rooms_check.append(rooms[i])
        # response = self.logic.normalize(input("> "))
        
        if mock_input != None:
            response = mock_input
        else: 
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
                    if mock_input == 'a':
                        user_next_option = 'quit'
                    else:
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
                        temp_room = self.logic.current_room[0]
                        counter = 0
                        for i in rooms:
                            if temp_room == i:
                                map = f"git_a_clue/assets_ascii/youare_{counter}.txt"
                                print(print_ascii(map))
                            counter += 1    
                        time.sleep(1)
                        #CALL THE NEXT FUNCTION
                        if mock_input == 'a':
                            user_next_option = 'quit'
                        else:

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
                    if mock_input == 'roll':
                        user_next_option = 'quit'
                    else:


                        user_next_option = self.logic.normalize(input("> "))
                    check_input(user_next_option) 
                elif user_input == "rules":
                    self.menu.rules()
                    print("   ")
                    print("Please choose from available rooms:")
                    print("Type:")
                    print(murder_rooms)
                    if mock_input == 'rules':
                        user_next_option = 'quit'
                    else:

                        user_next_option = self.logic.normalize(input("> "))
                    check_input(user_next_option) 
                elif user_input == "hand":
                    print(print_ascii(hand_o_cards))
                    print(white_and_green_bkgrnd + "This is your hand " + ', '.join(self.logic.player_hand) + color_end)
                    print("  ")
                    print("Please choose from available rooms:")
                    print("Type:")
                    print(murder_rooms)
                    if mock_input == 'hand':
                        user_next_option = 'quit'
                    else:

                        user_next_option = self.logic.normalize(input("> "))
                    check_input(user_next_option) 
                elif user_input == "room":
                    #TODO current "you are here" ascii
                    #print(print_ascii(you_front_desk))
                    print("You're currently in ", str(self.logic.current_room))
                    print("   ")
                    print("Please choose from available rooms:")
                    print("Type:")
                    print(murder_rooms)
                    print(murder_rooms)
                    if mock_input == 'room':
                        user_next_option = 'quit'
                    else:


                        user_next_option = self.logic.normalize(input("> "))
                    check_input(user_next_option) 
                elif user_input == 'quit':
                    self.leave_boddy_on_read()

            #If all else fails, re-print rooms & call the function recursively
            else:
                #TODOShould we make this line red??
                print("Please choose from available rooms:")  
                print("Type:")      
                print(rooms)
                if mock_input != None:
                    user_next_option = 'quit'
                else: 
                    user_next_option = self.logic.normalize(input("> "))
                
                # user_next_option = self.logic.normalize(user_input("> "))
                check_input(user_next_option)    

        check_input(response)



    def sus_accusation(self, mock_input = None):
        print("Time to investigate & interrogate...")
        print(f"Now that you're in the {self.logic.current_room[0]}, who do you think committed this heinous crime?!")
        print("Type:")
        self.sus_helper()
        if mock_input != None:
            L1 = mock_input
        else: 
            L1 = self.logic.normalize(input("> "))   

        # L1 = self.logic.normalize(input("> "))

        def check_input(user_input):
            #Check if input is outside of people choices
            if user_input == 'g':
                print("John thinks your code sucks, please choose from available suspects.")
                print("Type:")
                self.sus_helper()
                if mock_input == 'g':
                    user_next_option = 'quit'
                else:
                    user_next_option = self.logic.normalize(input("> "))
 
                # user_next_option = self.logic.normalize(input("> "))
                check_input(user_next_option)     
            #check to ensure input is in the available options          
            elif user_input in self.lib.keys():
                self.accused_person = []
                self.accused_person.append(self.logic.perma_suspects[self.lib[user_input]])
                #CALL THE NEXT FUNCTION
                if mock_input == 'a':
                    user_next_option = 'quit'
                else:

                    self.gad_accusation(self.accused_person)
            #checks input against menu options
            elif self.menu.menu_validation(user_input) == True:
                if user_input == "roll":
                    print("Cannot re-roll mid turn.")
                    print("  ")
                    print("Please choose from available suspects.")
                    print("Type:")
                    self.sus_helper()
                    if mock_input == 'roll':
                        user_next_option = 'quit'
                    else:


                        user_next_option = self.logic.normalize(input("> "))
                    check_input(user_next_option) 
                elif user_input == "rules":
                    self.menu.rules()
                    print("  ")
                    print("Please choose from available suspects.")
                    print("Type:")
                    self.sus_helper()
                    if mock_input == 'rules':
                        user_next_option = 'quit'
                    else:

                    
                        user_next_option = self.logic.normalize(input("> "))
                    check_input(user_next_option) 
                elif user_input == "hand":
                    print(print_ascii(hand_o_cards))
                    print(white_and_green_bkgrnd + "This is your hand " + ', '.join(self.logic.player_hand) + color_end)
                    print("  ")
                    print("Please choose from available suspects.")
                    print("Type:")
                    self.sus_helper()
                    if mock_input == 'hand':
                        user_next_option = 'quit'
                    else:

                        user_next_option = self.logic.normalize(input("> "))
                    check_input(user_next_option) 
                elif user_input == "room":
                    print("You are currently in ", str(self.logic.current_room))
                    print("  ")
                    print("Please choose from available suspects.")
                    print("Type:")
                    self.sus_helper()
                    if mock_input == 'room':
                        user_next_option = 'quit'
                    else:

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
                if mock_input != None:
                    L1 = mock_input
                    user_next_option = 'quit'
                else: 
                    L1 = self.logic.normalize(input("> ")) 
                    user_next_option = self.logic.normalize(input("> "))

                
                # user_next_option = self.logic.normalize(input("> "))
                check_input(user_next_option)

        check_input(L1)

    def gad_accusation(self, person_accused, mock_input = None):
        print(f"And how do you think {person_accused[0]} did it?!")
        print("Type:")
        self.gadget_helper()
        if mock_input != None:
            L2 = mock_input
        else: 
            L2 = self.logic.normalize(input("> "))   

        # L2 = self.logic.normalize(input("> "))

        def check_input(user_input):
            #Check if input is outside of gadget choices
            if user_input == 'g':
                print("Please choose from available gadgets.")
                print("Type:")
                self.gadget_helper()
                if mock_input == 'g':
                    user_next_option = 'quit'
                else:

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
                    if mock_input == 'roll':
                        user_next_option = 'quit'
                    else:

                        user_next_option = self.logic.normalize(input("> "))
                    check_input(user_next_option) 
                elif user_input == "rules":
                    self.menu.rules()
                    print("  ")
                    print("Please choose from available gadgets.")
                    print("Type:")
                    self.gadget_helper()
                    if mock_input == 'rules':
                        user_next_option = 'quit'
                    else:

                        user_next_option = self.logic.normalize(input("> "))
                    check_input(user_next_option) 
                elif user_input == "hand":
                    print(print_ascii(hand_o_cards))
                    print(white_and_green_bkgrnd + "This is your hand " + ', '.join(self.logic.player_hand) + color_end)
                    print("  ")
                    print("Please choose from available gadgets.")
                    print("Type:")
                    self.gadget_helper()
                    if mock_input == 'hand':
                        user_next_option = 'quit'
                    else:

                        user_next_option = self.logic.normalize(input("> "))
                    check_input(user_next_option) 
                elif user_input == "room":
                    print("You're currently in ", str(self.logic.current_room))
                    print("  ")
                    print("Please choose from available gadgets.")
                    print("Type:")
                    self.gadget_helper()
                    if mock_input == 'room':
                        user_next_option = 'quit'
                    else:

                        user_next_option = self.logic.normalize(input("> "))
                    check_input(user_next_option) 
                elif user_input == 'quit':
                    self.leave_boddy_on_read()
            #If all else fails, re-print rooms & call the function recursively
            else:
                #TODOShould we make this line red??
                print("Please choose from available gadgets.")
                print("Type:")
                self.gadget_helper()
                if mock_input != None:
                    user_next_option = 'quit'
                else: 
                    user_next_option = self.logic.normalize(input("> "))

                # user_next_option = self.logic.normalize(input("> "))
                check_input(user_next_option)

        check_input(L2)


    def type_of_guess(self, mock_input = None):
        roll_or_warning = """

        Would you like to (ROLL) again or make a (FINAL) accusation? 

        **************** WARNING **************** 
        Making a final accusation will end the game
        """
        print(roll_or_warning)
        if mock_input != None:
            response = mock_input
        else: 
            response = self.logic.normalize(input("> "))   


        # response = self.logic.normalize(input("> "))

        def check_input(user_input):
            if user_input == 'final': 
                if mock_input == 'final':
                    user_next_option = 'quit'
                else:

                    self.final_guess()
            #check input against menu prompts
            elif self.menu.menu_validation(user_input) == True:
                if user_input == "roll":
                    if mock_input == 'roll':
                        user_next_option = 'quit'
                    else:

                        self.roll_and_rooms()
                elif user_input == "rules":
                    self.menu.rules()
                    print(roll_or_warning)
                    if mock_input == 'rules':
                        user_next_option = 'quit'
                    else:

                        user_next_option = self.logic.normalize(input("> "))
                    check_input(user_next_option) 
                elif user_input == "hand":
                    print(print_ascii(hand_o_cards))
                    print(white_and_green_bkgrnd + "This is your hand " + ', '.join(self.logic.player_hand) + color_end)
                    print("  ")
                    print(roll_or_warning)
                    if mock_input == 'hand':
                        user_next_option = 'quit'
                    else:

                        user_next_option = self.logic.normalize(input("> "))
                    check_input(user_next_option) 
                elif user_input == "room":
                    print("You're currently in ", str(self.logic.current_room))
                    print(roll_or_warning)
                    if mock_input == 'room':
                        user_next_option = 'quit'
                    else:

                        user_next_option = self.logic.normalize(input("> "))
                    check_input(user_next_option) 
                else:
                    self.leave_boddy_on_read()
            else:
                #TODO: Should we make this line red??
                print("Please choose either (final) or (roll).")
                if mock_input != None:
                    user_next_option = 'quit'
                else: 
                    user_next_option = self.logic.normalize(input("> "))

                # user_next_option = self.logic.normalize(input("> "))
                check_input(user_next_option)

        check_input(response)


    def final_guess(self, mock_avatar = None, mock_sus = None, mock_gadget = None, mock_place = None):
        final_accusation = []
        if mock_avatar != None:
            self.avatar = mock_avatar
            
        print(f"Alright {self.avatar}, it's time to take the final whiteboard and see if you can avenge John & pass the test.")

        print("Who do you think did it?")
        self.sus_helper()
        if mock_sus != None:
            sus_response = mock_sus
        else: 
            sus_response = self.logic.normalize(input("> "))   

        # sus_response = self.logic.normalize(input("> "))

        def person_input(user_input):
            #Check if input is outside of people choices
            if user_input == 'g':
                print("Please choose from available suspects.")
                print("Type:")
                self.sus_helper()
                
                if mock_sus != None:
                    sus_response = 'g'
                    user_next_option = 'quit'
                else: 
                    user_next_option = self.logic.normalize(input("> "))

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
                    if mock_sus != None:
                        sus_response = 'roll'
                        user_next_option = 'quit'
                    else: 

                        user_next_option = self.logic.normalize(input("> "))
                        person_input(user_next_option) 
                elif user_input == "rules":
                    self.menu.rules()
                    print("  ")
                    print("Please choose from available suspects.")
                    print("Type:")
                    self.sus_helper()
                    if mock_sus != None:
                        sus_response = 'rules'
                        user_next_option = 'quit'
                    else: 

                        user_next_option = self.logic.normalize(input("> "))
                        person_input(user_next_option) 
                elif user_input == "hand":
                    print(print_ascii(hand_o_cards))
                    print(white_and_green_bkgrnd + "This is your hand " + ', '.join(self.logic.player_hand) + color_end)
                    print("  ")
                    print("Please choose from available suspects.")
                    print("Type:")
                    self.sus_helper()
                    if mock_sus != None:
                        sus_response = 'hand'
                        user_next_option = 'quit'
                    else: 

                        user_next_option = self.logic.normalize(input("> "))
                        person_input(user_next_option) 
                elif user_input == "room":
                    print("You're currently in ", str(self.logic.current_room))
                    print("  ")
                    print("Please choose from available suspects.")
                    print("Type:")
                    self.sus_helper()
                    if mock_sus != None:
                        sus_response = 'room'
                        user_next_option = 'quit'
                    else: 

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
                if mock_sus != None:
                    sus_response = 'quit'
                else: 
                    sus_response = self.logic.normalize(input("> "))


        person_input(sus_response)

        print("How did they do it?")
        self.gadget_helper()
        if mock_gadget != None:
            gadget_option = mock_gadget
        else: 
            gadget_option = self.logic.normalize(input("> ")) 

        # gadget_option = self.logic.normalize(input("> "))

        def gadget_input(user_input):
                #Check if input is outside of gadget choices
            if user_input == 'g':
                print("Please choose from available gadgets.")
                print("Type:")
                self.gadget_helper()
                if mock_gadget != None:
                    gadget_option = 'g'
                    user_next_option = 'quit'
                else: 

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
                    if mock_gadget != None:
                        gadget_option = 'roll'
                        user_next_option = 'quit'
                    else: 

                        user_next_option = self.logic.normalize(input("> "))
                        gadget_input(user_next_option) 
                elif user_input == "rules":
                    self.menu.rules()
                    print("  ")
                    print("Please choose from available gadgets.")
                    print("Type:")
                    self.gadget_helper()
                    if mock_gadget != None:
                        gadget_option = 'rules'
                        user_next_option = 'quit'
                    else: 

                        user_next_option = self.logic.normalize(input("> "))
                        gadget_input(user_next_option) 
                elif user_input == "hand":
                    print(print_ascii(hand_o_cards))
                    print(white_and_green_bkgrnd + "This is your hand " + ', '.join(self.logic.player_hand) + color_end)
                    print("  ")
                    print("Please choose from available rooms.")
                    print("Type:")
                    self.gadget_helper()
                    if mock_gadget != None:
                        gadget_option = 'hand'
                        user_next_option = 'quit'
                    else: 

                        user_next_option = self.logic.normalize(input("> "))
                        gadget_input(user_next_option) 
                elif user_input == "room":
                    print("You're currently in ", str(self.logic.current_room))
                    print("  ")
                    print("Please choose from available gadgets.")
                    print("Type:")
                    self.gadget_helper()
                    if mock_gadget != None:
                        gadget_option = 'room'
                        user_next_option = 'quit'
                    else: 

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
                if mock_gadget != None:
                    gadget_option = mock_gadget
                    user_next_option = 'quit'
                else: 
                    gadget_option = self.logic.normalize(input("> ")) 
                    user_next_option = self.logic.normalize(input("> "))

                # user_next_option = self.logic.normalize(input("> "))
                # gadget_input(user_next_option)

        gadget_input(gadget_option)

        print("Last thing, where did this happen?")
        self.room_helper()
        if mock_place != None:
            place_option = mock_place
        else: 
            place_option = self.logic.normalize(input("> "))


        # place_option = self.logic.normalize(input("> "))

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
                    if mock_place != None:
                        place_option = 'roll'
                        user_next_option = 'quit'
                    else: 

                        user_next_option = self.logic.normalize(input("> "))
                        place_option(user_next_option) 
                elif user_input == "rules":
                    self.menu.rules()
                    print("  ")
                    print("Please choose from available rooms.")
                    print("Type:")
                    self.room_helper()
                    if mock_sus != None:
                        place_option = 'rules'
                        user_next_option = 'quit'
                    else: 

                        user_next_option = self.logic.normalize(input("> "))
                        place_option(user_next_option) 
                elif user_input == "hand":
                    print(print_ascii(hand_o_cards))
                    print(white_and_green_bkgrnd + "This is your hand " + ', '.join(self.logic.player_hand) + color_end)
                    print("  ")
                    print("Please choose from available rooms.")
                    print("Type:")
                    self.room_helper()
                    if place_option != None:
                        place_option = 'hand'
                        user_next_option = 'quit'
                    else: 

                        user_next_option = self.logic.normalize(input("> "))
                        place_option(user_next_option) 
                elif user_input == "room":
                    print("You're currently in ", str(self.logic.current_room))
                    print("  ")
                    print("Please choose from available rooms.")
                    print("Type:")
                    self.room_helper()
                    if place_option != None:
                        place_option = 'room'
                        user_next_option = 'quit'
                    else: 

                        user_next_option = self.logic.normalize(input("> "))
                        place_option(user_next_option) 
                else:
                    self.leave_boddy_on_read()
            #If all else fails, re-print rooms & call the function recursively
            else:
                #TODO: Should we make this line red??
                print("Please choose from available rooms.")
                print("Type:")
                self.room_helper()
                if mock_place != None:
                    place_option = mock_place
                    user_next_option = 'quit'
                else: 
                    place_option = self.logic.normalize(input("> ")) 
                    user_next_option = self.logic.normalize(input("> "))


                # user_next_option = self.logic.normalize(input("> "))
                # gadget_input(user_next_option)

        room_input(place_option)

        print("Sending your report to Wadsworth for review.....")

        time.sleep(1)
        #if mock anything is not none
        if mock_place != None:
            final_accusation = [mock_sus,mock_gadget,mock_place]
            user_next_option = 'quit'
            


        # if final_accusation == self.logic.solution_list:
        #     print(f"You did it! You solved John's murder!! It was {final_accusation[0]} with the {final_accusation[1]} in the {final_accusation[2]}")
        #     #TODO: BRING ON THE ASCII

        # else:   
        #     print(f"What did you learn about learning, because you didn't solve this crime! It was {self.logic.solution_list[0]} with the {self.logic.solution_list[1]} in the {self.logic.solution_list[2]}")
        #     #TODO: BRING ON THE ASCII

        # print("What would you like to do next? Type (restart) to kill some more time, (rules) to view the brief, or (quit).")
        # response = self.logic.normalize(input("> "))     
        # def check_input(user_input):
        #     #Check if input is outside of people choices
        #     kill_some_time = "Type (restart) to kill some more time, (rules) to view the brief, or (quit)."
        #     if user_input == "restart":
        #         self.logic.reset_tables()
        #         self.accused_person = []
        #         self.gadget_accusation = []
        #         time.sleep(2)
        #         os.system('cls' if os.name == 'nt' else 'clear')
        #         self.start_game()

        #     elif self.menu.menu_validation(user_input) == True:
        #         if user_input == "roll":
        #             self.logic.reset_tables()
        #             self.accused_person = []
        #             self.gadget_accusation = []
        #             time.sleep(2)
        #             os.system('cls' if os.name == 'nt' else 'clear')
        #             self.start_game()
        #         elif user_input == "rules":
        #             self.menu.rules()
        #             print(kill_some_time)
        #             user_next_option = self.logic.normalize(input("> "))
        #             check_input(user_next_option) 
        #         elif user_input == "hand":
        #             print("Cannot access hand after final accusation")
        #             print(kill_some_time)
        #             user_next_option = self.logic.normalize(input("> "))
        #             check_input(user_next_option) 
        #         elif user_input == "room":
        #             print("Reset to the Front Desk, ready to play.")
        #             print(kill_some_time)
        #             user_next_option = self.logic.normalize(input("> "))
        #             check_input(user_next_option) 
        #         else:
        #             self.leave_boddy_on_read()
        #     else:
        #         #Should we make this line red??
        #         print(kill_some_time)
        #         user_next_option = self.logic.normalize(input("> "))
        #         check_input(user_next_option)

        # check_input(response)




    def leave_boddy_on_read(self):
        self.logic.reset_tables()
        self.accused_person = []
        self.gadget_accusation = []
        print("John hates a quitter - now his ghost will forever haunt your CSS.")
        #TODO:  ASCIIprint outline or a dead computer??
        # time.sleep(3)
        # os.system('cls' if os.name == 'nt' else 'clear')

    #TODOmake color letters
    def sus_helper(self):
        print("        " + white_and_red_background + " A " + color_end + f" for {self.logic.perma_suspects[0]}") 
        print("        " + white_and_red_background + " B " + color_end + f" for {self.logic.perma_suspects[1]}") 
        print("        " + white_and_red_background + " C " + color_end + f" for {self.logic.perma_suspects[2]}") 
        print("        " + white_and_red_background + " D " + color_end + f" for {self.logic.perma_suspects[3]}") 
        print("        " + white_and_red_background + " E " + color_end + f" for {self.logic.perma_suspects[4]}") 
        print("        " + white_and_red_background + " F " + color_end + f" for {self.logic.perma_suspects[5]}") 

        
        

    def gadget_helper(self):
        print("        " + white_and_red_background + " A " + color_end + f" for {self.logic.perma_gadgets[0]}") 
        print("        " + white_and_red_background + " B " + color_end + f" for {self.logic.perma_gadgets[1]}") 
        print("        " + white_and_red_background + " C " + color_end + f" for {self.logic.perma_gadgets[2]}") 
        print("        " + white_and_red_background + " D " + color_end + f" for {self.logic.perma_gadgets[3]}") 
        print("        " + white_and_red_background + " E " + color_end + f" for {self.logic.perma_gadgets[4]}") 
        print("        " + white_and_red_background + " F " + color_end + f" for {self.logic.perma_gadgets[5]}")


    def room_helper(self):
        print("        " + white_and_red_background + " A " + color_end + f" for {self.logic.move_rooms[0]}") 
        print("        " + white_and_red_background + " B " + color_end + f" for {self.logic.move_rooms[1]}") 
        print("        " + white_and_red_background + " C " + color_end + f" for {self.logic.move_rooms[2]}") 
        print("        " + white_and_red_background + " D " + color_end + f" for {self.logic.move_rooms[3]}") 
        print("        " + white_and_red_background + " E " + color_end + f" for {self.logic.move_rooms[4]}") 
        print("        " + white_and_red_background + " F " + color_end + f" for {self.logic.move_rooms[5]}")
        print("        " + white_and_red_background + " G " + color_end + f" for {self.logic.move_rooms[6]}")




# if __name__ == "__main__":
#     new_clue = Prompt()
#     new_clue.start_game()