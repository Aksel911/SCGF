import subprocess as sp
import time
import psutil
import pyautogui
import pygetwindow as gw
import random
import tkinter as tk
from tkinter import ttk, messagebox, filedialog, scrolledtext
from pymem.ptypes import RemotePointer
from ttkthemes import ThemedStyle
import json
import threading
from pymem.process import *
import pymem




def click_center_of_window(window_title):
    windows = gw.getWindowsWithTitle(window_title)
    if windows:
        window = windows[0]
        center_x = window.left + window.width // 2
        center_y = window.top + window.height // 2
        num_clicks = random.randint(1, 5)
        #num_clicks = random.randint(1, 1001)
        log(f"Making {num_clicks} clicks for: {window_title}")
        for _ in range(num_clicks):
            offset_x = random.randint(-5, 5)
            offset_y = random.randint(-5, 5)

            click_x = center_x + offset_x
            click_y = center_y + offset_y
            pyautogui.click(click_x, click_y)
            time.sleep(0.1)
    else:
        log(f"Window: '{window_title}' not found.")

def GetPtrAddr(base, offsets, pm):
    remote_pointer = RemotePointer(pm.process_handle, base)
    for offset in offsets:
        if offset != offsets[-1]:
            remote_pointer = RemotePointer(pm.process_handle, remote_pointer.value + offset)
        else:
            return remote_pointer.value + offset

def patch_game(exe_name, dll_name, base_offset, offsets, window_title):
    pm = pymem.Pymem(exe_name)
    gameModule = module_from_name(pm.process_handle, dll_name).lpBaseOfDll

    score = random.randint(1, 9999999)
    address = GetPtrAddr(gameModule + base_offset, offsets, pm)
    pm.write_int(address, score)

    log(f"Game: '{window_title}' patched clicks to: {score}.")




def patch_banana(window_title):
    patch_game("Banana.exe", "GameAssembly.dll", 0x00EA7648, [0x4A8, 0x78, 0x48, 0xB8, 0x88, 0x60, 0x28], window_title)

def patch_banana_and_cucumber(window_title):
    patch_game("Banana and Cucumber.exe", "GameAssembly.dll", 0x01332EE0, [0x5C, 0x0, 0x34], window_title)
    # Old versions:
    # patch_game("Banana and Cucumber.exe", "GameAssembly.dll", 0x0139E48C, [0x688, 0x24, 0x54], window_title) # v0.0.5
    # patch_game("Banana and Cucumber.exe", "GameAssembly.dll", 0x0139E40C, [0x688, 0x24, 0x54], window_title) # v0.0.4

def patch_cats(window_title):
    pm = pymem.Pymem("Cats.exe")
    gameModule = module_from_name(pm.process_handle, "GameAssembly.dll").lpBaseOfDll

    original_score = GetPtrAddr(gameModule + 0x01395DE8, [0xBC8], pm)
    original_score = pm.read_int(original_score)

    score = original_score + random.randint(1, 9999999)
    pm.write_int(GetPtrAddr(gameModule + 0x01395DE8, [0xBC8], pm), score)

    log(f"Game: '{window_title}' Original score was: {original_score} , patched score clicks to: {score}.")

def patch_egg(window_title):
    patch_game("Egg.exe", "GameAssembly.dll", 0x00D57188, [0xD40], window_title)

def patch_flags(window_title):
    patch_game("Flaggenspiel.exe", "UnityPlayer.dll", 0x01D04080, [0xD0, 0x8, 0xD8], window_title)


def close_process(process_name):
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == process_name:
            proc.terminate()
def run_process(game_id, window_title, process_name, delay_click, delay_close):
    sp.Popen(f'start steam://rungameid/{game_id}', shell=True)
    time.sleep(delay_click)

    if window_title == "Banana":
        patch_banana(window_title)
    elif window_title == "Cats":
        patch_cats(window_title)
    elif window_title == "Banana and Cucumber":
        patch_banana_and_cucumber(window_title)
    elif window_title == "Egg":
        patch_egg(window_title)
    elif window_title == "Flaggenspiel":
        click_center_of_window(window_title)
        patch_flags(window_title)





    click_center_of_window(window_title)
    log(f"Game: '{window_title}' will close in: {delay_close}...sec")
    time.sleep(delay_close)
    close_process(process_name)


def start_farming():
    global farming
    farming = True
    pint = 0
    while farming:
        log(f'Start loop: {pint}...')

        pint += 1
        for process in processes:
            if not farming:
                break
            log(f"Opening game: '{process["title"]}'...")
            run_process(process["game_id"], process["title"], process["name"], process["start_delay"],
                        process["close_delay"])

        new_loop_start_time = random.randint(5, 15)
        last_pint = pint - 1

        log(f'Loop {last_pint} will finish in {new_loop_start_time}...sec')
        for new_loop_start in range(new_loop_start_time):
            time.sleep(new_loop_start)


        log(f'Loop {last_pint} finished!')
def stop_farming():
    log("Farming stopped. Program will close in 5 seconds...")
    app.after(5000, app.destroy)



def add_game():
    add_game_window = tk.Toplevel(app)
    add_game_window.title("Add Game")

    ttk.Label(add_game_window, text="Steam Game ID:").grid(row=0, column=0)
    ttk.Label(add_game_window, text="Window Title:").grid(row=1, column=0)
    ttk.Label(add_game_window, text="Process Name:").grid(row=2, column=0)
    ttk.Label(add_game_window, text="Start Delay (seconds):").grid(row=3, column=0)
    ttk.Label(add_game_window, text="Close Delay (seconds):").grid(row=4, column=0)

    game_id_entry = ttk.Entry(add_game_window)
    title_entry = ttk.Entry(add_game_window)
    name_entry = ttk.Entry(add_game_window)
    start_delay_entry = ttk.Entry(add_game_window)
    close_delay_entry = ttk.Entry(add_game_window)

    game_id_entry.grid(row=0, column=1)
    title_entry.grid(row=1, column=1)
    name_entry.grid(row=2, column=1)
    start_delay_entry.grid(row=3, column=1)
    close_delay_entry.grid(row=4, column=1)

    start_delay_entry.insert(0, "10")
    close_delay_entry.insert(0, "60")

    def save_game():
        game_id = game_id_entry.get()
        title = title_entry.get()
        name = name_entry.get()
        start_delay = start_delay_entry.get()
        close_delay = close_delay_entry.get()

        if not name.endswith('.exe'):
            name += ".exe"

        if game_id and title and name and start_delay and close_delay:
            processes.append({
                "game_id": game_id,
                "title": title,
                "name": name,
                "start_delay": int(start_delay),
                "close_delay": int(close_delay)
            })
            update_processes_list()
            add_game_window.destroy()
        else:
            messagebox.showerror("Error", "All fields must be filled out!")

    ttk.Button(add_game_window, text="Add Game", command=save_game).grid(row=5, columnspan=2)
def delete_game():
    selected = listbox.curselection()
    if selected:
        processes.pop(selected[0])
        update_processes_list()
    else:
        messagebox.showerror("Error", "No game selected!")




def update_processes_list():
    listbox.delete(0, tk.END)
    for process in processes:
        listbox.insert(tk.END, f'{process["title"]} (ID: {process["game_id"]})')


def save_games():
    file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
    if file_path:
        with open(file_path, 'w') as file:
            json.dump(processes, file)
        messagebox.showinfo("Success", "Games saved successfully!")

def load_games():
    file_path = filedialog.askopenfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
    if file_path:
        with open(file_path, 'r') as file:
            global processes
            processes = json.load(file)
        update_processes_list()
        messagebox.showinfo("Success", "Games loaded successfully!")


def log(message):
    log_text.configure(state='normal')
    log_text.insert(tk.END, f"{message}\n")
    log_text.configure(state='disabled')
    log_text.yview(tk.END)

def on_key_press(event):
    if event.keysym == "F2":
        exit()

start_delay = 10
close_delay = 90

processes = [
    {"game_id": "2923300", "title": "Banana", "name": "Banana.exe", "start_delay": start_delay, "close_delay": close_delay},
    {"game_id": "2977660", "title": "Cats", "name": "Cats.exe", "start_delay": start_delay, "close_delay": close_delay},
    {"game_id": "3015610", "title": "Banana and Cucumber", "name": "Banana and Cucumber.exe", "start_delay": start_delay, "close_delay": close_delay},
    {"game_id": "2784840", "title": "Egg", "name": "Egg.exe", "start_delay": start_delay, "close_delay": close_delay},
    {"game_id": "2996990", "title": "Flaggenspiel", "name": "Flaggenspiel.exe", "start_delay": start_delay, "close_delay": close_delay}
]

pyautogui.PAUSE = 0.00001

farming = False

app = tk.Tk()
app.title("[SCGF] Steam Clicker Games Farmer")

# Create a themed style
style = ThemedStyle(app)
style.set_theme("breeze")
app.configure(background=style.lookup('TFrame', 'background'))

app.bind("<KeyPress>", on_key_press)

title_label = ttk.Label(app, text="Games for farm:", font=("Helvetica", 14))
title_label.pack(pady=(10, 0))

frame = ttk.Frame(app)
frame.pack(pady=10)

listbox = tk.Listbox(frame, width=50, height=10)
listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

button_frame = ttk.Frame(app)
button_frame.pack(pady=10)

start_button = ttk.Button(button_frame, text="Start Farming", command=lambda: threading.Thread(target=start_farming).start())
start_button.pack(side=tk.LEFT, padx=5)

stop_button = ttk.Button(button_frame, text="Stop Farming", command=stop_farming)
stop_button.pack(side=tk.LEFT, padx=5)

add_button = ttk.Button(button_frame, text="Add Game", command=add_game)
add_button.pack(side=tk.LEFT, padx=5)

delete_button = ttk.Button(button_frame, text="Delete Game", command=delete_game)
delete_button.pack(side=tk.LEFT, padx=5)

save_button = ttk.Button(button_frame, text="Save Games", command=save_games)
save_button.pack(side=tk.LEFT, padx=5)

load_button = ttk.Button(button_frame, text="Load Games", command=load_games)
load_button.pack(side=tk.LEFT, padx=5)

log_frame = ttk.Frame(app)
log_frame.pack(pady=10, fill=tk.BOTH, expand=True)

log_text = scrolledtext.ScrolledText(log_frame, wrap=tk.WORD, height=10)
log_text.pack(fill=tk.BOTH, expand=True)
log_text.config(state=tk.DISABLED)
log(f"""Welcome to SCGF!

This program automatically launches Steam games.
Finds the center of the program window and patches clicks in all 5 pre-installed games (Banana, Cucumber, Cats, Egg, Flag Clicker) from 1 to 9999999, then makes a random number of clicks (from 10 to 1000), then closes the game and opens the next one.

Dont forget to set Flag Clicker game to window mode!


https://github.com/Aksel911/SCGF""")


update_processes_list()

app.mainloop()
