import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

# Password generation function
def generate_password():
    try:
        length = int(entry_length.get())
        if length <= 0:
            messagebox.showerror("Input Error", "Password length must be a positive integer.")
            return

        use_letters = var_letters.get()
        use_numbers = var_numbers.get()
        use_symbols = var_symbols.get()
        
        character_pool = ""
        if use_letters:
            character_pool += string.ascii_letters
        if use_numbers:
            character_pool += string.digits
        if use_symbols:
            character_pool += string.punctuation

        if not character_pool:
            messagebox.showerror("Input Error", "Select at least one character type.")
            return

        # Generate password
        password = ''.join(random.choice(character_pool) for _ in range(length))
        entry_password.delete(0, tk.END)
        entry_password.insert(0, password)
    except ValueError:
        messagebox.showerror("Input Error", "Invalid password length.")

# Copy to clipboard function
def copy_to_clipboard():
    password = entry_password.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

# GUI setup
app = tk.Tk()
app.title("Random Password Generator")

# Password Length
frame_length = tk.Frame(app)
frame_length.pack(pady=5)
label_length = tk.Label(frame_length, text="Password Length:")
label_length.pack(side=tk.LEFT)
entry_length = tk.Entry(frame_length, width=5)
entry_length.pack(side=tk.LEFT)

# Character Options
frame_options = tk.Frame(app)
frame_options.pack(pady=5)
var_letters = tk.BooleanVar(value=True)
var_numbers = tk.BooleanVar(value=True)
var_symbols = tk.BooleanVar(value=True)

check_letters = tk.Checkbutton(frame_options, text="Letters (A-Z, a-z)", variable=var_letters)
check_letters.pack(anchor='w')
check_numbers = tk.Checkbutton(frame_options, text="Numbers (0-9)", variable=var_numbers)
check_numbers.pack(anchor='w')
check_symbols = tk.Checkbutton(frame_options, text="Symbols (!@#$)", variable=var_symbols)
check_symbols.pack(anchor='w')

# Generate Button
button_generate = tk.Button(app, text="Generate Password", command=generate_password)
button_generate.pack(pady=10)

# Password Display
entry_password = tk.Entry(app, width=30)
entry_password.pack(pady=5)

# Copy to Clipboard Button
button_copy = tk.Button(app, text="Copy to Clipboard", command=copy_to_clipboard)
button_copy.pack(pady=5)

app.mainloop()
