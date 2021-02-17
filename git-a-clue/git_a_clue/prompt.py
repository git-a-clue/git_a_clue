from main_logic import *
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
print("Type (rules) to view the brief")
print("Type (quit) to leave John's death a mystery")
# wait for input and direct with logic
normalize(input("> "))

choose_avatar = f"""
Please choose you avatar from the following list.
Type:
a for {suspects[0]}
b for {suspects[1]}
c for {suspects[2]}
d for {suspects[3]}
e for {suspects[4]}
f for {suspects[5]}

"""
# May need to revisit dict referencing
lib = {
    'a': 0,
    'b': 1,
    'c': 2,
    'd': 3,
    'e': 4,
    'f': 5
}
user1_choice = normalize(input("> "))
avatar1 = suspects[lib[user1_choice]]

start_game_deal_cards(suspects, solution_list)
start_game_deal_cards(gadgets, solution_list)
start_game_deal_cards(rooms, solution_list)

print(f"Alright Detective {avatar1}. Welcome to Git_A_Clue. Let's go solve a murder!")
for i in range(3):
    for j in range(2):
        if i == 1:
            start_game_deal_cards(suspects, player_hand)
        if i == 2:
            start_game_deal_cards(gadgets, player_hand)
        if i == 3:
            start_game_deal_cards(rooms, player_hand)

print("Here are your leads. Use them wisely.")
print(player_hand)

# Roll dice



# Choose room

# Make guess

# Change rooms

# 