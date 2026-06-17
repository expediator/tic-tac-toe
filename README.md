# ✕ Tic-Tac-Toe — Three Implementations

Three versions of Tic-Tac-Toe in one repo: a browser game with unbeatable AI, a Python CLI, and a C implementation.

**Play:** [expediator.github.io/tic-tac-toe](https://expediator.github.io/tic-tac-toe/) &nbsp;·&nbsp; **Portfolio:** [expediator.github.io/resume](https://expediator.github.io/resume/)

---

## Versions

### 1. Browser (JavaScript) — deployed at the link above
- **vs AI** mode: minimax algorithm — the AI is mathematically unbeatable (always wins or draws)
- **vs Friend** mode: two players on the same screen
- Dark neon theme, animated win/draw detection, score tracking
- No install — open the URL

### 2. Python CLI
```bash
python tictactoe.py
```
Terminal-based, plays against a minimax AI.

### 3. C Implementation
```bash
gcc tictactoe.c -o tictactoe
./tictactoe
```
Systems-level implementation, shows understanding of memory management and pointers.

## How Minimax Works

Minimax is a recursive algorithm that:
1. Tries every possible move on the board
2. Scores each outcome: win = +10, loss = -10, draw = 0
3. The AI picks the move that maximizes its own score (assuming the human plays optimally)
4. Result: the AI never makes a mistake — the best a human can do is draw

With alpha-beta pruning added, the search tree is cut down significantly (though unnecessary for a 3×3 board).

## Files

```
tic-tac-toe/
├── index.html       ← Browser game (deployed to GitHub Pages)
├── tictactoe.py     ← Python CLI version
├── tictactoe.c      ← C implementation
└── README.md
```
