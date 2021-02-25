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

###########################
# type_of_guess function tests
###########################

# @pytest.mark.skip("pending")
def test_capture_type_of_guess_bad_input(capsys):
    actual = Prompt().type_of_guess('purple')
    captured = capsys.readouterr()
    assert 'Please choose either (final) or (roll).' in captured.out
        
# @pytest.mark.skip("pending")  
def test_capture_type_of_guess_final_input(capsys):
    Prompt().type_of_guess('final')
    out,err = capsys.readouterr()
    assert '(FINAL)' in out 


# @pytest.mark.skip("pending")  
def test_capture_type_of_guess_roll_input(capsys):
    Prompt().type_of_guess('roll')
    out,err = capsys.readouterr()
    assert '(ROLL)' in out 
    
# @pytest.mark.skip("pending")  
def test_capture_type_of_guess_rules_input(capsys):
    Prompt().type_of_guess('rules')
    out,err = capsys.readouterr()
    assert 'Would you like to (ROLL) again' in out 


# @pytest.mark.skip("pending")  
def test_capture_type_of_guess_hand_input(capsys):
    Prompt().type_of_guess('hand')
    out,err = capsys.readouterr()
    assert '(FINAL) accusation' in out 
    
# @pytest.mark.skip("pending")  
def test_capture_type_of_guess_room_input(capsys):
    Prompt().type_of_guess('room')
    out,err = capsys.readouterr()
    assert 'Would you like' in out 

