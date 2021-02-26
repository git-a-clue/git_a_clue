from main_logic import Clue_Logic
from menu_logic import Menu_Logic
from ascii_func import print_ascii
from ascii_func import animate_ascii
from termcolor import colored
from playsound import playsound
import time
import os
import re
# display welcome laptop

# display greeting
# prompt to hit enter

# *********** ASCII Variables ************

computer_cf = "assets_ascii/clue_comp.txt"
floorplan = "assets_ascii/cf_floorplan.txt"
dice_animation = "assets_animation/animation"
walk_hall = "assets_ascii/walk_down_hall.txt"
hand_o_cards = "assets_ascii/hand_o_cards.txt"
ascii_murder = "assets_ascii/murder.txt"

swear_jar = "assets_ascii/swear_jar.txt"

john_outline = "assets_ascii/john_outline.txt"
scary_john = "assets_ascii/scary_john.txt"
#*********** you are here.... *******

you_front_desk = "assets_ascii/you_are_here_frontd.txt"

#*********** GADGETS ***************
ascii_gadgets = "assets_ascii/gadgets_word.txt"

whiteboard = "assets_ascii/gadget_0.txt"
apple_pen = "assets_ascii/gadget_1.txt"
keyboard = "assets_ascii/gadget_2.txt"
laptop = "assets_ascii/gadget_3.txt"
ethernet = "assets_ascii/gadget_4.txt"
donut = "assets_ascii/gadget_5.txt"

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
    
        greeting = """
        There's been a murrrrrrder at Code Fellows! 
        John Cokos needs your help to bring his killer to justice.

        
        """
        

        greeting_pt2 = " Type (PLAY) to investigate, (RULES) to view the brief, or (QUIT) to leave John's death a mystery. "
        
        print(print_ascii(computer_cf))
        time.sleep(2)
        print(print_ascii(ascii_murder))

        playsound("assets/sounds/dun-dun-dun.wav")
        print(colored(greeting, "green"))    

        print(white_and_red_background + greeting_pt2 + color_end)
        print("  ")
        user_input = mock_input or input("> ")
        response = self.logic.normalize(user_input)
        
        # user_input = mock_input or input("> ")
        # response = self.logic.normalize(input("> "))   
        
        
        """VALIDATES & DIRECTS BASED ON USER CHOICE, RETURNS 'ERROR' IF USER ENTERS ANYTHING OTHER THAN A MENU OPTION"""
        def check_input(user_input):
            #Check if input is outside of people choices
            if user_input == "play" or user_input == "p":
                
                self.pick_a_player()
            #check input against menu prompts
            elif self.menu.menu_validation(user_input) == True:
                if user_input == "roll":
                    print(red + "Before we play, pick an avatar." + color_end)
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
                    print(red + "No hand dealt" + color_end)
                    print("  ")
                    print(white_and_red_background + greeting_pt2 + color_end)
                    user_next_option = self.logic.normalize(input("> "))
                    check_input(user_next_option) 
                elif user_input == "room":
                    print(red + "Currently at the Front Desk, ready to play." + color_end)
                    print("  ")
                    print(white_and_red_background + greeting_pt2 + color_end)
                    user_next_option = self.logic.normalize(input("> "))
                    check_input(user_next_option) 
                elif user_input == "quit":
                    self.leave_boddy_on_read()
            elif user_input == "cheat":
                self.cheat_helper()
                print("Type (play) to investigate, (rules) to view the brief, or (quit) to leave John's death a mystery.")
                print("  ")
                print(white_and_red_background + greeting_pt2 + color_end)
                user_next_option = self.logic.normalize(input("> "))
                check_input(user_next_option)           
            else:
                print(red + "Please enter a valid option." + color_end)

                print("Type (play) to investigate, (rules) to view the brief, or (quit) to leave John's death a mystery.")
                print("  ")
                print(white_and_red_background + greeting_pt2 + color_end)
                user_next_option = self.logic.normalize(input("> "))
                check_input(user_next_option)
        check_input(response)


    def pick_a_player(self):
        choose_avatar = """
        Please choose you avatar from the following list."""
        print(colored(choose_avatar, "green"))
        print("        Type:")
        self.sus_helper()
        response = self.logic.normalize(input("> "))        

        
        
        """VALIDATES & DIRECTS BASED ON USER CHOICE, RETURNS 'ERROR' IF USER ENTERS ANYTHING OTHER THAN A MENU OPTION"""
        def check_input(user_input):
            #Check if input is outside of people choices
            if user_input == 'g':
                print(red + "Aaron was out of town, pick an avatar from the list" + color_end)
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
                    print(red + "Before we play, pick an avatar." + color_end)
                    print("Type:")
                    self.sus_helper()
                    user_next_option = self.logic.normalize(input("> "))
                    check_input(user_next_option) 
                elif user_input == "rules":
                    self.menu.rules()
                    print(red + "Before we play, pick an avatar." + color_end)
                    print("Type:")
                    self.sus_helper()
                    user_next_option = self.logic.normalize(input("> "))
                    check_input(user_next_option) 
                elif user_input == "hand":
                    print(red + "Before we play, pick an avatar." + color_end)
                    print("Type:")
                    self.sus_helper()
                    user_next_option = self.logic.normalize(input("> "))
                    check_input(user_next_option)
                elif user_input == "room":
                    print(red + "Currently at the Front Desk, ready to play." + color_end)
                    print("Type:")
                    self.sus_helper()
                    user_next_option = self.logic.normalize(input("> "))
                    check_input(user_next_option) 
                else:
                    self.leave_boddy_on_read()
            elif user_input == "cheat":
                self.cheat_helper()
                print(red + "Vince's alibi checked out please choose from below:" + color_end)
                print("Type:")
                self.sus_helper()
                user_next_option = self.logic.normalize(input("> "))
                check_input(user_next_option)   
            else:
                
                print(red + "Vince's alibi checked out please choose from below:" + color_end)
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
        playsound('assets/sounds/door.mp3')
        
        
        #TODO make link blue 
        print(colored("""
        
        Here are your leads. Use the whiteboard to eliminate your suspects with this link:

        https://zealous-northcutt-ef89fd.netlify.app/scorecard.html 
        
        Use them wisely:
        """, "green"))
        hand_holder = self.logic.player_hand
        print(print_ascii(hand_o_cards))
        print(white_and_green_bkgrnd + ', '.join(hand_holder) + color_end)
        playsound('assets/sounds/card-deal.wav')


        print(colored("""
        What would you like to do next?
        """, "green"))
        self.menu.menu()
        response = self.logic.normalize(input("> "))
        
        
        """VALIDATES & DIRECTS BASED ON USER CHOICE, RETURNS 'ERROR' IF USER ENTERS ANYTHING OTHER THAN A MENU OPTION"""
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
                    print(print_ascii(hand_o_cards))
                    print(white_and_green_bkgrnd + ', '.join(hand_holder) + color_end)
                    print("  ")
                    print("Please choose from menu:")
                    self.menu.menu()
                    user_next_option = self.logic.normalize(input("> "))
                    check_input(user_next_option) 
                elif user_input == "room":
                    print(green + f"You're currently in {(self.logic.current_room[0])}" + color_end)
                    print("Please choose from menu:")
                    self.menu.menu()
                    user_next_option = self.logic.normalize(input("> "))
                    check_input(user_next_option) 
                else:
                    self.leave_boddy_on_read()
            elif user_input == "cheat":
                self.cheat_helper()
                print(red + "Please choose from available menu choices." + color_end)
                self.menu.menu()
                user_next_option = self.logic.normalize(input("> "))
                check_input(user_next_option) 
            else:
                
                print(red + "Please choose from available menu choices." + color_end)
                self.menu.menu()
                user_next_option = self.logic.normalize(input("> "))
                check_input(user_next_option) 
        
        check_input(response)

    def pick_a_room_helper(self, available_rooms):
        alpha = [white_and_red_background + ' A ' + color_end, white_and_red_background + ' B ' + color_end, white_and_red_background + ' C ' + color_end, white_and_red_background + ' D ' + color_end, white_and_red_background + ' E ' + color_end, white_and_red_background + ' F ' + color_end, white_and_red_background + ' G ' + color_end]
        self.logic.available_rooms_check = []
        for i in range(len(available_rooms)):
            room_loop = f'{alpha[i]} for {available_rooms[i]}'
            print(room_loop)
            self.logic.available_rooms_check.append(available_rooms[i])

    def print_map_helper(self):
        temp_room = self.logic.current_room[0]
        counter = 0
        for i in self.logic.move_rooms:
            if temp_room == i:
                map = f"assets_ascii/youare_{counter}.txt"
                print(print_ascii(map))
                break
            counter += 1    

    def cheat_helper(self):
        if self.logic.solution_list == []:
            print(white_and_green_bkgrnd + "You've CI cn't help you right now " + color_end)
            print("  ")
        else: 
            print(white_and_green_bkgrnd + "You've called your CI - they said the solution is " + ' , '.join(self.logic.solution_list) + color_end)
            print("  ")

    def roll_and_rooms(self):
        alpha = [white_and_red_background + ' A ' + color_end, white_and_red_background + ' B ' + color_end, white_and_red_background + ' C ' + color_end, white_and_red_background + ' D ' + color_end, white_and_red_background + ' E ' + color_end, white_and_red_background + ' F ' + color_end, white_and_red_background + ' G ' + color_end]
        print("  ")
        print(colored("Rolling...", "green"))
        rooms, roll = self.logic.eligible_rooms()
        print(green + f"You've rolled a {roll}" + color_end)
        playsound("assets/sounds/dice-roll.wav")
        print("  ")
        print(colored('Pick a room to move to:', "green"))
        self.pick_a_room_helper(rooms)
        print("  ")
        response = self.logic.normalize(input("> "))


        
        
        """VALIDATES & DIRECTS BASED ON USER CHOICE, RETURNS 'ERROR' IF USER ENTERS ANYTHING OTHER THAN A MENU OPTION"""
        def check_input(user_input):
            #check to ensure input is a-g
            if user_input in self.lib.keys():
                if len(rooms) < self.lib[user_input] + 1:
                    print(colored("Please choose from available rooms:", "green"))  
                    print("Type:")      
                    self.pick_a_room_helper(rooms)
                    user_next_option = self.logic.normalize(input("> "))
                    check_input(user_next_option)
                else:
                    room_choice = rooms[self.lib[user_input]]
                
                #Happy path - check to be sure room is AVAILABLE
                    if room_choice in self.logic.available_rooms_check:
                        self.logic.current_room = []
                        self.logic.current_room.append(rooms[self.lib[user_input]])
                        
                        print(green + f"Moving to {self.logic.current_room[0]}..." + color_end)

                        self.print_map_helper()
                        #CALL THE NEXT FUNCTION
                        playsound('assets/sounds/magic_appear.mp3')
                        self.sus_accusation()
                #else re-prompt
                    else:
                        print(colored("Please choose from available rooms:", "green"))  
                        print("Type:")      
                        self.pick_a_room_helper(rooms)
                        user_next_option = self.logic.normalize(input("> "))
                        check_input(user_next_option)  
            #checks input against menu options
            elif self.menu.menu_validation(user_input) == True:
                if user_input == "roll":
                    print(colored("Cannot re-roll mid turn.", "red"))
                    print("   ")
                    print(colored("Please choose from available rooms:", "green"))                 
                    print("Type:")
                    self.pick_a_room_helper(rooms)
                    user_next_option = self.logic.normalize(input("> "))
                    check_input(user_next_option) 
                elif user_input == "rules":
                    self.menu.rules()
                    print("   ")
                    print(colored("Please choose from available rooms:", "green"))
                    print("Type:")
                    self.pick_a_room_helper(rooms)
                    user_next_option = self.logic.normalize(input("> "))
                    check_input(user_next_option) 
                elif user_input == "hand":
                    print(print_ascii(hand_o_cards))
                    print(white_and_green_bkgrnd + "This is your hand: " + ', '.join(self.logic.player_hand) + color_end)
                    print("  ")
                    print(colored("Please choose from available rooms:", "green"))
                    print("Type:")
                    self.pick_a_room_helper(rooms)
                    user_next_option = self.logic.normalize(input("> "))
                    check_input(user_next_option) 
                elif user_input == "room":
                    #TODO current "you are here" ascii
                    
                    print(green + f"You're currently in {(self.logic.current_room[0])}" + color_end)
                    print("   ") 
                    self.print_map_helper()
                    print(colored("Please choose from available rooms:", "green"))
                    print("Type:")
                    self.pick_a_room_helper(rooms)
                    user_next_option = self.logic.normalize(input("> "))
                    check_input(user_next_option) 
                else:
                    self.leave_boddy_on_read()
            else:
                print(colored("Invalid input!", "green"))
                print("")
                print(colored("Please choose from available rooms:", "green"))  

                print("Type:")
                self.pick_a_room_helper(rooms)
                user_next_option = self.logic.normalize(input("> "))
                check_input(user_next_option) 


        check_input(response)



    def sus_accusation(self):
        print(green + "Time to investigate & interrogate..." + color_end)
        print(colored(f"Now that you're in {self.logic.current_room[0]}, who do you think committed this heinous crime?!", "green"))
        print("Type:")
        self.sus_helper()
        L1 = self.logic.normalize(input("> "))

        
        
        """VALIDATES & DIRECTS BASED ON USER CHOICE, RETURNS 'ERROR' IF USER ENTERS ANYTHING OTHER THAN A MENU OPTION"""
        def check_input(user_input):
            #Check if input is outside of people choices
            if user_input == 'g':
                print(colored("John thinks your code sucks, please choose from available suspects.", "green"))
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
                    print(red + "Cannot re-roll mid turn." + color_end)
                    print("  ")
                    print(colored("Please choose from available suspects.", "green"))
                    print("Type:")
                    self.sus_helper()
                    user_next_option = self.logic.normalize(input("> "))
                    check_input(user_next_option) 
                elif user_input == "rules":
                    self.menu.rules()
                    print("  ")
                    print(colored("Please choose from available suspects.", "green"))
                    print("Type:")
                    self.sus_helper()
                    user_next_option = self.logic.normalize(input("> "))
                    check_input(user_next_option) 
                elif user_input == "hand":
                    print(print_ascii(hand_o_cards))
                    print(white_and_green_bkgrnd + "This is your hand: " + ', '.join(self.logic.player_hand) + color_end)
                    print("  ")
                    print(colored("Please choose from available suspects.", "green"))
                    print("Type:")
                    self.sus_helper()
                    user_next_option = self.logic.normalize(input("> "))
                    check_input(user_next_option) 
                elif user_input == "room":
                    print(green + f"You're currently in {(self.logic.current_room[0])}" + color_end)
                    print("  ")
                    self.print_map_helper()
                    print(colored("Please choose from available suspects.", "green"))
                    print("Type:")
                    self.sus_helper()
                    user_next_option = self.logic.normalize(input("> "))
                    check_input(user_next_option) 
                else:
                    self.leave_boddy_on_read()
            elif user_input == "cheat":
                self.cheat_helper()
                print(colored("Please choose from available suspects.", "green"))
                print("Type:")
                self.sus_helper()
                user_next_option = self.logic.normalize(input("> "))
                check_input(user_next_option)                   
            #If all else fails, re-print rooms & call the function recursively
            else:
                #Should we make this line red??
                print(colored("Please choose from available suspects.", "green"))
                print("Type:")
                self.sus_helper()
                user_next_option = self.logic.normalize(input("> "))
                check_input(user_next_option)

        check_input(L1)

    def gad_accusation(self, person_accused):
        playsound("assets/sounds/grunt.wav")
        print(colored(f"And how do you think {person_accused[0]} did it?!", "green"))
        print("Type:")
        self.gadget_helper()
        L2 = self.logic.normalize(input("> "))

        
        
        """VALIDATES & DIRECTS BASED ON USER CHOICE, RETURNS 'ERROR' IF USER ENTERS ANYTHING OTHER THAN A MENU OPTION"""
        def check_input(user_input):
            #Check if input is outside of gadget choices
            if user_input == 'g':
                print(colored("Please choose from available gadgets.", "green"))
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
                # print("TEST CHEAT", self.logic.solution_list)
                playsound('assets/sounds/punch.wav')
                self.type_of_guess()

            #checks input against menu options
            elif self.menu.menu_validation(user_input) == True:
                if user_input == "roll":
                    print(red + "Cannot re-roll mid turn." + color_end)
                    print("  ")
                    print(colored("Please choose from available gadgets.", "green"))
                    print("Type:")
                    self.gadget_helper()
                    user_next_option = self.logic.normalize(input("> "))
                    check_input(user_next_option) 
                elif user_input == "rules":
                    self.menu.rules()
                    print("  ")
                    print(colored("Please choose from available gadgets.", "green"))
                    print("Type:")
                    self.gadget_helper()
                    user_next_option = self.logic.normalize(input("> "))
                    check_input(user_next_option) 
                elif user_input == "hand":
                    print(print_ascii(hand_o_cards))
                    print(white_and_green_bkgrnd + "This is your hand: " + ', '.join(self.logic.player_hand) + color_end)
                    print("  ")
                    print(colored("Please choose from available gadgets.", "green"))
                    print("Type:")
                    self.gadget_helper()
                    user_next_option = self.logic.normalize(input("> "))
                    check_input(user_next_option) 
                elif user_input == "room":
                    print(green + f"You're currently in {(self.logic.current_room[0])}" + color_end)
                    print("  ")
                    self.print_map_helper()
                    print(colored("Please choose from available gadgets.", "green"))
                    print("Type:")
                    self.gadget_helper()
                    user_next_option = self.logic.normalize(input("> "))
                    check_input(user_next_option) 
                else:
                    self.leave_boddy_on_read()
            elif user_input == "cheat":
                self.cheat_helper()
                print(colored("Please choose from available gadgets.", "green"))
                print("Type:")
                self.gadget_helper()
                user_next_option = self.logic.normalize(input("> "))
                check_input(user_next_option)           
            #If all else fails, re-print rooms & call the function recursively
            else:
                print(colored("Please choose from available gadgets.", "green"))
                print("Type:")
                self.gadget_helper()
                user_next_option = self.logic.normalize(input("> "))
                check_input(user_next_option)

        check_input(L2)

    
    def type_of_guess(self):
        roll_or_warning = """

        Would you like to (ROLL) again or make a (FINAL) accusation? 

        **************** WARNING **************** 
        Making a final accusation will end the game
        """
        print(colored(roll_or_warning, "red"))
        response = self.logic.normalize(input("> "))

        
        
        """VALIDATES & DIRECTS BASED ON USER CHOICE, RETURNS 'ERROR' IF USER ENTERS ANYTHING OTHER THAN A MENU OPTION"""
        def check_input(user_input):
            if user_input == 'final': 
                self.final_guess()
            #check input against menu prompts
            elif self.menu.menu_validation(user_input) == True:
                if user_input == "roll":
                    self.roll_and_rooms()
                elif user_input == "rules":
                    self.menu.rules()
                    print(colored(roll_or_warning, "red"))
                    user_next_option = self.logic.normalize(input("> "))
                    check_input(user_next_option) 
                elif user_input == "hand":
                    print(print_ascii(hand_o_cards))
                    print(white_and_green_bkgrnd + "This is your hand: " + ', '.join(self.logic.player_hand) + color_end)
                    print("  ")
                    print(colored(roll_or_warning, "red"))
                    user_next_option = self.logic.normalize(input("> "))
                    check_input(user_next_option) 
                elif user_input == "room":
                    print(green + f"You're currently in {(self.logic.current_room[0])}" + color_end)
                    print("  ")
                    self.print_map_helper()
                    print(colored(roll_or_warning, "red"))
                    user_next_option = self.logic.normalize(input("> "))
                    check_input(user_next_option) 
                else:
                    self.leave_boddy_on_read()
            elif user_input == "cheat":
                self.cheat_helper()
                print(red + "Please choose either (final) or (roll)." + color_end)
                user_next_option = self.logic.normalize(input("> "))
                check_input(user_next_option)
            else:
                print(red + "Please choose either (final) or (roll)." + color_end)
                user_next_option = self.logic.normalize(input("> "))
                check_input(user_next_option)

        check_input(response)


    def final_guess(self):
        final_accusation = []
        print("  ")
        print(colored(f" Alright {self.avatar}, it's time to take the final whiteboard and see if you can avenge John & pass the test. ", "green"))
        print(print_ascii(john_outline))
        print(green + "Who do you think did it?" + color_end)
        self.sus_helper()
        sus_response = self.logic.normalize(input("> "))

        def person_input(user_input):
            #Check if input is outside of people choices
            if user_input == 'g':
                print(colored("Please choose from available suspects.", "green"))
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
                    print(red + "Cannot re-roll mid turn." + color_end)
                    print("  ")
                    print(colored("Please choose from available suspects.", "green"))
                    print("Type:")
                    self.sus_helper()
                    user_next_option = self.logic.normalize(input("> "))
                    person_input(user_next_option) 
                elif user_input == "rules":
                    self.menu.rules()
                    print("  ")
                    print(colored("Please choose from available suspects.", "green"))
                    print("Type:")
                    self.sus_helper()
                    user_next_option = self.logic.normalize(input("> "))
                    person_input(user_next_option) 
                elif user_input == "hand":
                    print(print_ascii(hand_o_cards))
                    print(white_and_green_bkgrnd + "This is your hand: " + ', '.join(self.logic.player_hand) + color_end)
                    print("  ")
                    print(colored("Please choose from available suspects.", "green"))
                    print("Type:")
                    self.sus_helper()
                    user_next_option = self.logic.normalize(input("> "))
                    person_input(user_next_option) 
                elif user_input == "room":
                    print(green + f"You're currently in {(self.logic.current_room[0])}" + color_end)
                    print("  ")
                    temp_room = self.logic.current_room[0]
                    counter = 0
                    for i in self.logic.move_rooms:
                        if temp_room == i:
                            map = f"assets_ascii/youare_{counter}.txt"
                            print(print_ascii(map))
                        counter += 1
                    print(colored("Please choose from available suspects.", "green"))
                    print("Type:")
                    self.sus_helper()
                    user_next_option = self.logic.normalize(input("> "))
                    person_input(user_next_option) 
                else:
                    self.leave_boddy_on_read()
            elif user_input == "cheat":
                self.cheat_helper()
                print(colored("Please choose from available suspects.", "green"))
                print("Type:")
                self.sus_helper()
                user_next_option = self.logic.normalize(input("> "))
                person_input(user_next_option)       
            #If all else fails, re-print rooms & call the function recursively
            else:
                print(colored("Please choose from available suspects.", "green"))
                print("Type:")
                self.sus_helper()
                user_next_option = self.logic.normalize(input("> "))
                person_input(user_next_option)

        person_input(sus_response)

        print(green + "How did they do it?" + color_end)
        self.gadget_helper()
        gadget_option = self.logic.normalize(input("> "))

        def gadget_input(user_input):
                #Check if input is outside of gadget choices
            if user_input == 'g':
                print(colored("Please choose from available gadgets.", "green"))
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
                    print(red + "Cannot re-roll mid turn." + color_end)
                    print("  ")
                    print(colored("Please choose from available gadgets.", "green"))
                    print("Type:")
                    self.gadget_helper()
                    user_next_option = self.logic.normalize(input("> "))
                    gadget_input(user_next_option) 
                elif user_input == "rules":
                    self.menu.rules()
                    print("  ")
                    print(colored("Please choose from available gadgets.", "green"))
                    print("Type:")
                    self.gadget_helper()
                    user_next_option = self.logic.normalize(input("> "))
                    gadget_input(user_next_option) 
                elif user_input == "hand":
                    print(print_ascii(hand_o_cards))
                    print(white_and_green_bkgrnd + "This is your hand: " + ', '.join(self.logic.player_hand) + color_end)
                    print("  ")
                    print(colored("Please choose from available gadgets.", "green"))
                    print("Type:")
                    self.gadget_helper()
                    user_next_option = self.logic.normalize(input("> "))
                    gadget_input(user_next_option) 
                elif user_input == "room":
                    print(green + f"You're currently in {(self.logic.current_room[0])}" + color_end)
                    print("  ")
                    self.print_map_helper()
                    print(colored("Please choose from available gadgets.", "green"))
                    print("Type:")
                    self.gadget_helper()
                    user_next_option = self.logic.normalize(input("> "))
                    gadget_input(user_next_option) 
                else:
                    self.leave_boddy_on_read()
            elif user_input == "cheat":
                self.cheat_helper()
                print(colored("Please choose from available gadgets.", "green"))
                print("Type:")
                self.gadget_helper()
                user_next_option = self.logic.normalize(input("> "))
                gadget_input(user_next_option)
            #If all else fails, re-print rooms & call the function recursively
            else:
                
                print(colored("Please choose from available gadgets.", "green"))
                print("Type:")
                self.gadget_helper()
                user_next_option = self.logic.normalize(input("> "))
                gadget_input(user_next_option)

        gadget_input(gadget_option)

        print(green + "Last thing, where did this happen?" + color_end)
        self.room_helper()
        place_option = self.logic.normalize(input("> "))

        def room_input(user_input):
            if user_input in self.lib.keys():
                final_accusation.append(self.logic.move_rooms[self.lib[user_input]])
            #checks input against menu options
            elif self.menu.menu_validation(user_input) == True:
                if user_input == "roll":
                    print(red + "Cannot re-roll mid turn." + color_end)
                    print("  ")
                    print(colored("Please choose from available rooms.", "green"))
                    print("Type:")
                    self.room_helper()
                    user_next_option = self.logic.normalize(input("> "))
                    gadget_input(user_next_option) 
                elif user_input == "rules":
                    self.menu.rules()
                    print("  ")
                    print(colored("Please choose from available rooms.", "green"))
                    print("Type:")
                    self.room_helper()
                    user_next_option = self.logic.normalize(input("> "))
                    gadget_input(user_next_option) 
                elif user_input == "hand":
                    print(print_ascii(hand_o_cards))
                    print(white_and_green_bkgrnd + "This is your hand: " + ', '.join(self.logic.player_hand) + color_end)
                    print("  ")
                    print(colored("Please choose from available rooms.", "green"))
                    print("Type:")
                    self.room_helper()
                    user_next_option = self.logic.normalize(input("> "))
                    gadget_input(user_next_option) 
                elif user_input == "room":
                    print(green + f"You're currently in {(self.logic.current_room[0])}" + color_end)
                    print("  ")
                    self.print_map_helper()
                    print(colored("Please choose from available rooms.", "green"))
                    print("Type:")
                    self.room_helper()
                    user_next_option = self.logic.normalize(input("> "))
                    gadget_input(user_next_option) 
                else:
                    self.leave_boddy_on_read()
            elif user_input == "cheat":
                self.cheat_helper()
                print(colored("Please choose from available rooms.", "green"))
                print("Type:")
                self.room_helper()
                user_next_option = self.logic.normalize(input("> "))
                gadget_input(user_next_option)
            #If all else fails, re-print rooms & call the function recursively
            else:
                print(colored("Please choose from available rooms.", "green"))
                print("Type:")
                self.room_helper()
                user_next_option = self.logic.normalize(input("> "))
                gadget_input(user_next_option)

        room_input(place_option)

        print(green + "Sending your report to Brook for review....." + color_end)
        print(" ")

        time.sleep(1.5)

        if final_accusation == self.logic.solution_list:
            print(colored(f"You did it! You solved John's murder!! It was {final_accusation[0]}, {final_accusation[1]} in the {final_accusation[2]}", "green"))
            #TODO: BRING ON THE ASCII
            temp_gadget = final_accusation[1]
            counter = 0
            for i in self.logic.perma_gadgets:
                if temp_gadget == i:
                    map = f"assets_ascii/gadget_{counter}.txt"
                    print(print_ascii(map))
                counter += 1
            
            playsound('assets/sounds/guitar.wav')
            print(" ")    


        else:   
            print(colored(f"What did you learn about learning, because you didn't solve this crime! It was {self.logic.solution_list[0]}, {self.logic.solution_list[1]} in the {self.logic.solution_list[2]}", "green"))
    
            #TODO: BRING ON THE ASCII
            temp_gadget = self.logic.solution_list[1]
            counter = 0
            for i in self.logic.perma_gadgets:
                if temp_gadget == i:
                    map = f"assets_ascii/gadget_{counter}.txt"
                    print(print_ascii(map))
                counter += 1
            playsound('assets/sounds/boo.wav')
            print(" ")    


        print(white_and_red_background + "What would you like to do next? Type (restart) to kill some more time, (rules) to view the brief, or (quit)." + color_end)
        response = self.logic.normalize(input("> "))     
        
        
        """VALIDATES & DIRECTS BASED ON USER CHOICE, RETURNS 'ERROR' IF USER ENTERS ANYTHING OTHER THAN A MENU OPTION"""
        def check_input(user_input):
            #Check if input is outside of people choices
            kill_some_time = "Type (restart) to kill some more time, (rules) to view the brief, or (quit)."
            if user_input == "restart":
                self.logic.reset_tables()
                self.accused_person = []
                self.gadget_accusation = []
                print('First, John has to add to the swear jar')
                print(print_ascii(swear_jar))
                playsound('assets/sounds/coin.wav')
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
                    print(green + "Reset to the Front Desk, ready to play." + color_end)
                    print(white_and_red_background + kill_some_time + color_end)
                    user_next_option = self.logic.normalize(input("> "))
                    check_input(user_next_option) 
                else:
                    self.leave_boddy_on_read()
            elif user_input == "cheat":
                self.cheat_helper()
                print(kill_some_time)
                user_next_option = self.logic.normalize(input("> "))
                check_input(user_next_option)        
            else:
                #Should we make this line red??
                print(kill_some_time)
                user_next_option = self.logic.normalize(input("> "))
                check_input(user_next_option)

        check_input(response)




    def leave_boddy_on_read(self):
        self.logic.reset_tables()
        self.accused_person = []
        self.gadget_accusation = []
        print(green + "John hates a quitter - his ghost will haunt your CSS, FOREVER." + color_end)
        print(print_ascii(scary_john))
        playsound('assets/sounds/game-over.wav')


    
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




if __name__ == "__main__":
    new_clue = Prompt()
    new_clue.start_game()