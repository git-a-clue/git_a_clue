import pytest
from git_a_clue.main_logic import Clue_Logic
from git_a_clue.menu_logic import Menu_Logic
from git_a_clue.prompt import Prompt

# Main_Logic Tests -- 15 passing; 80% on report
# @pytest.mark.skip("pending")
def test_logic():
    actual = Clue_Logic.suspects[0]
    expected = 's1'
    assert actual == expected

# @pytest.mark.skip("pending")
def test_normalize():
    actual = Clue_Logic().normalize('AWS')
    expected = 'aws'
    assert actual == expected

# @pytest.mark.skip("pending")
def test_start_game_deal_cards():
    test_in = ['s1', 's2', 's3']
    test_out = []
    Clue_Logic().start_game_deal_cards(test_in, test_out)
    assert test_out[0]

# @pytest.mark.skip("pending")
def test_random_helper():
    actual = Clue_Logic().random_helper(2,6)
    assert actual >= 2 and actual <= 6

# @pytest.mark.skip("pending")
def test_solution_deal():
    clue = Clue_Logic()
    clue.solution_deal()
    actual = len(clue.solution_list)
    expected = 3
    assert actual == expected

# @pytest.mark.skip("pending")
def test_player_hand_deal():
    clue = Clue_Logic()
    clue.player_hand_deal()
    actual = len(clue.player_hand)
    expected = 6
    assert actual == expected

# @pytest.mark.skip("pending")
def test_check_guess1(capsys):
    actual = Clue_Logic().check_guess('s9', 'g9', 'r9')
    captured = capsys.readouterr()
    assert captured.out == "Sorry no help here!\n"

# @pytest.mark.skip("pending")
def test_check_guess2(capsys):
    clue = Clue_Logic()
    clue.suspects = ['s1']
    clue.check_guess('s1', 's1', 's1')
    captured = capsys.readouterr()
    assert captured.out == "Not this time we have s1\n"

# @pytest.mark.skip("pending")
def test_check_guess3(capsys):
    actual = Clue_Logic().check_guess('h9', 'j9', 'k9')
    captured = capsys.readouterr()
    assert captured.out == "Sorry no help here!\n"

# If we need better test coverage we can add tests for the rest of the cases.

# @pytest.mark.skip("pending")
def test_roll_dice():
    roll = Clue_Logic().roll_dice()
    assert roll <= 6 and roll >= 1

# @pytest.mark.skip("pending")
def test_eligible_rooms():
    clue = Clue_Logic()
    li = clue.eligible_rooms()
    assert len(li[0]) == li[1]

# @pytest.mark.skip("pending")
def test_reset_tables():
    clue = Clue_Logic()
    clue.solution_list.append('words')
    clue.reset_tables()
    assert clue.solution_list == []

# @pytest.mark.skip("pending")
def test_reset_tables2():
    clue = Clue_Logic()
    clue.player_hand.append('words')
    clue.reset_tables()
    assert clue.player_hand == []

# @pytest.mark.skip("pending")
def test_reset_tables3():
    clue = Clue_Logic()
    clue.available_rooms_check.append('words')
    clue.reset_tables()
    assert clue.available_rooms_check == []

# @pytest.mark.skip("pending")
def test_reset_tables4():
    clue = Clue_Logic()
    clue.current_room = 'r7'
    clue.reset_tables()
    assert clue.current_room == "Front Desk - Roll the dice to explore campus"

# Menu_Logic Tests
# @pytest.mark.skip("pending")
def test_menu_logic():
    assert Menu_Logic()
    
# @pytest.mark.skip("pending")
def test_menu(capsys):
    actual = Menu_Logic().menu()
    captured = capsys.readouterr()
    assert captured.out == "Type (roll) to continue play\nType (rules) to view the brief\nType (hand) to view your leads\nType (room) to be reminded of where you are\nType (quit) to leave John's death a mystery\n"

# @pytest.mark.skip("pending")
def test_menu_validation():
    actual = Menu_Logic().menu_validation("roll")
    expected = True
    assert actual == expected
    
# @pytest.mark.skip("pending")
def test_menu_validation2():
    actual = Menu_Logic().menu_validation("gimme_a_schnack")
    expected = False
    assert actual == expected
    

# @pytest.mark.skip("pending")
def test_menu_helper(capsys):
    actual = Menu_Logic().menu_helper("gimme_a_schnack")
    captured = capsys.readouterr()
    assert captured.out == "Please try again\nType (roll) to continue play\nType (rules) to view the brief\nType (hand) to view your leads\nType (room) to be reminded of where you are\nType (quit) to leave John's death a mystery\n"

# @pytest.mark.skip("pending")
# def test_menu_rules(capsys):
#     rule = Menu_Logic().rules()
#     captured = capsys.readouterr()
#     assert captured == "'\n'\n '            Solve the murder of John Cokos:\n'\n '            1. Roll the dice to move from room to room\n'\n '            \n'\n '            2. Your practice and final whiteboards will ask for a suspect, a '\n 'gadget, and a room\n'\n '                - You must move to a room to complete any whiteboard\n'\n '                        AND\n'\n '                - Whiteboards can only reference the room you are standing '\n 'in\n'\n '            \n'\n '            3. Practice your whiteboarding skills\n'\                - You'll start the game with 6 cards to eliminate suspects, \n 'gadgets and rooms\n'\n '                - Use the cards and the front-end website to develop your '\n 'algorithm\n'\n '                - Make eliminations by suggesting a suspect, a gadget, and '\n 'the room you are in\n'\n '                - The TA will give you a hint if they have one\n'\n '                - Use the feedback to make corrections to your practice '\n 'whiteboard\n'\n '                - You can practice as many times as you want\n'\n '            \n'\n '            4. Your final whiteboard\n'\n                 - For your final whiteboard, move to the room you'd like to \n 'solve in\n'\n '                - Schedule some time with an instructor and present your '\n 'final solution \n'\n '                - The instructor will give you feedback and a passing or '\n 'failing grade\n'\n '                - The game ends once you receive your grade\n'\n '                - \n'\n             5. You've only got one chance at your final whiteboard, so study \n 'hard\n'\n '        \n') == ('\n'\n '            Solve the murder of John Cokos:\n'\n '            1. Roll the dice to move from room to room\n'\n '            \n'\n '            2. Your practice and final whiteboards will ask for a suspect, a '\n 'gadget, and a room\n'\n '                - You must move to a room to complete any whiteboard\n'\n '                        AND\n'\n '                - Whiteboards can only reference the room you are standing '\n 'in\n'\n '            \n'\n '            3. Practice your whiteboarding skills\n'\n                 - You'll start the game with 6 cards to eliminate suspects, \n 'gadgets and rooms\n'\n '                - Use the cards and the front-end website to develop your '\n 'algorithm\n'\n '                - Make eliminations by suggesting a suspect, a gadget, and '\n 'the room you are in\n'\n '                - The TA will give you a hint if they have one\n'\n '                - Use the feedback to make corrections to your practice '\n 'whiteboard\n'\n '                - You can practice as many times as you want\n'\n '            \n'\n '            4. Your final whiteboard\n'\n                 - For your final whiteboard, move to the room you'd like to \n 'solve in\n'\n '                - Schedule some time with an instructor and present your '\n 'final solution \n'\n '                - The instructor will give you feedback and a passing or '\n 'failing grade\n'\n '                - The game ends once you receive your grade\n'\n '                - \n'\n             5. You've only got one chance at your final whiteboard, so study \n 'hard\n'\n '        '"


# Prompt Tests

# @pytest.mark.skip("pending")
def test_prompt_logic():
    assert Prompt()
    
# @pytest.mark.skip("pending")
def test_prompt_logic2():
    test_prompt = Prompt()
    actual = test_prompt.accused_person
    expected = []
    actual == expected
    
# @pytest.mark.skip("pending")
def test_start_game():
    pass

# @pytest.mark.skip("pending")
def test_pick_a_player():
    pass


#### RUN THIS WITH pytest -s and type quit 
# when prompted in terminal

# @pytest.mark.skip("pending")
def test_time_to_deal_and_pick():
    test_prompt = Prompt()
    actual = test_prompt.time_to_deal_and_pick("Kim")
    expected = "quit"
    assert actual == expected
    
# # @pytest.mark.skip("pending")
# def test_time_to_deal_and_pick2():
#     test_prompt = Prompt()
#     actual = test_prompt.time_to_deal_and_pick("Kim")
#     expected = "quit"
#     assert actual != expected   
    