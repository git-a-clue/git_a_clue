from unittest import TestCase, main
from unittest.mock import patch
import sys
import os
import pytest

from git_a_clue.main_logic import Clue_Logic
from git_a_clue.menu_logic import Menu_Logic
from git_a_clue.prompt import Prompt

# @pytest.fixture
# def fake_capsys(capsys):
#     return capsys

    
def test_capture_output(capsys):
    Prompt().start_game('green')
    out,err = capsys.readouterr()
    
    # print(f'captured text: {captured.out}')
    assert 'Please enter a valid option' in out 
    
# def write_output(mock_input):
#     with open('./start_game_test.txt','a') as sg:
#         sg.write(f'Input given: {mock_input}\n')
#         sg.writelines(captured.out)
    
# def test_start_game_with_input(capsys):
#     capture_output()
#     write_output('play')
    
#     assert os.path.exists('./start_game_test.txt')
    
    # start_game_with_input('p')
    # start_game_with_input('roll')
    # start_game_with_input('rules')
    # start_game_with_input('hand')
    # start_game_with_input('room')
    # start_game_with_input('quit')
    # start_game_with_input('yellow')
    
        
        
# https://dbader.org/blog/python-check-if-file-exists
# https://www.devdungeon.com/content/python-use-stringio-capture-stdout-and-stderr
# https://stackoverflow.com/questions/37918163/unittests-for-infinite-loop
