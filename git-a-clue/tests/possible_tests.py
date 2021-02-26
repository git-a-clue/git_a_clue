# @pytest.mark.skip("pending")
# def test_menu_rules(capsys):
#     rule = Menu_Logic().rules()
#     captured = capsys.readouterr()
#     assert captured == "'\n'\n '            Solve the murder of John Cokos:\n'\n '            1. Roll the dice to move from room to room\n'\n '            \n'\n '            2. Your practice and final whiteboards will ask for a suspect, a '\n 'gadget, and a room\n'\n '                - You must move to a room to complete any whiteboard\n'\n '                        AND\n'\n '                - Whiteboards can only reference the room you are standing '\n 'in\n'\n '            \n'\n '            3. Practice your whiteboarding skills\n'\                - You'll start the game with 6 cards to eliminate suspects, \n 'gadgets and rooms\n'\n '                - Use the cards and the front-end website to develop your '\n 'algorithm\n'\n '                - Make eliminations by suggesting a suspect, a gadget, and '\n 'the room you are in\n'\n '                - The TA will give you a hint if they have one\n'\n '                - Use the feedback to make corrections to your practice '\n 'whiteboard\n'\n '                - You can practice as many times as you want\n'\n '            \n'\n '            4. Your final whiteboard\n'\n                 - For your final whiteboard, move to the room you'd like to \n 'solve in\n'\n '                - Schedule some time with an instructor and present your '\n 'final solution \n'\n '                - The instructor will give you feedback and a passing or '\n 'failing grade\n'\n '                - The game ends once you receive your grade\n'\n '                - \n'\n             5. You've only got one chance at your final whiteboard, so study \n 'hard\n'\n '        \n') == ('\n'\n '            Solve the murder of John Cokos:\n'\n '            1. Roll the dice to move from room to room\n'\n '            \n'\n '            2. Your practice and final whiteboards will ask for a suspect, a '\n 'gadget, and a room\n'\n '                - You must move to a room to complete any whiteboard\n'\n '                        AND\n'\n '                - Whiteboards can only reference the room you are standing '\n 'in\n'\n '            \n'\n '            3. Practice your whiteboarding skills\n'\n                 - You'll start the game with 6 cards to eliminate suspects, \n 'gadgets and rooms\n'\n '                - Use the cards and the front-end website to develop your '\n 'algorithm\n'\n '                - Make eliminations by suggesting a suspect, a gadget, and '\n 'the room you are in\n'\n '                - The TA will give you a hint if they have one\n'\n '                - Use the feedback to make corrections to your practice '\n 'whiteboard\n'\n '                - You can practice as many times as you want\n'\n '            \n'\n '            4. Your final whiteboard\n'\n                 - For your final whiteboard, move to the room you'd like to \n 'solve in\n'\n '                - Schedule some time with an instructor and present your '\n 'final solution \n'\n '                - The instructor will give you feedback and a passing or '\n 'failing grade\n'\n '                - The game ends once you receive your grade\n'\n '                - \n'\n             5. You've only got one chance at your final whiteboard, so study \n 'hard\n'\n '        '"

@pytest.mark.skip("pending")
def test_menu_rules(capsys):
    rule = Menu_Logic().rules()
    captured = capsys.readouterr()
    actual = re.search('(?<=^[\s"\']*)','captured')
    expected = ''
    assert actual == expected


@pytest.mark.skip("pending")
def test_menu_helper2(capsys):
    
    actual = Menu_Logic().menu_helper("hand")
    captured = capsys.readouterr()
    assert captured.out == "s2"


@pytest.mark.skip("pending")
def test_start_game(capsys):
    test_prompt = Prompt()
    actual = test_prompt.start_game()
    expected = None  
    assert actual == expected

@pytest.mark.skip("pending")
def test_time_to_deal_and_pick2():
    test_prompt = Prompt()
    actual = test_prompt.time_to_deal_and_pick("Kim")
    expected = "rules"
    assert actual == expected   


# @pytest.mark.skip("pending")
def test_pick_a_player():
    pass


#### RUN THIS WITH pytest -s and type quit 
# when prompted in terminal

@pytest.mark.skip("pending")
def test_time_to_deal_and_pick():
    test_prompt = Prompt()
    actual = test_prompt.time_to_deal_and_pick("Kim")
    expected = "quit"
    assert actual == expected  
    
@pytest.mark.skip("pending")
def test_menu_rules(capsys):
    actual = Menu_Logic().rules()
    expected = 'Solve'
    assert actual == expected
    # captured = capsys.readouterr()
    # assert captured == "'\n'\n '            Solve the murder of John Cokos:\n'\n '            1. Roll the dice to move from room to room\n'\n '            \n'\n '            2. Your practice and final whiteboards will ask for a suspect, a '\n 'gadget, and a room\n'\n '                - You must move to a room to complete any whiteboard\n'\n '                        AND\n'\n '                - Whiteboards can only reference the room you are standing '\n 'in\n'\n '            \n'\n '            3. Practice your whiteboarding skills\n'\                - You'll start the game with 6 cards to eliminate suspects, \n 'gadgets and rooms\n'\n '                - Use the cards and the front-end website to develop your '\n 'algorithm\n'\n '                - Make eliminations by suggesting a suspect, a gadget, and '\n 'the room you are in\n'\n '                - The TA will give you a hint if they have one\n'\n '                - Use the feedback to make corrections to your practice '\n 'whiteboard\n'\n '                - You can practice as many times as you want\n'\n '            \n'\n '            4. Your final whiteboard\n'\n                 - For your final whiteboard, move to the room you'd like to \n 'solve in\n'\n '                - Schedule some time with an instructor and present your '\n 'final solution \n'\n '                - The instructor will give you feedback and a passing or '\n 'failing grade\n'\n '                - The game ends once you receive your grade\n'\n '                - \n'\n             5. You've only got one chance at your final whiteboard, so study \n 'hard\n'\n '        \n') == ('\n'\n '            Solve the murder of John Cokos:\n'\n '            1. Roll the dice to move from room to room\n'\n '            \n'\n '            2. Your practice and final whiteboards will ask for a suspect, a '\n 'gadget, and a room\n'\n '                - You must move to a room to complete any whiteboard\n'\n '                        AND\n'\n '                - Whiteboards can only reference the room you are standing '\n 'in\n'\n '            \n'\n '            3. Practice your whiteboarding skills\n'\n                 - You'll start the game with 6 cards to eliminate suspects, \n 'gadgets and rooms\n'\n '                - Use the cards and the front-end website to develop your '\n 'algorithm\n'\n '                - Make eliminations by suggesting a suspect, a gadget, and '\n 'the room you are in\n'\n '                - The TA will give you a hint if they have one\n'\n '                - Use the feedback to make corrections to your practice '\n 'whiteboard\n'\n '                - You can practice as many times as you want\n'\n '            \n'\n '            4. Your final whiteboard\n'\n                 - For your final whiteboard, move to the room you'd like to \n 'solve in\n'\n '                - Schedule some time with an instructor and present your '\n 'final solution \n'\n '                - The instructor will give you feedback and a passing or '\n 'failing grade\n'\n '                - The game ends once you receive your grade\n'\n '                - \n'\n             5. You've only got one chance at your final whiteboard, so study \n 'hard\n'\n '        '"

@pytest.mark.skip("pending")
def test_prompt_logic2():
    new_prompt = Prompt() 
    actual = new_prompt.e
    expected = 4
    assert actual == expected 

@pytest.mark.skip("pending")
def test_start_game(monkeypatch):

    # monkeypatch the "input" function, so that it returns "Mark".
    # This simulates the user entering "Mark" in the terminal:
    monkeypatch.setattr('builtins.input', lambda _: "play")

    # go about using input() like you normally would:
    Prompt().start_game()
    
    assert user_input == "play"    

# @pytest.mark.skip("pending")
def test_menu_helper(capsys):
    actual = Menu_Logic().menu_helper("gimme_a_schnack")
    captured = capsys.readouterr()
    assert captured.out == "Please try again\nType (roll) to continue play\nType (rules) to view the brief\nType (hand) to view your leads\nType (room) to be reminded of where you are\nType (quit) to leave John's death a mystery\n"

# @pytest.mark.skip("pending")
def test_menu_helper2(capsys):
    new_player = Clue_Logic()
    new_player.player_hand.append('s1')
    actual = Menu_Logic.menu_helper(new_player,"hand")
    captured = capsys.readouterr()
    expected = "['s1']\n"
    
    assert captured.out == expected

# @pytest.mark.skip("pending")
def test_menu_helper3(capsys):
    new_player = Clue_Logic()
    new_player.current_room = ('r7')
    actual = Menu_Logic.menu_helper(new_player,"room")
    captured = capsys.readouterr()
    expected = "r7\n"
    
    assert captured.out == expected

# https://code-maven.com/mocking-input-and-output-for-python-testing

# Monkeypatch -- https://stackoverflow.com/questions/35851323/how-to-test-a-function-with-input-call