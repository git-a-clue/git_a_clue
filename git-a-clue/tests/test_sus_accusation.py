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
# sus_accusation function tests
###########################


# @pytest.mark.skip("pending")    
def test_capture_sus_bad_input(capsys):
    Prompt().sus_accusation('yellow')
    out,err = capsys.readouterr()
    
    assert 'Please choose from available suspects' in out 
    
# @pytest.mark.skip("pending")  
def test_capture_sus_g_input(capsys):
    Prompt().sus_accusation('g')
    out,err = capsys.readouterr()
    assert 'code sucks' in out 

# @pytest.mark.skip("pending")  
def test_capture_sus_key_input(capsys):
    Prompt().sus_accusation('a')
    out,err = capsys.readouterr()
    assert 'Dario Thornhill' in out 


# @pytest.mark.skip("pending")  
def test_capture_sus_roll_input(capsys):
    Prompt().sus_accusation('roll')
    out,err = capsys.readouterr()
    assert 'Cannot re-roll' in out 
    
# @pytest.mark.skip("pending")  
def test_capture_sus_rules_input(capsys):
    Prompt().sus_accusation('rules')
    out,err = capsys.readouterr()
    assert 'Please choose from available suspects' in out 


# @pytest.mark.skip("pending")  
def test_capture_sus_hand_input(capsys):
    Prompt().sus_accusation('hand')
    out,err = capsys.readouterr()
    assert 'Please choose from available suspects' in out 
    
# @pytest.mark.skip("pending")  
def test_capture_sus_room_input(capsys):
    Prompt().sus_accusation('room')
    out,err = capsys.readouterr()
    assert 'You are currently in' in out 

##############################

