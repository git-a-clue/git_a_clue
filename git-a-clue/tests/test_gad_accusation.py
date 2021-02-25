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
# gad_accusation function tests
###########################


# @pytest.mark.skip("pending")    
def test_capture_gad_bad_input(capsys):
    Prompt().gad_accusation('kim','yellow')
    out,err = capsys.readouterr()
    
    assert 'Please choose from available gadgets' in out 
    
# @pytest.mark.skip("pending")  
def test_capture_gad_g_input(capsys):
    Prompt().gad_accusation('kim','g')
    out,err = capsys.readouterr()
    assert 'Please choose from available gadgets' in out 


# @pytest.mark.skip("pending")  
def test_capture_gad_roll_input(capsys):
    Prompt().gad_accusation('kim','roll')
    out,err = capsys.readouterr()
    assert 'Cannot re-roll' in out 
    
# @pytest.mark.skip("pending")  
def test_capture_gad_rules_input(capsys):
    Prompt().gad_accusation('kim','rules')
    out,err = capsys.readouterr()
    assert 'Please choose from available gadgets' in out 


# @pytest.mark.skip("pending")  
def test_capture_gad_hand_input(capsys):
    Prompt().gad_accusation('kim','hand')
    out,err = capsys.readouterr()
    assert 'This is your hand' in out 
    
# @pytest.mark.skip("pending")  
def test_capture_gad_room_input(capsys):
    Prompt().gad_accusation('kim','room')
    out,err = capsys.readouterr()
    assert 'Apple Pencil' in out 

