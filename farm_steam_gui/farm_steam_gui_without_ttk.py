import subprocess as sp
import time
import psutil
import pyautogui
import pygetwindow as gw
import random
import tkinter as tk
from tkinter import messagebox, filedialog, scrolledtext
import json
import threading



def click_center_of_window(window_title):
    windows = gw.getWindowsWithTitle(window_title)
    if windows:
        window = windows[0]
        center_x = window.left + window.width // 2
        center_y = window.top + window.width // 2
        num_clicks = random.randint(1, 1001)
        log(f"Making {num_clicks} clicks for: {window_title}")
        for _ in range(num_clicks):
            pyautogui.click(center_x, center_y)
            time.sleep(0.1)
    else:
        log(f"Window with title containing '{window_title}' not found.")


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
            run_process(process["game_id"], process["title"], process["name"], process["start_delay"], process["close_delay"])

        time.sleep(10)
        last_pint = pint - 1
        log(f'Loop {last_pint} finished!')
        # time.sleep(1800)


def stop_farming():
    global farming
    farming = False
    log("Farming stopped.")


def add_game():
    add_game_window = tk.Toplevel(app)
    add_game_window.title("Add Game")
    add_game_window.configure(bg='#2b2b2b')

    tk.Label(add_game_window, text="Steam Game ID:", bg='#2b2b2b', fg='white').grid(row=0, column=0)
    tk.Label(add_game_window, text="Window Title:", bg='#2b2b2b', fg='white').grid(row=1, column=0)
    tk.Label(add_game_window, text="Process Name:", bg='#2b2b2b', fg='white').grid(row=2, column=0)
    tk.Label(add_game_window, text="Start Delay (seconds):", bg='#2b2b2b', fg='white').grid(row=3, column=0)
    tk.Label(add_game_window, text="Close Delay (seconds):", bg='#2b2b2b', fg='white').grid(row=4, column=0)

    game_id_entry = tk.Entry(add_game_window, bg='#404040', fg='white', insertbackground='white')
    title_entry = tk.Entry(add_game_window, bg='#404040', fg='white', insertbackground='white')
    name_entry = tk.Entry(add_game_window, bg='#404040', fg='white', insertbackground='white')
    start_delay_entry = tk.Entry(add_game_window, bg='#404040', fg='white', insertbackground='white')
    close_delay_entry = tk.Entry(add_game_window, bg='#404040', fg='white', insertbackground='white')

    game_id_entry.grid(row=0, column=1)
    title_entry.grid(row=1, column=1)
    name_entry.grid(row=2, column=1)
    start_delay_entry.grid(row=3, column=1)
    close_delay_entry.grid(row=4, column=1)


    def save_game():
        game_id = game_id_entry.get()
        title = title_entry.get()
        name = name_entry.get()
        start_delay = start_delay_entry.get()
        close_delay = close_delay_entry.get()

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

    tk.Button(add_game_window, text="Add Game", command=save_game, bg='#5a5a5a', fg='white').grid(row=5, columnspan=2)


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
    log_text.config(state=tk.NORMAL)
    log_text.insert(tk.END, message + "\n")
    log_text.config(state=tk.DISABLED)
    log_text.see(tk.END)


processes = [
    {"game_id": "2923300", "title": "Banana", "name": "Banana.exe", "start_delay": 10, "close_delay": 60},
    {"game_id": "2977660", "title": "Cats", "name": "Cats.exe", "start_delay": 10, "close_delay": 90},
    {"game_id": "3015610", "title": "Banana and Cucumber", "name": "Banana and Cucumber.exe", "start_delay": 10, "close_delay": 60},
    {"game_id": "2784840", "title": "Egg", "name": "Egg.exe", "start_delay": 10, "close_delay": 90}
]

pyautogui.PAUSE = 0.00001

farming = False

app = tk.Tk()
app.title("Steam Item Farmer")
app.configure(bg='#2b2b2b')


title_label = tk.Label(app, text="Games for farm:", font=("Helvetica", 14), bg='#2b2b2b', fg='white')
title_label.pack(pady=(10, 0))

frame = tk.Frame(app, bg='#2b2b2b')
frame.pack(pady=10)

listbox = tk.Listbox(frame, width=50, height=10, bg='#404040', fg='white')
listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

button_frame = tk.Frame(app, bg='#2b2b2b')
button_frame.pack(pady=10)

start_button = tk.Button(button_frame, text="Start Farming", command=lambda: threading.Thread(target=start_farming).start(), bg='#5a5a5a', fg='white')
start_button.pack(side=tk.LEFT, padx=5)

stop_button = tk.Button(button_frame, text="Stop Farming", command=stop_farming, bg='#5a5a5a', fg='white')
stop_button.pack(side=tk.LEFT, padx=5)

add_button = tk.Button(button_frame, text="Add Game", command=add_game, bg='#5a5a5a', fg='white')
add_button.pack(side=tk.LEFT, padx=5)

delete_button = tk.Button(button_frame, text="Delete Game", command=delete_game, bg='#5a5a5a', fg='white')
delete_button.pack(side=tk.LEFT, padx=5)

save_button = tk.Button(button_frame, text="Save Games", command=save_games, bg='#5a5a5a', fg='white')
save_button.pack(side=tk.LEFT, padx=5)

load_button = tk.Button(button_frame, text="Load Games", command=load_games, bg='#5a5a5a', fg='white')
load_button.pack(side=tk.LEFT, padx=5)

log_frame = tk.Frame(app, bg='#2b2b2b')
log_frame.pack(pady=10, fill=tk.BOTH, expand=True)

log_text = scrolledtext.ScrolledText(log_frame, wrap=tk.WORD, height=10, bg='#404040', fg='white', insertbackground='white')
log_text.pack(fill=tk.BOTH, expand=True)
log_text.config(state=tk.DISABLED)

update_processes_list()
app.mainloop()
