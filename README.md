# Tic-Tac-Toe

Three implementations of Tic-Tac-Toe — GUI (Python/Kivy), CLI (Python), and systems-level (C).

## Versions

### GUI — `tic_tac_toe_gui.py` (Kivy + Minimax AI)
Full graphical interface with two modes:
- **User vs Friend** — local two-player
- **User vs AI** — unbeatable minimax AI

```bash
pip install kivy
python tic_tac_toe_gui.py
```

### CLI — `tic_tac_toe_cli.py` (Python)
Simple terminal-based two-player game with board display and win/draw detection.

```bash
python tic_tac_toe_cli.py
```

### C — `tic_tac_toe.c`
Terminal implementation in C.

```bash
gcc tic_tac_toe.c -o ttt
./ttt
```

## Stack

`Python` · `Kivy` · `Minimax algorithm` · `C`
