import tkinter as tk
from tkinter import ttk, messagebox
import random
import json
from pathlib import Path

# ----- load quotes from JSON -----
APP_DIR = Path(__file__).resolve().parent
DATA_FILE = APP_DIR / "data" / "quotes.json"

try:
    with DATA_FILE.open("r", encoding="utf-8") as f:
        data = json.load(f)
    quotes = data["quotes"]  # expecting a list of strings
except Exception as e:
    messagebox.showwarning(
        "Quotes not found",
        f"Could not load {DATA_FILE}.\nReason: {e}\n\nFalling back to a tiny built-in list."
    )
    quotes = [
        "Do. Or do not. There is no try. — Yoda",
        "With great power comes great responsibility. — Uncle Ben",
    ]

# ----- GUI -----
root = tk.Tk()
root.title("Fun Hub")
root.geometry("600x400")
root.minsize(520, 340)
root.configure(bg="#f9e6f0")  # pale pink background

# Styles
style = ttk.Style()
style.theme_use("clam")
style.configure("TFrame", background="#f9e6f0")
style.configure("TLabel", background="#f9e6f0", foreground="#5f4b8b", font=("Arial Rounded MT Bold", 14))
style.configure("TButton", background="#dec7e0", foreground="#3b1f47", font=("Arial Rounded MT Bold", 12))
style.map("TButton", background=[("active", "#e7d2ea")])

# Content container
content = ttk.Frame(root, style="TFrame")
content.pack(fill="both", expand=True, padx=24, pady=24)

# Notebook
notebook = ttk.Notebook(content)
notebook.pack(fill="both", expand=True)

# --- Quote Guessr tab
quote_tab = ttk.Frame(notebook, style="TFrame")
notebook.add(quote_tab, text="Quote Guessr")

# pastel “card” container
card = tk.Frame(
    quote_tab,
    bg="#f7ecf3",
    highlightbackground="#e7d2ea",
    highlightthickness=2,
    bd=0
)
card.pack(padx=24, pady=24, fill="both", expand=True)

# inner padding
inner = tk.Frame(card, bg="#f7ecf3")
inner.pack(padx=18, pady=18, fill="both", expand=True)

def show_random_quote():
    quote_label.config(text=random.choice(quotes))

title_label = ttk.Label(
    inner,
    text="Welcome to Quote Guessr!",
    style="TLabel",
    font=("Arial Rounded MT Bold", 18)
)
title_label.pack(pady=(8, 6))

# soft divider
divider = tk.Canvas(inner, height=2, bd=0, highlightthickness=0, bg="#f7ecf3")
divider.pack(fill="x", padx=4, pady=(0, 12))
divider.create_line(0, 1, 1000, 1, fill="#e0cfe6")

quote_label = ttk.Label(
    inner,
    text="",
    style="TLabel",
    wraplength=520,
    justify="center",
    font=("Arial", 13)
)
quote_label.pack(pady=8)

quote_button = ttk.Button(
    inner,
    text="Show Random Quote",
    command=show_random_quote,
    style="TButton"
)
quote_button.pack(pady=(10, 4))

root.mainloop()
