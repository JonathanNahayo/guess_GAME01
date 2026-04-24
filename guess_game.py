import random
import tkinter as tk
from tkinter import messagebox


class GuessGameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.root.geometry("420x350")
        self.root.configure(bg="#1e1e2f")

        # Game variables
        self.round_number = 1
        self.min_val = 1
        self.max_val = 100
        self.max_attempts = 7

        self.secret_number = 0
        self.attempts_left = 0

        self.create_widgets()
        self.start_game()

    # ================= UI =================
    def create_widgets(self):
        tk.Label(
            self.root,
            text="🎯 Guess The Number",
            font=("Arial", 16, "bold"),
            bg="#1e1e2f",
            fg="white"
        ).pack(pady=10)

        self.info_label = tk.Label(self.root, bg="#1e1e2f", fg="white")
        self.info_label.pack()

        self.entry = tk.Entry(self.root, font=("Arial", 14), justify="center")
        self.entry.pack(pady=10)

        tk.Button(
            self.root,
            text="Submit Guess",
            command=self.check_guess,
            bg="#2196F3",
            fg="white",
            width=15
        ).pack(pady=5)

        self.result_label = tk.Label(
            self.root,
            text="",
            bg="#1e1e2f",
            fg="white",
            font=("Arial", 12)
        )
        self.result_label.pack(pady=5)

        self.attempts_label = tk.Label(
            self.root,
            text="",
            bg="#1e1e2f",
            fg="white"
        )
        self.attempts_label.pack(pady=5)

        # Continue frame (hidden by default)
        self.continue_frame = tk.Frame(self.root, bg="#1e1e2f")

        self.continue_label = tk.Label(
            self.continue_frame,
            text="Do you want to continue?",
            bg="#1e1e2f",
            fg="white"
        )
        self.continue_label.pack(pady=5)

        tk.Button(
            self.continue_frame,
            text="Yes",
            command=self.next_round,
            bg="#4CAF50",
            fg="white",
            width=10
        ).pack(side="left", padx=10)

        tk.Button(
            self.continue_frame,
            text="No",
            command=self.exit_game,
            bg="#F44336",
            fg="white",
            width=10
        ).pack(side="right", padx=10)

    # ================= START GAME =================
    def start_game(self):
        self.secret_number = random.randint(self.min_val, self.max_val)
        self.attempts_left = self.max_attempts

        self.info_label.config(
            text=f"Round {self.round_number}: Guess between {self.min_val}-{self.max_val}"
        )
        self.result_label.config(text="")
        self.update_attempts()
        self.entry.delete(0, tk.END)

        # hide continue buttons
        self.continue_frame.pack_forget()

    # ================= UPDATE ATTEMPTS =================
    def update_attempts(self):
        self.attempts_label.config(
            text=f"Attempts left: {self.attempts_left}"
        )

    # ================= CHECK GUESS =================
    def check_guess(self):
        try:
            guess = int(self.entry.get())

            if guess < self.min_val or guess > self.max_val:
                messagebox.showwarning("Error", "Number out of range!")
                return

            self.attempts_left -= 1

            if guess < self.secret_number:
                self.result_label.config(text="Too low 📉")
            elif guess > self.secret_number:
                self.result_label.config(text="Too high 📈")
            else:
                messagebox.showinfo(
                    "Correct 🎉",
                    f"You won in {self.max_attempts - self.attempts_left} attempts!"
                )
                self.show_continue()
                return

            self.update_attempts()

            if self.attempts_left == 0:
                messagebox.showerror(
                    "Game Over ❌",
                    f"The correct number was {self.secret_number}"
                )
                self.show_continue()

        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter a valid number!")

    # ================= CONTINUE OPTION =================
    def show_continue(self):
        self.continue_frame.pack(pady=10)

    def next_round(self):
        self.round_number += 1
        self.max_val += 50  # difficulty increases
        self.start_game()

    def exit_game(self):
        self.root.destroy()


# ================= RUN APP =================
if __name__ == "__main__":
    root = tk.Tk()
    app = GuessGameGUI(root)
    root.mainloop()