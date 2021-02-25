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
# start_game function tests
###########################

# @pytest.mark.skip("pending")  
def test_capture_start_bad_input(capsys):
    Prompt().start_game('green')
    out,err = capsys.readouterr()
    assert 'Please enter a valid option' in out 
    
# @pytest.mark.skip("pending")  
def test_capture_start_play_input(capsys):
    Prompt().start_game('play')
    out,err = capsys.readouterr()
    assert 'John hates a quitter' in out 

# @pytest.mark.skip("pending")  
def test_capture_start_roll_input(capsys):
    Prompt().start_game('roll')
    out,err = capsys.readouterr()
    assert 'John hates a quitter' in out 

# @pytest.mark.skip("pending")  
def test_capture_start_rules_input(capsys):
    Prompt().start_game('rules')
    out,err = capsys.readouterr()
    assert 'John hates a quitter' in out 

# @pytest.mark.skip("pending")  
def test_capture_start_hand_input(capsys):
    Prompt().start_game('hand')
    out,err = capsys.readouterr()
    assert 'No hand dealt' in out 
    
# @pytest.mark.skip("pending")  
def test_capture_start_room_input(capsys):
    Prompt().start_game('room')
    out,err = capsys.readouterr()
    assert 'John hates a quitter' in out 



# https://dbader.org/blog/python-check-if-file-exists
# https://www.devdungeon.com/content/python-use-stringio-capture-stdout-and-stderr
# https://stackoverflow.com/questions/37918163/unittests-for-infinite-loop
