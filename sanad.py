import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors vs Opponent")
        self.root.geometry("550x650")
        self.root.resizable(False, False)
        self.root.configure(bg="#1E1E2E")

        self.player_score = 0
        self.opponent_score = 0
        self.target_score = 3
        self.is_thinking = False
        self.choices = {
            "Rock": "🪨",
            "Paper": "📄",
            "Scissors": "✂️"
        }

        self.thinking_messages = [
            "Opponent is thinking...",
            "Opponent is choosing a move...",
            "Opponent is analyzing your strategy...",
            "Opponent is making a choice..."
        ]

        self.create_widgets()

    def create_widgets(self):
        title_label = tk.Label(
            self.root, 
            text="👤 You vs Opponent 👤", 
            font=("Helvetica", 22, "bold"), 
            fg="#F5E0DC", 
            bg="#1E1E2E",
            pady=20
        )
        title_label.pack()

        score_frame = tk.Frame(self.root, bg="#313244", bd=2, relief="groove")
        score_frame.pack(fill="x", padx=25, pady=10)

        self.score_label = tk.Label(
            score_frame, 
            text=f"You: {self.player_score}   |   Opponent: {self.opponent_score}", 
            font=("Helvetica", 18, "bold"), 
            fg="#A6E3A1", 
            bg="#313244",
            pady=15
        )
        self.score_label.pack()

        self.display_label = tk.Label(
            self.root, 
            text="Make your move when ready!", 
            font=("Helvetica", 16, "bold"), 
            fg="#CDD6F4", 
            bg="#1E1E2E",
            pady=20
        )
        self.display_label.pack()

        self.result_label = tk.Label(
            self.root, 
            text="", 
            font=("Helvetica", 18, "bold"), 
            fg="#FAB387", 
            bg="#1E1E2E",
            pady=10
        )
        self.result_label.pack()

        buttons_frame = tk.Frame(self.root, bg="#1E1E2E")
        buttons_frame.pack(pady=20)

        self.buttons = {}
        for choice, emoji in self.choices.items():
            btn = tk.Button(
                buttons_frame,
                text=f"{emoji}\n{choice}",
                font=("Helvetica", 14, "bold"),
                width=9,
                height=3,
                bg="#89B4FA",
                fg="#11111B",
                activebackground="#B4BEFE",
                cursor="hand2",
                command=lambda c=choice: self.start_turn(c)
            )
            btn.pack(side="left", padx=12)
            self.buttons[choice] = btn

        reset_btn = tk.Button(
            self.root,
            text="Reset Game 🔄",
            font=("Helvetica", 13, "bold"),
            bg="#F38BA8",
            fg="#11111B",
            cursor="hand2",
            command=self.reset_game
        )
        reset_btn.pack(side="bottom", pady=25)

    def start_turn(self, player_choice):
        if self.is_thinking or self.player_score >= self.target_score or self.opponent_score >= self.target_score:
            return

        self.is_thinking = True
        p_emoji = self.choices[player_choice]
        
        self.display_label.config(text=f"You chose: {player_choice} {p_emoji}")
        self.result_label.config(text=random.choice(self.thinking_messages), fg="#F9E2AF")

        self.root.after(1200, lambda: self.finish_turn(player_choice))

    def finish_turn(self, player_choice):
        opponent_choice = random.choice(list(self.choices.keys()))

        if player_choice == opponent_choice:
            res_text = "🤝 It's a Tie!"
            res_color = "#FAB387"
        elif (player_choice == "Rock" and opponent_choice == "Scissors") or \
             (player_choice == "Paper" and opponent_choice == "Rock") or \
             (player_choice == "Scissors" and opponent_choice == "Paper"):
            res_text = "🎉 You won this round!"
            res_color = "#A6E3A1"
            self.player_score += 1
        else:
            res_text = "💥 Opponent won this round!"
            res_color = "#F38BA8"
            self.opponent_score += 1

        p_emoji = self.choices[player_choice]
        o_emoji = self.choices[opponent_choice]
        
        self.display_label.config(text=f"You: {player_choice} {p_emoji}  🆚  Opponent: {opponent_choice} {o_emoji}")
        self.result_label.config(text=res_text, fg=res_color)
        self.score_label.config(text=f"You: {self.player_score}   |   Opponent: {self.opponent_score}")

        self.is_thinking = False
        self.check_game_over()

    def check_game_over(self):
        if self.player_score == self.target_score:
            messagebox.showinfo("Victory! 🏆", "Congratulations! You defeated your opponent!")
        elif self.opponent_score == self.target_score:
            messagebox.showwarning("Defeat! 👤", "Game Over! Your opponent won the match.")

    def reset_game(self):
        self.player_score = 0
        self.opponent_score = 0
        self.is_thinking = False
        self.score_label.config(text=f"You: {self.player_score}   |   Opponent: {self.opponent_score}")
        self.display_label.config(text="Make your move when ready!")
        self.result_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissorsApp(root)
    root.mainloop()