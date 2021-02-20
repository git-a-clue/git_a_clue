import pytest
from git_a_clue.main_logic import Clue_Logic
from git_a_clue.menu_logic import Menu_Logic
from git_a_clue.prompt import Prompt

# Main_Logic Tests
@pytest.mark.skip("pending")
def test_logic():
    actual = Clue_Logic.suspects[0]
    expected = 's1'
    assert actual == expected

@pytest.mark.skip("pending")
def test_normalize():
    actual = Clue_Logic().normalize('AWS')
    expected = 'aws'
    assert actual == expected

@pytest.mark.skip("pending")
def test_start_game_deal_cards():
    test_in = ['s1', 's2', 's3']
    test_out = []
    Clue_Logic().start_game_deal_cards(test_in, test_out)
    assert test_out[0]

@pytest.mark.skip("pending")
def test_random_helper():
    actual = Clue_Logic().random_helper(2,6)
    assert actual >= 2 and actual <= 6

@pytest.mark.skip("pending")
def test_solution_deal():
    clue = Clue_Logic()
    clue.solution_deal()
    actual = len(clue.solution_list)
    expected = 3
    assert actual == expected

@pytest.mark.skip("pending")
def test_player_hand_deal():
    clue = Clue_Logic()
    clue.player_hand_deal()
    actual = len(clue.player_hand)
    expected = 6
    assert actual == expected

@pytest.mark.skip("pending")
def test_check_guess1(capsys):
    actual = Clue_Logic().check_guess('s9', 'g9', 'r9')
    captured = capsys.readouterr()
    assert captured.out == "Sorry no help here!\n"

@pytest.mark.skip("pending")
def test_check_guess2(capsys):
    clue = Clue_Logic()
    clue.suspects = ['s1']
    clue.check_guess('s1', 's1', 's1')
    captured = capsys.readouterr()
    assert captured.out == "Not this time we have s1\n"

@pytest.mark.skip("pending")
def test_check_guess3(capsys):
    actual = Clue_Logic().check_guess('h9', 'j9', 'k9')
    captured = capsys.readouterr()
    assert captured.out == "Sorry no help here!\n"

# If we need better test coverage we can add tests for the rest of the cases.

@pytest.mark.skip("pending")
def test_roll_dice():
    roll = Clue_Logic().roll_dice()
    assert roll <= 6 and roll >= 1

@pytest.mark.skip("pending")
def test_eligible_rooms():
    clue = Clue_Logic()
    li = clue.eligible_rooms()
    assert len(li[0]) == li[1]

@pytest.mark.skip("pending")
def test_reset_tables():
    clue = Clue_Logic()
    clue.solution_list.append('words')
    clue.reset_tables()
    assert clue.solution_list == []

@pytest.mark.skip("pending")
def test_reset_tables2():
    clue = Clue_Logic()
    clue.player_hand.append('words')
    clue.reset_tables()
    assert clue.player_hand == []

@pytest.mark.skip("pending")
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

# Prompt Tests

# Pytest.mark.skip
# @pytest.mark.skip("pending")
# # Ashley Casimir taught me about capturing print statements
# def test_bst_add_right_kid(create_int_tree, capsys):
#     create_int_tree.add(16)
#     captured = capsys.readouterr()
#     assert captured.out == "11\n13\n15\n16\n"