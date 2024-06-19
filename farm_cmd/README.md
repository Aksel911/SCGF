[EZ_FARM.py](#EZ_FARM) | [FARM_STEAM](#FARM_STEAM) | [FARM](#FARM)

### EZ_FARM
# [EZ_FARM.py](https://github.com/Aksel911/SCGF/blob/main/farm_cmd/ez_farm.py)

EZ_FARM.py is a Python script designed to automate the process of launching and closing Steam games at regular intervals. This tool can be useful for various purposes such as farming in-game items or boosting game time for achievements. The bot ensures only one game runs at a time and waits a specified period between game launches.

## Features

-   **Sequential Game Launching**: Opens each game in the list one by one.
-   **Customizable Delays**: Configurable delays for both the start and close of each game.
-   **Automated Game Closing**: Uses `taskkill` to forcefully close games after a specified duration.
-   **Random Interval Between Cycles**: Waits between 3 to 3.5 hours before starting a new cycle.

## Installation

1.  **Clone the repository**:

    `git clone https://github.com/Aksel911/SCGF.git
    cd steam-game-rotation-bot` 
    
2.  **Install dependencies**: This script requires Python to be installed on your machine. You can download Python from [here](https://www.python.org/downloads/).
    

## Usage

1.  **Configure the game list**: Modify the `processes` list in `ez_farm.py` to include the games you want to rotate. Each game should have its Steam `game_id`, `title`, `name` (executable name), `start_delay`, and `close_delay`.
   
    
    `processes = [
        {"game_id": "2923300", "title": "Banana", "name": "Banana.exe", "start_delay": 10, "close_delay": 90},
        {"game_id": "2977660", "title": "Cats", "name": "Cats.exe", "start_delay": 10, "close_delay": 90},
        {"game_id": "3015610", "title": "Banana and Cucumber", "name": "Banana and Cucumber.exe", "start_delay": 10, "close_delay": 90},
        {"game_id": "2784840", "title": "Egg", "name": "Egg.exe", "start_delay": 10, "close_delay": 90},
        {"game_id": "2996990", "title": "Flaggenspiel", "name": "Flaggenspiel.exe", "start_delay": 10, "close_delay": 90}
    ]` 
    
2.  **Run the script**: Execute the script using Python.
    
    `python ez_farm.py` 
    

## How It Works

1.  The script opens each game in the list using the Steam protocol (`steam://rungameid/`).
2.  It waits for the specified `start_delay` before moving on.
3.  After the `close_delay`, it forcefully closes the game using the `taskkill` command.
4.  The script waits for a random interval between 3 to 3.5 hours before starting the next cycle.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements

-   Steam Protocol Documentation







#
#
#






### FARM_STEAM
# [FARM_STEAM.py](https://github.com/Aksel911/SCGF/blob/main/farm_cmd/farm_steam.py)


FARM_STEAM.py is a Python script designed to automate interactions with Steam games by simulating clicks at the center of the game window. This tool is useful for various tasks such as in-game farming, botting, or testing. The bot runs games sequentially, performs a random number of clicks, and then closes the game after a specified duration.

## Features

-   **Sequential Game Management**: Launches each game one at a time.
-   **Random Clicks**: Simulates a random number of clicks (between 1 and 1000) at the center of the game window.
-   **Customizable Delays**: Allows setting specific delays for starting clicks and closing each game.
-   **Automated Game Closing**: Uses `psutil` to forcefully close the game process after the specified duration.

## Installation

1.  **Clone the repository**:

    `git clone https://github.com/Aksel911/SCGF.git
    cd steam-game-click-bot` 
    
2.  **Install dependencies**: This script requires Python and several libraries. Install the dependencies using `pip`:

    `pip install psutil pyautogui pygetwindow` 
    

## Usage

1.  **Configure the game list**: Modify the `processes` list in `farm_steam.py` to include the games you want to automate. Each game should have its Steam `game_id`, `title`, `name` (executable name), `start_delay`, and `close_delay`.
    
    
    `processes = [
        {"game_id": "2923300", "title": "Banana", "name": "Banana.exe", "start_delay": 10, "close_delay": 60},
        {"game_id": "2977660", "title": "Cats", "name": "Cats.exe", "start_delay": 10, "close_delay": 90},
        {"game_id": "3015610", "title": "Banana and Cucumber", "name": "Banana and Cucumber.exe", "start_delay": 10, "close_delay": 60},
        {"game_id": "2784840", "title": "Egg", "name": "Egg.exe", "start_delay": 10, "close_delay": 90}
    ]` 
    
2.  **Run the script**: Execute the script using Python.
    
    `python farm_steam.py` 
    

## How It Works

1.  **Game Launch**: The script opens each game using the Steam protocol (`steam://rungameid/`).
2.  **Simulated Clicks**: After the `start_delay`, it finds the game window and simulates a random number of clicks at the center.
3.  **Game Closing**: After the `close_delay`, it forcefully closes the game using `psutil`.
4.  **Looping**: The script waits for a short interval before starting the next loop.

## Example Configuration

Here is an example configuration of the game list:

`processes = [
    {"game_id": "2923300", "title": "Banana", "name": "Banana.exe", "start_delay": 10, "close_delay": 60},
    {"game_id": "2977660", "title": "Cats", "name": "Cats.exe", "start_delay": 10, "close_delay": 90},
    {"game_id": "3015610", "title": "Banana and Cucumber", "name": "Banana and Cucumber.exe", "start_delay": 10, "close_delay": 60},
    {"game_id": "2784840", "title": "Egg", "name": "Egg.exe", "start_delay": 10, "close_delay": 90}
]` 

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements

-   Steam Protocol Documentation
-   [pygetwindow Documentation](https://github.com/asweigart/pygetwindow)
-   [pyautogui Documentation](https://pyautogui.readthedocs.io/en/latest/)
-   [psutil Documentation](https://psutil.readthedocs.io/en/latest/)






#
#
#




### FARM
# [FARM.py](https://github.com/Aksel911/SCGF/blob/main/farm_cmd/farm.py)


Local Game Click Bot is a Python script designed to automate interactions with local game executables by simulating clicks at the center of the game window. This tool is useful for various tasks such as in-game farming, botting, or testing. The bot runs games sequentially, performs a random number of clicks, and then closes the game after a specified duration.

## Features

-   **Sequential Game Management**: Launches each game one at a time from a specified path.
-   **Random Clicks**: Simulates a random number of clicks (between 1 and 1000) at the center of the game window.
-   **Customizable Delays**: Allows setting specific delays for starting clicks and closing each game.
-   **Automated Game Closing**: Uses `psutil` to forcefully close the game process after the specified duration.

## Installation

1.  **Clone the repository**:
    
    `git clone https://github.com/Aksel911/SCGF.git
    cd local-game-click-bot` 
    
2.  **Install dependencies**: This script requires Python and several libraries. Install the dependencies using `pip`:
    
    
    `pip install psutil pyautogui pygetwindow` 
    

## Usage

1.  **Configure the game list**: Modify the `processes` list in `main.py` to include the games you want to automate. Each game should have its path, `title`, `name` (executable name), `start_delay`, and `close_delay`.
    
    `steam_path = r"C:\Program Files (x86)\Steam\steamapps\common"
    processes = [
        {"path": rf"{steam_path}\Banana\Banana.exe", "title": "Banana", "name": "Banana.exe", "start_delay": 10, "close_delay": 60},
        {"path": rf"{steam_path}\Cats\Cats.exe", "title": "Cats", "name": "Cats.exe", "start_delay": 10, "close_delay": 90},
        {"path": rf"{steam_path}\Cucumber\Banana and Cucumber.exe", "title": "Banana and Cucumber", "name": "Banana and Cucumber.exe", "start_delay": 10, "close_delay": 60},
        {"path": rf"{steam_path}\EGG\Egg.exe", "title": "Egg", "name": "Egg.exe", "start_delay": 10, "close_delay": 90}
    ]` 
    
2.  **Run the script**: Execute the script using Python.
    
    
    `python main.py` 
    

## How It Works

1.  **Game Launch**: The script opens each game using the provided executable path.
2.  **Simulated Clicks**: After the `start_delay`, it finds the game window and simulates a random number of clicks at the center.
3.  **Game Closing**: After the `close_delay`, it forcefully closes the game using `psutil`.
4.  **Looping**: The script waits for a short interval before starting the next loop.

## Example Configuration

Here is an example configuration of the game list:

`steam_path = r"C:\Program Files (x86)\Steam\steamapps\common"
processes = [
    {"path": rf"{steam_path}\Banana\Banana.exe", "title": "Banana", "name": "Banana.exe", "start_delay": 10, "close_delay": 60},
    {"path": rf"{steam_path}\Cats\Cats.exe", "title": "Cats", "name": "Cats.exe", "start_delay": 10, "close_delay": 90},
    {"path": rf"{steam_path}\Cucumber\Banana and Cucumber.exe", "title": "Banana and Cucumber", "name": "Banana and Cucumber.exe", "start_delay": 10, "close_delay": 60},
    {"path": rf"{steam_path}\EGG\Egg.exe", "title": "Egg", "name": "Egg.exe", "start_delay": 10, "close_delay": 90}
]` 

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements

-   [pygetwindow Documentation](https://github.com/asweigart/pygetwindow)
-   [pyautogui Documentation](https://pyautogui.readthedocs.io/en/latest/)
-   [psutil Documentation](https://psutil.readthedocs.io/en/latest/)