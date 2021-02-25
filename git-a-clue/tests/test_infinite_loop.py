from unittest import TestCase, main
from unittest.mock import patch
import sys
import os
import pytest

from git_a_clue.prompt import Prompt
from git_a_clue.main_logic import Clue_Logic
from git_a_clue.menu_logic import Menu_Logic

# all pass with the addition of mock_input optional arguments
# and with if/else statements around both expected input areas

###################
#  start_game tests
###################

   
def test_capture_output_bad_input(capsys):
    Prompt().start_game('green')
    out,err = capsys.readouterr()
    
    assert 'Please enter a valid option' in out 
    
###################
#  pick_a_player tests
###################

    
def test_capture_output_play_input(capsys):
    Prompt().pick_a_player('yellow')
    out,err = capsys.readouterr()
    
    assert 'Please choose you avatar' in out 

###################
#  time_to-deal_and_pick tests
###################

    
def test_capture_output_play_input(capsys):
    Prompt().time_to_deal_and_pick('yellow')
    out,err = capsys.readouterr()
    
    assert 'Please choose you avatar' in out 

        
        
# https://dbader.org/blog/python-check-if-file-exists
# https://www.devdungeon.com/content/python-use-stringio-capture-stdout-and-stderr
# https://stackoverflow.com/questions/37918163/unittests-for-infinite-loop
