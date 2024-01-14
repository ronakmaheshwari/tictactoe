import tkinter as tk
from tkinter import messagebox

class TicTacToeBoard(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Tic-Tac-Toe")
        self.geometry("300x300")

        self.current_player = "X"
        self.board = [""] * 9

        self.create_widgets()

    def create_widgets(self):
        self.buttons = []
        for i in range(9):
            button = tk.Button(self, text="", font=("Arial", 20), width=3, height=1, command=lambda i=i: self.on_click(i))
            button.grid(row=i // 3, column=i % 3, padx=5, pady=5, sticky="nsew")
            self.buttons.append(button)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

    def on_click(self, index):
        if self.board[index] == "":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player, state=tk.DISABLED, disabledforeground="black")

            if self.check_winner():
                messagebox.showinfo("Victory", f"Player {self.current_player} wins!")
                self.reset_board()
            elif "" not in self.board:
                messagebox.showinfo("Tie")
                self.reset_board()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
            (0, 4, 8), (2, 4, 6)              # Diagonals
        ]

        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != "":
                for i in combo:
                    self.buttons[i].config(bg="lightgreen")
                return True

        return False

    def reset_board(self):
        for i in range(9):
            self.buttons[i].config(text="", state=tk.NORMAL, bg=self.cget("bg"))
            self.board[i] = ""
        self.current_player = "X"

if __name__ == "__main__":
    app = TicTacToeBoard()
    app.mainloop()
