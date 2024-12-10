import tkinter as tk
import secrets
import string
import pyperclip

# Password generation function
def generate_password(length=12):
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    symbols = string.punctuation

    if length < 4:
        length = 4

    password = [
        secrets.choice(uppercase),
        secrets.choice(lowercase),
        secrets.choice(digits),
        secrets.choice(symbols)
    ]

    all_chars = uppercase + lowercase + digits + symbols

    for _ in range(length - 4):
        password.append(secrets.choice(all_chars))

    secrets.SystemRandom().shuffle(password)
    return ''.join(password)

# Function to handle password generation and display
def generate_and_display():
    try:
        pwd_length = int(length_entry.get())
        if pwd_length < 0:
            pwd_length = 12
    except ValueError:
        pwd_length = 12

    pwd = generate_password(pwd_length)
    password_label.config(text=pwd)

# Function to copy password to clipboard
def copy_to_clipboard():
    pwd = password_label.cget("text")
    pyperclip.copy(pwd)
    copy_label.config(text="Copied!", fg="green")

# Create the main window
root = tk.Tk()
root.title("Password Generator")
root.resizable(False, False)

# Create and place widgets
tk.Label(root, text="Enter password length:").grid(row=0, column=0, padx=10, pady=5)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, padx=10, pady=5)
length_entry.insert(0, "12")  # Default length

generate_button = tk.Button(root, text="Generate Password", command=generate_and_display)
generate_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

password_label = tk.Label(root, text="", wraplength=300, font=("Helvetica", 14))
password_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

copy_label = tk.Label(root, text="", fg="green")
copy_label.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

# Run the main event loop
root.mainloop()