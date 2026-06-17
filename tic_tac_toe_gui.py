from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
import math

class TicTacToe(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.game_mode = None
        self.board = [" "] * 9
        self.current_player = "X"
        self.buttons = []

        self.menu()

    # ---------------- MENU ----------------
    def menu(self):
        self.clear_widgets()
        self.add_widget(Label(text="Tic Tac Toe", font_size=40))
        self.add_widget(Button(text="User vs Friend", on_press=lambda x: self.start("FRIEND")))
        self.add_widget(Button(text="User vs AI", on_press=lambda x: self.start("AI")))

    def start(self, mode):
        self.game_mode = mode
        self.board = [" "] * 9
        self.current_player = "X"
        self.clear_widgets()

        grid = GridLayout(cols=3)
        self.buttons = []

        for i in range(9):
            btn = Button(font_size=40)
            btn.bind(on_press=lambda btn, i=i: self.click(i))
            self.buttons.append(btn)
            grid.add_widget(btn)

        self.add_widget(grid)

    # ---------------- GAME LOGIC ----------------
    def click(self, i):
        if self.board[i] == " ":
            self.move(i, self.current_player)

    def move(self, i, player):
        self.board[i] = player
        self.buttons[i].text = player

        if self.win(player):
            self.popup(f"{player} Wins!")
            return

        if " " not in self.board:
            self.popup("Draw!")
            return

        self.current_player = "O" if player == "X" else "X"

        if self.game_mode == "AI" and self.current_player == "O":
            self.ai_move()

    def win(self, p):
        w = [(0,1,2),(3,4,5),(6,7,8),
             (0,3,6),(1,4,7),(2,5,8),
             (0,4,8),(2,4,6)]
        return any(self.board[a]==self.board[b]==self.board[c]==p for a,b,c in w)

    # ---------------- AI ----------------
    def minimax(self, is_max):
        if self.win("O"):
            return 1
        if self.win("X"):
            return -1
        if " " not in self.board:
            return 0

        if is_max:
            best = -math.inf
            for i in range(9):
                if self.board[i] == " ":
                    self.board[i] = "O"
                    best = max(best, self.minimax(False))
                    self.board[i] = " "
            return best
        else:
            best = math.inf
            for i in range(9):
                if self.board[i] == " ":
                    self.board[i] = "X"
                    best = min(best, self.minimax(True))
                    self.board[i] = " "
            return best

    def ai_move(self):
        best_score = -math.inf
        move = 0
        for i in range(9):
            if self.board[i] == " ":
                self.board[i] = "O"
                score = self.minimax(False)
                self.board[i] = " "
                if score > best_score:
                    best_score = score
                    move = i
        self.move(move, "O")

    # ---------------- POPUP ----------------
    def popup(self, text):
        box = BoxLayout(orientation='vertical')
        box.add_widget(Label(text=text))
        btn = Button(text="Play Again")
        box.add_widget(btn)
        popup = Popup(title="Game Over", content=box, size_hint=(0.7,0.4))
        btn.bind(on_press=lambda x: (popup.dismiss(), self.menu()))
        popup.open()

class TicTacToeApp(App):
    def build(self):
        return TicTacToe()

if __name__ == "__main__":
    TicTacToeApp().run()
