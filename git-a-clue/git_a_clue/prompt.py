from main_logic import *
from playsound import playsound
# display welcome laptop

# display greeting
# prompt to hit enter

greeting = """
There's been a murrrrrrder at Code Fellows! 
Mr Body needs your help to bring his killer to justice. 


"""
# display chalk outline
print(greeting)
# figure out how to format as a column
# add colors via https://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html
print("Type (start) to investigate")
menu()
# wait for input and direct with logic


choose_avatar = f"""
Please choose you avatar from the following list.
Type:
a for {suspects[0]} #poss_move[0]
b for {suspects[1]}
c for {suspects[2]}
d for {suspects[3]}
e for {suspects[4]}
f for {suspects[5]}

"""
print(choose_avatar)


# May need to revisit dict referencing
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

user1_choice = normalize(input("> "))
user_room_choice = normalize(input("> "))

# if user_room_choice is not in list, print dummmmmmy!

if user1_choice = 6:
    print("Vince has declined to participate")
    
avatar1 = suspects[lib[user1_choice]]

start_game_deal_cards(suspects, solution_list)
start_game_deal_cards(gadgets, solution_list)
start_game_deal_cards(rooms, solution_list)


print(f"Alright Detective {avatar1}. Welcome to Git_A_Clue. Let's go solve a murder!")
for i in range(1,4):
    for j in range(2):
        if i == 1:
            start_game_deal_cards(suspects, player_hand)
        if i == 2:
            start_game_deal_cards(gadgets, player_hand)
        if i == 3:
            start_game_deal_cards(rooms, player_hand)

print("Here are your leads. Use them wisely.")
print(player_hand)

print("What would you like to do next? ")
menu()
user_next_option = normalize(input("> "))


check_guess('s1', 'g2', 'r3')

# play('assets/creeky_door.mp3')


# Roll dice



# Choose room

# Make guess

# Change rooms

# 