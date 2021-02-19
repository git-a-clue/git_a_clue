

def menu():
    print("Type (roll) to continue play")
    print("Type (rules) to view the brief")
    print("Type (hand) to view your leads")
    print("Type (quit) to leave John's death a mystery")
    # response = normalize(input("> "))
    
    if response == ("roll"):
        # roll_dice()
        # what to do if they look at rules in flow and not before a roll??
    elif response == ("rules"):
        rules()
    elif response == ("hand")
        print(player_hand)
    if response == ("quit"):
        # end_game()
    else:
        print ("Please try again")
        
    # return response
    
    
    
    
def rules(): 
    # clear screen
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
    menu()
