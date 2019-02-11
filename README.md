# scoreboardmelee
Score Board Melee is a small GUI app to help in updating OBS layout. It is specifically designed for Super Smash Bros. Melee 1 vs. 1 tournament sets but can be modified for other games and situations as well. Supports player names, integer scores, match label, miscellaneous info (these are all saved in text files) and character stock icons with different colours (saved as images). The stock icons are not freely available and need to be obtained separately.

## Prerequisites
This is a Python 3 project which depends on the module tkinter

## How to run
In Linux, just use
```
python3 scoreboard.py
```
First, I suggest you set a directory for the text files and stock icons. If they already exist in the directory, they are loaded. In OBS (or similar software) you need to set the text labels and images to be read from the corresponding files.

## License
This project is licensed under the MIT License. See [LICENSE.md](LICENSE.md).
