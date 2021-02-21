from playsound import playsound

playsound('./assets/sounds/creeky_door.mp3')

# For pycairo fix:
# From root directory: kim/codefellows--First I installed homebrew, 
# then pkg-config, and then installed pycairo using $ brew install python cairo. 
# I installed using $ pip3 install pycairo just to make sure and it is all good. 

# used pip install pipenv to create poetry alternative environment
# then pipenv shell

# this video: https://realpython.com/lessons/playsound/
# Needed to use pipenv install PyObjC like the video describes for Mac error missing AppKit
