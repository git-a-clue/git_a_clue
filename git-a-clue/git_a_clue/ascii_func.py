import time
import random
import re

# ALL COLORS!!


def print_ascii(path):
    with open(path, "r") as template:
        new_file = template.read()
        return colorize_text(new_file)



def colorize_text(text):
    text = re.sub("{red?}","\\033[1;31m", text)
    text = re.sub("{green?}","\\033[1;32m", text)
    text = re.sub("{yellow?}","\\033[1;33m", text)
    text = re.sub("{blue?}","\\033[1;34m", text)
    text = re.sub("{purple?}","\\033[1;35m", text)
    text = re.sub("{cyan?}","\\033[1;36m", text)
    text = re.sub("{white?}","\\033[1;37m", text)
    text = re.sub("{end?}","\\033[0m", text)
    return text


def animate_ascii(path, frames, loops=1, delay=0.2):
    for i in range(9):
        print(" ")
    for n in range(loops):
        for x in range(frames):
            get_path = f"{path}_{x}.txt"
            with open (get_path, "r") as template:
                for k in range(9):
                    print("\033[A\033[A")
                text = template.read()  
                text = colorize_text(text)
                print(text)
                time.sleep(delay)


