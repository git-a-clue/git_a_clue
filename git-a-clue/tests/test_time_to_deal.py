# from unittest import TestCase, main
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
# time_to_deal_and_pick function tests
###########################


# @pytest.mark.skip("pending")  
def test_capture_deal_bad_input(capsys):
    Prompt().time_to_deal_and_pick('kim','yellow')
    out,err = capsys.readouterr()
    
    assert 'Alright Detective kim' in out 
    

# @pytest.mark.skip("pending")  
def test_capture_deal_rules_input(capsys):
    Prompt().time_to_deal_and_pick('kim','rules')
    out,err = capsys.readouterr()
    assert 'Please choose from menu:' in out 

# @pytest.mark.skip("pending")  
def test_capture_deal_hand_input(capsys):
    Prompt().time_to_deal_and_pick('kim','hand')
    out,err = capsys.readouterr()
    assert 'Please choose from menu:' in out 
    
# @pytest.mark.skip("pending")  
def test_capture_deal_room_input(capsys):
    Prompt().time_to_deal_and_pick('kim','room')
    out,err = capsys.readouterr()
    assert 'Please choose from menu:' in out 


