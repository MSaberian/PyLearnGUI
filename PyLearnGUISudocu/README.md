# Sudoku

Sudoku is a logic-based, combinatorial number-placement puzzle. In classic Sudoku, the objective is to fill a 9 × 9 grid with digits so that each column, each row, and each of the nine 3 × 3 subgrids that compose the grid (also called "boxes", "blocks", or "regions") contain all of the digits from 1 to 9. The puzzle setter provides a partially completed grid, which for a well-posed puzzle has a single solution.

I use https://github.com/jeffsieu/py-sudoku library to make sudoku numbers. In this app user can set difficulty for new game or open file game.

![_difficulty](https://user-images.githubusercontent.com/43343453/224332673-e1c0b808-2133-424c-9cc0-770a24ce6c5f.png)


And this app have ability to dark them, pink and green them will be activated in the next version. I use https://github.com/5yutan5/PyQtDarkTheme library to dark them.

![_darkthem](https://user-images.githubusercontent.com/43343453/224332699-1439f19b-93bb-4a08-9501-25f0c2125bdf.png)


You can solve puzzle by "solve puzzle" from menu.

![_solved](https://user-images.githubusercontent.com/43343453/224332752-032c8b3e-c7ca-47fb-b5ca-d80d71e5edb6.png)


If you fill the puzzle correctly you will win.

![_win](https://user-images.githubusercontent.com/43343453/224332845-1ee49eae-b77c-470d-8246-d991689b8bab.png)


This app have about and help windows.

![_about](https://user-images.githubusercontent.com/43343453/224332794-c54fc033-4486-4b9f-85df-a37faf4dc871.png)


![_help](https://user-images.githubusercontent.com/43343453/224332819-988652b0-1e3b-43a3-beac-40333e2f93f8.png)


To create .exe file follow:

0. Offing Real-time protection system.

1. Install Pyinstaller by this command in terminal: pip install -U pyinstaller

2. Create .exe file by this command in terminal: pyinstaller main.py

3. Copy sudoku.png, win.png, about.png and Help.png to dist folder next to the main.exe file.

4. Run main.exe in dist folder




