import tkinter as tk
import random

# -------------------------
# GAME DATA
# -------------------------

point_U = 0
point_C = 0

games = ["paper", "sisser", "rock"]

win_game = {
    "paper": "rock",
    "sisser": "paper",
    "rock": "sisser"
}


# -------------------------
# FUNCTIONS
# -------------------------

def play(user):

    global point_U, point_C

    computer = random.choice(games)

    user_choice.config(text=user.upper())
    computer_choice.config(text=computer.upper())

    if user == computer:

        result.config(
            text="DRAW!",
            fg="#FFD166"
        )

    elif win_game[user] == computer:

        point_U += 1

        result.config(
            text="YOU WIN!",
            fg="#00FF99"
        )

    else:

        point_C += 1

        result.config(
            text="COMPUTER WINS!",
            fg="#FF4D6D"
        )

    user_score.config(text=str(point_U))
    computer_score.config(text=str(point_C))

    if point_U == 10:

        result.config(
            text="🏆 YOU WIN THE GAME!",
            fg="#00FF99"
        )

        disable_buttons()

    elif point_C == 10:

        result.config(
            text="💀 COMPUTER WON!",
            fg="#FF4D6D"
        )

        disable_buttons()


def disable_buttons():

    paper_button.config(state="disabled")
    sisser_button.config(state="disabled")
    rock_button.config(state="disabled")


def new_game():

    global point_U, point_C

    point_U = 0
    point_C = 0

    user_score.config(text="0")
    computer_score.config(text="0")

    user_choice.config(text="?")
    computer_choice.config(text="?")

    result.config(
        text="CHOOSE YOUR WEAPON",
        fg="#FFFFFF"
    )

    paper_button.config(state="normal")
    sisser_button.config(state="normal")
    rock_button.config(state="normal")


# -------------------------
# MAIN WINDOW
# -------------------------

window = tk.Tk()

window.title("Rock Paper Scissors")
window.geometry("900x650")
window.resizable(False, False)

window.configure(bg="#080B16")


# -------------------------
# TITLE
# -------------------------

title = tk.Label(
    window,
    text="ROCK • PAPER • SCISSORS",
    font=("Arial", 30, "bold"),
    fg="#FFFFFF",
    bg="#080B16"
)

title.pack(pady=(35, 5))


subtitle = tk.Label(
    window,
    text="FIRST TO 10 WINS",
    font=("Arial", 11, "bold"),
    fg="#00D9FF",
    bg="#080B16"
)

subtitle.pack()


# -------------------------
# SCORE FRAME
# -------------------------

score_frame = tk.Frame(
    window,
    bg="#111629"
)

score_frame.pack(
    pady=30,
    padx=100,
    fill="x"
)


# USER SCORE

user_frame = tk.Frame(
    score_frame,
    bg="#111629"
)

user_frame.pack(
    side="left",
    expand=True,
    pady=20
)

tk.Label(
    user_frame,
    text="YOU",
    font=("Arial", 15, "bold"),
    fg="#00D9FF",
    bg="#111629"
).pack()

user_score = tk.Label(
    user_frame,
    text="0",
    font=("Arial", 40, "bold"),
    fg="#FFFFFF",
    bg="#111629"
)

user_score.pack()


# VS

tk.Label(
    score_frame,
    text="VS",
    font=("Arial", 20, "bold"),
    fg="#777F9E",
    bg="#111629"
).pack(
    side="left",
    padx=30
)


# COMPUTER SCORE

computer_frame = tk.Frame(
    score_frame,
    bg="#111629"
)

computer_frame.pack(
    side="left",
    expand=True,
    pady=20
)

tk.Label(
    computer_frame,
    text="COMPUTER",
    font=("Arial", 15, "bold"),
    fg="#A56BFF",
    bg="#111629"
).pack()

computer_score = tk.Label(
    computer_frame,
    text="0",
    font=("Arial", 40, "bold"),
    fg="#FFFFFF",
    bg="#111629"
)

computer_score.pack()


# -------------------------
# BATTLE AREA
# -------------------------

battle = tk.Frame(
    window,
    bg="#080B16"
)

battle.pack(
    pady=10
)


# USER CHOICE

user_choice = tk.Label(
    battle,
    text="?",
    font=("Arial", 55, "bold"),
    fg="#00D9FF",
    bg="#080B16",
    width=8
)

user_choice.pack(
    side="left"
)


# RESULT
result = tk.Label(
    battle,
    text="CHOOSE YOUR WEAPON",
    font=("Arial", 16, "bold"),
    fg="#FFFFFF",
    bg="#080B16",
    width=22
)

result.pack(
    side="left"
)


# COMPUTER CHOICE

computer_choice = tk.Label(
    battle,
    text="?",
    font=("Arial", 55, "bold"),
    fg="#A56BFF",
    bg="#080B16",
    width=8
)

computer_choice.pack(
    side="left"
)


# -------------------------
# BUTTONS
# -------------------------

buttons = tk.Frame(
    window,
    bg="#080B16"
)

buttons.pack(pady=30)


paper_button = tk.Button(
    buttons,
    text="✋\nPAPER",
    font=("Arial", 15, "bold"),
    width=12,
    height=3,
    bg="#151B31",
    fg="#FFFFFF",
    activebackground="#00D9FF",
    activeforeground="#000000",
    relief="flat",
    command=lambda: play("paper")
)

paper_button.pack(
    side="left",
    padx=10
)


sisser_button = tk.Button(
    buttons,
    text="✌\nSCISSORS",
    font=("Arial", 15, "bold"),
    width=12,
    height=3,
    bg="#151B31",
    fg="#FFFFFF",
    activebackground="#A56BFF",
    activeforeground="#000000",
    relief="flat",
    command=lambda: play("sisser")
)

sisser_button.pack(
    side="left",
    padx=10
)


rock_button = tk.Button(
    buttons,
    text="✊\nROCK",
    font=("Arial", 15, "bold"),
    width=12,
    height=3,
    bg="#151B31",
    fg="#FFFFFF",
    activebackground="#FF4D6D",
    activeforeground="#000000",
    relief="flat",
    command=lambda: play("rock")
)

rock_button.pack(
    side="left",
    padx=10
)


# -------------------------
# NEW GAME
# -------------------------

new_game_button = tk.Button(
    window,
    text="↻  NEW GAME",
    font=("Arial", 11, "bold"),
    bg="#080B16",
    fg="#777F9E",
    activebackground="#080B16",
    activeforeground="#FFFFFF",
    relief="flat",
    command=new_game
)

new_game_button.pack()


# -------------------------
# START
# -------------------------

window.mainloop()
