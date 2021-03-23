# Renamer
## A Python application made in Tinker


**Renamer** lets you select files that you want to rename chronologically (starting from 1, ..., up to how many files you supplied)
_Example:_ Suppose you download multiple pictures at once, that are names something like 20210903_193950.jpg. Instead of renaming, let's say 30 of these pictures, manually, **Renamer** will help you achieve this is only 2 seconds.

## Requirements
1. Python 3.x ([How to install]) (https://www.python.org/downloads/)
2. Pip (Command in Terminal: `python get-pip.py`) 
3. Pyinstaller (Command in Terminal: `pip install pyinstaller`)

## How to install
Position yourself in the folder where _app.py_ is and run a command: `pyinstaller --onedir --windowed app.py`
This should generate 2 new folders and you will find an **app.exe** file in _dist/app/_ folder.

# How to use
Click on the button **Select files** and select files that you would like to rename (you can select multiple files at once).
After that, click on the button **Rename files** and this will automatically rename files and place them in the application folder.
