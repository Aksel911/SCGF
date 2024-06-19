import random
import time
import subprocess as sp

start_delay = 10
close_delay = 10

processes = [
    {"game_id": "2923300", "title": "Banana", "name": "Banana.exe", "start_delay": start_delay, "close_delay": close_delay},
    {"game_id": "2977660", "title": "Cats", "name": "Cats.exe", "start_delay": start_delay, "close_delay": close_delay},
    {"game_id": "3015610", "title": "Banana and Cucumber", "name": "Banana and Cucumber.exe", "start_delay": start_delay, "close_delay": close_delay},
    {"game_id": "2784840", "title": "Egg", "name": "Egg.exe", "start_delay": start_delay, "close_delay": close_delay},
    {"game_id": "2996990", "title": "Flaggenspiel", "name": "Flaggenspiel.exe", "start_delay": start_delay, "close_delay": close_delay}
]

def run_process(game_id, window_title, process_name, delay_click, delay_close):
    process = sp.Popen(f'start steam://rungameid/{game_id}', shell=True)
    time.sleep(delay_click)
    print(f"Game {window_title} started. Waiting for {delay_close} seconds before closing...")
    time.sleep(delay_close)
    print(f"Closing game {window_title}...")
    sp.Popen(f'taskkill /IM "{process_name}" /F', shell=True)

def start_farming():
    global farming
    farming = True
    pint = 0
    while farming:
        print(f'Start loop: {pint}...')

        pint += 1
        for process in processes:
            if not farming:
                break
            print(f"Opening game: '{process["title"]}'...")
            run_process(process["game_id"], process["title"], process["name"], process["start_delay"], process["close_delay"])

        #new_loop_start_time = random.randint(5, 15)
        new_loop_start_time = random.randint(10800, 12600)  # 3 - 3.5h
        last_pint = pint - 1

        print(f'Loop {last_pint} will finish in {new_loop_start_time}... sec')
        time.sleep(new_loop_start_time)

start_farming()
