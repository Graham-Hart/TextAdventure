import time
import os
import sys

import loader

INTERVAL = 0.04
stages = None


def delay_print(s, interval):
    for c in s:
        print(c, end="", flush=True)
        time.sleep(interval)
    print()


def delay_input(prompt, interval):
    delay_print(prompt, interval)
    return input("\n")


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def run_stage(stage):
    cls()
    delay_print(stage["Text"], INTERVAL)
    if not stage["IsEnd"]:
        for i, opt in enumerate(stage["Options"]):
            delay_print(f"{i+1}: {opt}", INTERVAL)
        print()
        choice = delay_input("What do you do? (Number)", INTERVAL)

        while not any(map(str.isdigit, choice)) or int(choice) > len(stage["Options"]) or int(choice) == 0:
            choice = delay_input("Invalid Input. Try Again.", INTERVAL)
        return stage["Outcomes"][int(choice)-1]
    else:
        return None


def main():
    global stages
    stages = loader.load_story("story.txt")
    print(stages)
    stage = stages["start"]
    while True:
        next_stage = run_stage(stage)
        if next_stage == None:
            break
        else:
            try:
                stage = stages[next_stage]
            except:
                print(
                    f"Attempted to load stage '{next_stage}', stage not found. Please ensure that stage exists in story.txt.")
                sys.exit()
    delay_input("Press ENTER to exit.", INTERVAL)
    cls()


main()
