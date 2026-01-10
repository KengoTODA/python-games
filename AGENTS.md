# Repository Guidelines

## Project Structure & Module Organization
This repo has small Python games. The code files are in the top folder:
- `bingo.py` is a bingo game you play in the terminal.
- `pingpong.py` is a simple ping-pong game with a moving ball.
- `test_bingo.py` has tests for bingo.
There is no `src/` folder, so new game files should also live at the top level.

## Build, Test, and Development Commands
- `python bingo.py` starts the bingo game.
- `pgzrun pingpong.py` starts the ping-pong game (uses Pygame Zero).
- `python -m pytest` runs all tests.
- `python -m pip install pytest pgzero` installs tools if your computer does not have them.

## Coding Style & Naming Conventions
Keep code easy to read for kids:
- Use 4 spaces for indentation.
- Use simple, clear names like `create_board` and `picked_numbers`.
- Use ALL CAPS for fixed values like `PICKED`, `WIDTH`, and `HEIGHT`.
- Prefer short functions that do one job.
- Add small comments only when the code is not obvious.

## Testing Guidelines
Tests use `pytest`. Test files should be named like `test_*.py`. Test functions should be named like `test_*`. Tests should check rules that always stay the same (for example, the bingo center is always picked). Do not make tests that need key presses or windows.

## Commit & Pull Request Guidelines
There is no strict commit style here. Use short, clear messages like “Add test for bingo board”. In a pull request, explain what changed, say if you ran tests, and add a screenshot if you change how the game looks.

## Configuration & Dependencies
`pingpong.py` needs Pygame Zero (`pgzrun`). If you add a new tool or library, write the install command and how to run it in this file.
