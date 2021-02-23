from playsound import playsound
import time
import os
import shutil


# def move_sound_animation_png():
#     # display first floorplan--png
#     print('/Users/kim/codefellows/401/git_a_clue/git-a-clue/git_a_clue/assets/fp_animation/animation-blank.png')
#     # wait 9 sec...while playing the sound
#     playsound('/Users/kim/codefellows/401/git_a_clue/git-a-clue/git_a_clue/assets/sounds/magic_appear.mp3')
#     time(9)
#     # display second floor plan--png
#     print('/Users/kim/codefellows/401/git_a_clue/git-a-clue/git_a_clue/assets/fp_animation/animation-start.png')

def move_sound_animation_txt():
    # display first floorplan--png
    with open('/Users/kim/codefellows/401/git_a_clue/git-a-clue/git_a_clue/assets/fp_animation/ascii-floor-plan-names.txt') as f: 
        for line in f: 
            # print(line.strip().center(shutil.get_terminal_size().columns))
            print(line.strip())
            # print (line.strip())
    # wait 9 sec...while playing the sound
    playsound('/Users/kim/codefellows/401/git_a_clue/git-a-clue/git_a_clue/assets/sounds/magic_appear.mp3')
    # time.sleep(5)
    os.system('cls' if os.name == 'nt' else 'clear')

    # display second floor plan--png
    with open('/Users/kim/codefellows/401/git_a_clue/git-a-clue/git_a_clue/assets/fp_animation/ascii-floor-plan-with-you.txt') as f: 
        for line in f: 
            # print(line.strip().center(shutil.get_terminal_size().columns))
            print (line.strip()) 


move_sound_animation_txt()