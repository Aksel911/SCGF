[🇺🇸](#english-version) | [🇷🇺](#russian-version)

### English version
# [SCGF] Steam Clicker Games Farmer

![SCGF](/git-pics/main.png)

The program automatically launches Steam games. Finds the center of the program window and patches clicks in all 4 pre-installed games (Banana, Cucumber, Cats, Egg) from 1 to 9999999, then makes a random number of clicks (from 10 to 1000), then closes the game and opens the next one. Sleep time before repeating the cycle is from 5 to 15 seconds.

The repository contains the source code in the following forms:
 - [CMD](/farm_cmd)
 - - Execution via `.exe` variant ([farm.py](/farm_cmd/farm.py))
 - - Execution via `start steam://rungameid/` variant ([farm_steam.py](/farm_cmd/farm_steam.py))
 - [GUI](/farm_steam_gui)
 - - Old variant, without using ttkthemes ([farm_steam_gui.py](/farm_steam_gui/farm_steam_gui_without_ttk.py))
 - - Current variant of the program ([farm_steam_gui_withiut_ttk.py](/farm_steam_gui/farm_steam_gui.py))

## How to use the program:
The program loads with 4 games already automatically added:
 - [Banana](https://store.steampowered.com/app/2923300/Banana/)
 - [Banana and Cucumber](https://store.steampowered.com/app/3015610/Banana__Cucumber/)
 - [Cats](https://store.steampowered.com/app/2977660/Cats/)
 - [Egg](https://store.steampowered.com/app/2784840/Egg/)
 
 To start farming, click **Start Farming** button.
 To stop farming, click **Stop Farming** button.

If you wish to add a new game, click the **Add Game** button.

![Add Game](/git-pics/add_game.png)

A new window will appear, where you need to fill in:
- **Steam Game ID:** The game's ID on Steam. (You can find it by following the link to the game's page on Steam, for example: https://store.steampowered.com/app/2784840/Egg/ - the ID for the game Egg is 2784840)
- **Window Title:** The title of the game window. (For example: Egg)
- **Process Name:** The name of the game's process. (For example: Egg.exe)
- **Start Delay (second):** Do nothing for N seconds after starting the game.
- **Close Delay (seconds):** Close the game after N seconds after the random clicks have been made.
Then click **Add Game** button.

You can also remove a game from the list by clicking on it in the list and then clicking: **Delete Game** button.

To save the list of games, click **Save Games** button and then choose a suitable location and file name for you. The file will be saved in the format: **.json**

*Example .json file:*

    [{"game_id":  "2923300",  "title":  "Banana",  "name":  "Banana.exe",  "start_delay":  10,  "close_delay":  60},  {"game_id":  "2977660",  "title":  "Cats",  "name":  "Cats.exe",  "start_delay":  10,  "close_delay":  90},  {"game_id":  "3015610",  "title":  "Banana and Cucumber",  "name":  "Banana and Cucumber.exe",  "start_delay":  10,  "close_delay":  60},  {"game_id":  "2784840",  "title":  "Egg",  "name":  "Egg.exe",  "start_delay":  10,  "close_delay":  90}]

To load the list of games, click **Load Games** button and select the **.json** file previously saved by you.






### Russian version
# [SCGF] Steam Clicker Games Farmer

![SCGF](/git-pics/main.png)

Программа автоматически запускает Steam игры. Находит центр окна программы и патчит клики во всех 4-х предустановленных играх (Banana, Cucumber, Cats, Egg) от 1 до 9999999, далее делает рандомное количество кликов (от 10 до 1000), далее закрывает игру и открывает следующую. Время сна перед повторением цикла от 5 до 15 секунд.

В репозитории есть исходный код в виде:
 - [CMD](/farm_cmd)
 - - Вариант запуска через .exe ([farm.py](/farm_cmd/farm.py))
 - - Вариант запуска через `start steam://rungameid/` ([farm_steam.py](/farm_cmd/farm_steam.py))
 - [GUI](/farm_steam_gui)
 - - Старый вариант, без использования ttkthemes ([farm_steam_gui.py](/farm_steam_gui/farm_steam_gui_without_ttk.py))
 - - Актуальный вариант программы ([farm_steam_gui_withiut_ttk.py](/farm_steam_gui/farm_steam_gui.py))

## Как использовать программу:
Программа загружается с уже автоматически добавленными 4 играми:
 - [Banana](https://store.steampowered.com/app/2923300/Banana/)
 - [Banana and Cucumber](https://store.steampowered.com/app/3015610/Banana__Cucumber/)
 - [Cats](https://store.steampowered.com/app/2977660/Cats/)
 - [Egg](https://store.steampowered.com/app/2784840/Egg/)
 
 Для запуска фарминга нажать на кнопку: **Start Farming**.
 Для остановки фарминга нажать на кнопку: **Stop Farming**.

При желании можно добавить новую игру, нажав на кнопку: **Add Game**.

![Add Game](/git-pics/add_game.png)

Появится новое окно, в котором нужно заполнить:
- **Steam Game ID:** ID игры в Steam. (Можно получить узнав его по ссылке на страницу игры в Steam, например: https://store.steampowered.com/app/2784840/Egg/ - ID для игры Egg: 2784840
- **Window Title:** Название окна игры. (Например: Egg)
- **Process Name:** Название процесса игры. (Например: Egg.exe)
- **Start Delay (second):** Ничего не делает через N секунд после старта игры.
- **Close Delay (seconds):** Через сколько секунд закрыть игру после проделанных рандомных кликов.
Далее нажать на кнопку **Add Game**.

Так-же можно удалить игру из списка, необходимо кликнуть на нее в списке и далее нажать на кнопку: **Delete Game**.

Что бы сохранить список игр, необходимо нажать на кнопку: **Save Games** и далее выбрать любое подходящее для вас место и имя файла. Файл сохранится в формат: **.json**

*Пример файла:*

    [{"game_id":  "2923300",  "title":  "Banana",  "name":  "Banana.exe",  "start_delay":  10,  "close_delay":  60},  {"game_id":  "2977660",  "title":  "Cats",  "name":  "Cats.exe",  "start_delay":  10,  "close_delay":  90},  {"game_id":  "3015610",  "title":  "Banana and Cucumber",  "name":  "Banana and Cucumber.exe",  "start_delay":  10,  "close_delay":  60},  {"game_id":  "2784840",  "title":  "Egg",  "name":  "Egg.exe",  "start_delay":  10,  "close_delay":  90}]

Что бы загрузить список игр, необходимо нажать на кнопку: **Load Games** и выбрать заранее сохраненный вами **.json** файл.
