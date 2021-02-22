import sys
import pytest
import re
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
    clue.check_guess('s1', 'g9', 'r9')
    captured = capsys.readouterr()
    assert captured.out == "Not this time we have s1\n"

# @pytest.mark.skip("pending")
def test_check_guess2_1(capsys):
    clue = Clue_Logic()
    clue.gadgets = ['g1']
    clue.check_guess('s9', 'g1', 'r9')
    captured = capsys.readouterr()
    assert captured.out == "Not this time we have g1\n"

# @pytest.mark.skip("pending")
def test_check_guess2_2(capsys):
    clue = Clue_Logic()
    clue.rooms = ['r1']
    clue.check_guess('s9', 'g9', 'r1')
    captured = capsys.readouterr()
    assert captured.out == "Not this time we have r1\n"

# @pytest.mark.skip("pending")
def test_check_guess2_3(capsys):
    clue = Clue_Logic()
    clue.rooms = ['r1']
    clue.gadgets = ['g1']
    clue.suspects = ['s1']
    clue.check_guess('s2', 'g2', 'r1')
    captured = capsys.readouterr()
    assert captured.out == "Not this time we have r1\n"


# @pytest.mark.skip("pending")
def test_check_guess3(capsys):
    actual = Clue_Logic().check_guess('h9', 'j9', 'k9')
    captured = capsys.readouterr()
    assert captured.out == "Sorry no help here!\n"
    
# @pytest.mark.skip("pending")
def test_check_guess_have_solution(capsys):
    clue = Clue_Logic()
    sol_return = clue.solution_deal()
    truth = clue.solution_list
    
    actual = clue.check_guess(truth[0], truth[1], truth[2])
    captured = capsys.readouterr()
    assert captured.out == f"CHEAT {truth}\nSorry no help here!\n"


# If we need better test coverage we can add tests for the rest of the cases.

# @pytest.mark.skip("pending")
def test_roll_dice():
    roll = Clue_Logic().roll_dice()
    assert roll <= 6 and roll >= 1

# @pytest.mark.skip("pending")
def test_eligible_rooms():
    clue = Clue_Logic()
    li = clue.eligible_rooms()
    if li[1] == 6:
        assert len(li[0]) == li[1]+1
    else:
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
def test_menu_helper2(capsys):
    new_player = Clue_Logic()
    new_player.player_hand.append('s1')
    actual = Menu_Logic.menu_helper(new_player,"hand")
    captured = capsys.readouterr()
    expected = "['s1']\n"
    
    assert captured.out == expected

# @pytest.mark.skip("pending")
def test_menu_helper3(capsys):
    new_player = Clue_Logic()
    new_player.current_room = ('r7')
    actual = Menu_Logic.menu_helper(new_player,"room")
    captured = capsys.readouterr()
    expected = "r7\n"
    
    assert captured.out == expected


# @pytest.mark.skip("pending")
def test_menu_rules():
    
    Menu_Logic().rules()
    actual = '/Users/kim/codefellows/401/git_a_clue/git-a-clue/git_a_clue/assets/rules.txt'
    assert actual


# Prompt Tests

# @pytest.mark.skip("pending")
def test_prompt_logic():
    assert Prompt()
    
    
# @pytest.mark.skip("pending")
def test_prompt_logic3():
    test_prompt = Prompt()
    actual = test_prompt.accused_person
    expected = []
    assert actual == expected
    
