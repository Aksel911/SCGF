# [SCGF] Steam Clicker Games Farmer

![SCGF](/git-pics/main.png)

Программа автоматически запускает Steam игры. Находит центр окна программы и делает рандомное количество кликов (от 10 до 1000), далее закрывает игру и открывает следующую. Время сна перед повторением цикла от 5 до 15 секунд.

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
