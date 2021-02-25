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
# pick_a_player function tests
###########################


# @pytest.mark.skip("pending")  
def test_capture_pick_bad_input(capsys):
    Prompt().pick_a_player('yellow')
    out,err = capsys.readouterr()
    
    assert 'Please choose you avatar' in out 

# @pytest.mark.skip("pending")  
def test_capture_pick_g_input(capsys):
    Prompt().pick_a_player('g')
    out,err = capsys.readouterr()
    assert 'Aaron' in out 
    
# @pytest.mark.skip("pending")  
def test_capture_pick_roll_input(capsys):
    Prompt().pick_a_player('roll')
    out,err = capsys.readouterr()
    assert 'pick an avatar' in out 


# @pytest.mark.skip("pending")  
def test_capture_pick_rules_input(capsys):
    Prompt().pick_a_player('rules')
    out,err = capsys.readouterr()
    assert 'Before we play' in out 

# @pytest.mark.skip("pending")  
def test_capture_pick_hand_input(capsys):
    Prompt().pick_a_player('hand')
    out,err = capsys.readouterr()
    assert 'pick an avatar' in out 
    
# @pytest.mark.skip("pending")  
def test_capture_pick_room_input(capsys):
    Prompt().pick_a_player('room')
    out,err = capsys.readouterr()
    assert 'Front Desk' in out 

