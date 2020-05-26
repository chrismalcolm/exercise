"""
    Simple workout program.
"""

import copy
import json
import os
import random
import threading
import time


# Load config
with open("config.json", 'r') as cfg:
    CONFIG = json.load(cfg)
EXERCISE_TIME = CONFIG["exercise_time"]
COOLDOWN_TIME = CONFIG["cooldown_time"]
COUNT = CONFIG["count"]
EXERCISE_DICT = {
    category: set(exercises)
    for category, exercises in CONFIG["exercises"].items()
}

# State functions
def clear_cli():
    """Clear the CLI prompt."""
    os.system('cls' if os.name == 'nt' else 'clear')

def play_sound(name):
    """Play the sound using mpg123, in a different thread."""
    thread = threading.Thread(
        target=os.system,
        name=name,
        args=("mpg123 -q sounds/%s.mp3" % name,),
        daemon=True
    )
    thread.start()


# Run program
clear_cli()
print("Welcome to the workout programm!")
play_sound("welcome")
input("Press enter to start!")

for k, v in EXERCISE_DICT.items():
    input("--> Press enter to see %s workout" % k)
    clear_cli()
    print(k, "\n+-", "\n+- ".join(v), "\n")


clear_cli()

print("WORKOUT")
print("Exercise time: %is" % EXERCISE_TIME)
print("Cooldown time: %is" % COOLDOWN_TIME)
print("Number of exercises: %i" % COUNT)

input("--> Press enter to organise workout")
clear_cli()


CACHE = copy.deepcopy(EXERCISE_DICT)
CURRENT_TYPE = random.choice(list(CACHE.keys()))
EXERCISE_LIST = []

print("Workout list")
for i in range(COUNT):
    diff_list = list(CACHE.keys() - {CURRENT_TYPE}) or [CURRENT_TYPE]
    if not CACHE.get(CURRENT_TYPE):
        CACHE = copy.deepcopy(EXERCISE_DICT)
    CURRENT_TYPE = random.choice(diff_list)
    exercise = CACHE[CURRENT_TYPE].pop()
    print("Exercise %i: %s (%s)" %  (i+1, exercise, CURRENT_TYPE))
    EXERCISE_LIST.append(exercise)
    if not CACHE[CURRENT_TYPE]:
        del CACHE[CURRENT_TYPE]


play_sound("get_ready")
input("--> Press enter to begin workout!")


for n, exercise in enumerate(EXERCISE_LIST):

    # Do cooldown part
    for second_left in range(COOLDOWN_TIME, 0, -1):
        clear_cli()
        print("%i\n" % second_left)
        print("Next exercise %i: %s\n" % (n + 1, exercise))
        if second_left == COOLDOWN_TIME - 2:
            play_sound("cooldown")
        if second_left == 3:
            play_sound("countdown")
        time.sleep(1)

    # Do exercise part
    for second_left in range(EXERCISE_TIME, 0, -1):
        clear_cli()
        print("%i\n" % second_left)
        print("Exercise %i: %s\n" % (n + 1, exercise))
        if second_left == int(EXERCISE_TIME / 2):
            play_sound("halfway")
        if second_left == 3:
            play_sound("finish")
        time.sleep(1)

    # Finish exercise
    clear_cli()

clear_cli()
print("CONGRATS")
time.sleep(2)
play_sound("congrats")
input("--> Press enter exit workout program")
exit()
