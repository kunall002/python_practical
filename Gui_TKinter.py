
import tkinter as tk
from tkinter import scrolledtext

root = tk.Tk()
root.title("Tkinter GUI Demo")

label = tk.Label(root, text="Enter some text:")
label.pack(pady=10)

entry = tk.Entry(root, width=40)
entry.pack(pady=5)

def display_text():
    user_input = entry.get()
    text_area.insert(tk.END, user_input + "\n")
    entry.delete(0, tk.END)

button = tk.Button(root, text="Display Text", command=display_text)
button.pack(pady=10)

text_area = scrolledtext.ScrolledText(root, width=40, height=10, wrap=tk.WORD)
text_area.pack(pady=10)

root.mainloop()
