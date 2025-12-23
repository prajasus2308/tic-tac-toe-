import tkinter as tk
from tkinter import messagebox

# Initialize main window
root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("400x400")

# Game variables
current_player = "X"
buttons = [[None for _ in range(3)] for _ in range(3)]

# Colors for glowing effect
colors = ["#ffcccc", "#ff9999", "#ff6666", "#ff9999"]
color_index = 0

def glow_background():
    global color_index
    root.configure(bg=colors[color_index])
    color_index = (color_index + 1) % len(colors)
    root.after(500, glow_background)  # change every 500ms

def check_winner():
    for row in range(3):
        if buttons[row][0]["text"] == buttons[row][1]["text"] == buttons[row][2]["text"] != "":
            return True
    for col in range(3):
        if buttons[0][col]["text"] == buttons[1][col]["text"] == buttons[2][col]["text"] != "":
            return True
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return True
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return True
    return False

def check_draw():
    for row in range(3):
        for col in range(3):
            if buttons[row][col]["text"] == "":
                return False
    return True

def on_click(row, col):
    global current_player
    if buttons[row][col]["text"] == "":
        buttons[row][col]["text"] = current_player
        if check_winner():
            messagebox.showinfo("Game Over", f"Player {current_player} wins!")
            reset_game()
        elif check_draw():
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_game()
        else:
            current_player = "O" if current_player == "X" else "X"

def reset_game():
    global current_player
    current_player = "X"
    for row in range(3):
        for col in range(3):
            buttons[row][col]["text"] = ""

# Create buttons
for row in range(3):
    for col in range(3):
        buttons[row][col] = tk.Button(root, text="", font=("Arial", 24), width=6, height=3,
                                      bg="white", command=lambda r=row, c=col: on_click(r, c))
        buttons[row][col].grid(row=row, column=col, padx=5, pady=5)

# Start glowing background
glow_background()


root.mainloop()
