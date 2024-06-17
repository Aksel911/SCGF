import subprocess as sp
import time
import psutil
import pyautogui
import pygetwindow as gw
import random


def click_center_of_window(window_title):
    windows = gw.getWindowsWithTitle(window_title)
    if windows:
        window = windows[0]
        center_x = window.left + window.width // 2
        center_y = window.top + window.height // 2
        num_clicks = random.randint(1, 1001)
        print(f"Making {num_clicks} clicks for: {window_title}")
        for _ in range(num_clicks):
            pyautogui.click(center_x, center_y)
            time.sleep(0.1)
    else:
        print(f"Window with title containing '{window_title}' not found.")


def close_process(process_name):
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == process_name:
            proc.terminate()


def run_process(game_id, window_title, process_name, delay_click, delay_close):
    sp.Popen(f'start steam://rungameid/{game_id}', shell=True)
    time.sleep(delay_click)
    click_center_of_window(window_title)
    time.sleep(delay_close)
    close_process(process_name)


processes = [
    {"game_id": "2923300", "title": "Banana", "name": "Banana.exe", "start_delay": 10, "close_delay": 60},
    {"game_id": "2977660", "title": "Cats", "name": "Cats.exe", "start_delay": 10, "close_delay": 90},
    {"game_id": "3015610", "title": "Banana and Cucumber", "name": "Banana and Cucumber.exe", "start_delay": 10, "close_delay": 60},
    {"game_id": "2784840", "title": "Egg", "name": "Egg.exe", "start_delay": 10, "close_delay": 90}
]

pyautogui.PAUSE = 0.00001

pint = 0

while True:
    print(f'Start loop: {pint}...')
    pint += 1
    for process in processes:
        run_process(process["game_id"], process["title"], process["name"], process["start_delay"], process["close_delay"])

    time.sleep(10)
    last_pint = pint - 1
    print(f'Loop {last_pint} finished!')
    # time.sleep(1800)
