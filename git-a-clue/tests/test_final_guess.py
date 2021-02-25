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
# final_guess function tests
###########################

@pytest.mark.skip("pending")
def test_final_guess_bad_input(capsys):
    actual = Prompt().final_guess('kim','mr bean','candlestick','garage')
    captured = capsys.readouterr()
    assert 'Heather' in captured.out

########## person_input inner function ##########

@pytest.mark.skip("pending")
def test_capture_final_guess_g_sus_input(capsys):
    actual = Prompt().final_guess('kim','g','candlestick','garage')
    captured = capsys.readouterr()
    assert 'Teri Pfeffer' in captured.out

@pytest.mark.skip("pending")  
def test_capture_final_guess_roll_input(capsys):
    Prompt().final_guess('kim','roll','candlestick','garage')
    out,err = capsys.readouterr()
    assert 'Cannot re-roll' in out 
    
@pytest.mark.skip("pending")  
def test_capture_final_guess_rules_input(capsys):
    Prompt().final_guess('kim','rules','candlestick','garage')
    out,err = capsys.readouterr()
    assert 'Please choose from available suspects.' in out 

@pytest.mark.skip("pending")  
def test_capture_final_guess_hand_input(capsys):
    Prompt().final_guess('kim','hand','candlestick','garage')
    out,err = capsys.readouterr()
    assert 'Please choose from available suspects.' in out 
    
@pytest.mark.skip("pending")  
def test_capture_final_guess_room_input(capsys):
    Prompt().final_guess('kim','room','candlestick','garage')
    out,err = capsys.readouterr()
    assert 'lease choose from available suspects.' in out 


########## gadget_input inner function ##########

@pytest.mark.skip("pending")
def test_capture_final_guess_g_gadget_input(capsys):
    actual = Prompt().final_guess('kim','mr bean','g','garage')
    captured = capsys.readouterr()
    assert 'Teri Pfeffer' in captured.out

@pytest.mark.skip("pending")  
def test_capture_final_guess_roll_gadget_input(capsys):
    actual = Prompt().final_guess('kim','mr bean','roll','garage')
    out,err = capsys.readouterr()
    assert 'Cannot re-roll' in out 
    
@pytest.mark.skip("pending")  
def test_capture_final_guess_rules_gadget_input(capsys):
    Prompt().final_guess('kim','mr bean','rules','garage')
    out,err = capsys.readouterr()
    assert 'Please choose from available gadgets.' in out 
    
@pytest.mark.skip("pending")  
def test_capture_final_guess_hand_gadget_input(capsys):
    Prompt().final_guess('kim','mr bean','hand','garage')
    out,err = capsys.readouterr()
    assert 'Poisoned Donut' in out 

@pytest.mark.skip("pending")  
def test_capture_final_guess_room_gadget_input(capsys):
    Prompt().final_guess('kim','mr bean','room','garage')
    out,err = capsys.readouterr()
    assert 'Please choose from available gadgets.' in out 
 
########## room_input inner function ##########

# @pytest.mark.skip("pending")
def test_capture_final_guess_garage_room_input(capsys):
    actual = Prompt().final_guess('kim','mr bean','rope','garage')
    captured = capsys.readouterr()
    assert 'Teri Pfeffer' in captured.out

# @pytest.mark.skip("pending")  
def test_capture_final_guess_roll_room_input(capsys):
    actual = Prompt().final_guess('kim','mr bean','rope','roll')
    out,err = capsys.readouterr()
    assert 'Cannot re-roll' in out 
    
# @pytest.mark.skip("pending")  
def test_capture_final_guess_rules_room_input(capsys):
    Prompt().final_guess('kim','mr bean','rules','garage')
    out,err = capsys.readouterr()
    assert 'Please choose from available gadgets.' in out 
    
# @pytest.mark.skip("pending")  
def test_capture_final_guess_hand_room_input(capsys):
    Prompt().final_guess('kim','mr bean','hand','garage')
    out,err = capsys.readouterr()
    assert 'Poisoned Donut' in out 

# @pytest.mark.skip("pending")  
def test_capture_final_guess_room_room_input(capsys):
    Prompt().final_guess('kim','mr bean','room','garage')
    out,err = capsys.readouterr()
    assert 'Please choose from available gadgets.' in out 
