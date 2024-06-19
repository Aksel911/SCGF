import random
import time
import subprocess as sp
import logging
import psutil

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

start_delay = 10
close_delay = 90

processes = [
    {"game_id": "2923300", "title": "Banana", "name": "Banana.exe", "start_delay": start_delay, "close_delay": close_delay},
    {"game_id": "2977660", "title": "Cats", "name": "Cats.exe", "start_delay": start_delay, "close_delay": close_delay},
    {"game_id": "3015610", "title": "Banana and Cucumber", "name": "Banana and Cucumber.exe", "start_delay": start_delay, "close_delay": close_delay},
    {"game_id": "2784840", "title": "Egg", "name": "Egg.exe", "start_delay": start_delay, "close_delay": close_delay},
    {"game_id": "2996990", "title": "Flaggenspiel", "name": "Flaggenspiel.exe", "start_delay": start_delay, "close_delay": close_delay}
]

def is_process_running(process_name):
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == process_name:
            return True
    return False

def run_process(game_id, window_title, process_name, delay_click, delay_close):
    try:
        process = sp.Popen(f'start steam://rungameid/{game_id}', shell=True)
        logging.info(f"✨ Game {window_title} started. Waiting for {delay_click} seconds to check if it is running...")
        time.sleep(delay_click)

        if is_process_running(process_name):
            logging.info(f"✅ Game {window_title} is running. Waiting for {delay_close} seconds before closing...")
            time.sleep(delay_close)
            logging.info(f"✖️ Closing game {window_title}...")
            sp.Popen(f'taskkill /IM "{process_name}" /F', shell=True)
        else:
            logging.warning(f"⚠️ Game {window_title} did not start. Skipping to the next game...")
    except Exception as e:
        logging.error(f"❌ An error occurred: {e}")

def start_farming():
    pint = 0
    while True:
        logging.info(f"🚩 Starting loop: {pint}")
        for process in processes:
            logging.info(f"🎮 Opening game: '{process['title']}'...")
            run_process(process["game_id"], process["title"], process["name"], process["start_delay"], process["close_delay"])

        new_loop_start_time = random.randint(10800, 11000)  # 3h+-
        last_pint = pint
        pint += 1
        logging.info(f"✅ Loop: {last_pint} finished!")
        logging.info(f"🕒 Waiting for {new_loop_start_time} seconds before starting the next loop: {pint}...")
        time.sleep(new_loop_start_time)

if __name__ == "__main__":
    try:
        start_farming()
    except KeyboardInterrupt:
        logging.info("⛔ Stopping farming...")
