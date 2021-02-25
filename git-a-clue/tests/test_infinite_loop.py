from unittest import TestCase, main
from unittest.mock import patch
import sys
import os
import pytest

from git_a_clue.prompt_test import Prompt
from git_a_clue.main_logic_test import Clue_Logic
from git_a_clue.menu_logic_test import Menu_Logic

# all pass with the addition of mock_input optional arguments
# and with if/else statements around both expected input areas


def test_capture_start_bad_input(capsys):
    Prompt().start_game('green')
    out,err = capsys.readouterr()
    
    assert 'Please enter a valid option' in out 
    

# @pytest.mark.skip("pending")  
def test_capture_pick_bad_input(capsys):
    Prompt().pick_a_player('yellow')
    out,err = capsys.readouterr()
    
    assert 'Please choose you avatar' in out 


# @pytest.mark.skip("pending")    
def test_capture_roll_bad_input(capsys):
    Prompt().roll_and_rooms('yellow')
    out,err = capsys.readouterr()
    
    assert 'Pick a room' in out 


# @pytest.mark.skip("pending")
def test_sus_accusation_bad_input(capsys):
    Prompt().sus_accusation('orange')
    out,err = capsys.readouterr()
    
    assert 'Please choose from available' in out 


# @pytest.mark.skip("pending")
def test_gad_accusation_bad_input(capsys):
    Prompt().gad_accusation('kim','orange')
    out,err = capsys.readouterr()
    
    assert 'Please choose from available' in out 


# @pytest.mark.skip("pending")
def test_type_of_guess_bad_input(capsys):
    actual = Prompt().type_of_guess('purple')
    captured = capsys.readouterr()
    assert 'Please choose either (final) or (roll).' in captured.out
    

# @pytest.mark.skip("pending")
def test_final_guess_bad_input(capsys):
    actual = Prompt().final_guess('g','yellow','green')
    captured = capsys.readouterr()
    assert 'Please choose from available suspects..' in captured.out


# https://dbader.org/blog/python-check-if-file-exists
# https://www.devdungeon.com/content/python-use-stringio-capture-stdout-and-stderr
# https://stackoverflow.com/questions/37918163/unittests-for-infinite-loop
