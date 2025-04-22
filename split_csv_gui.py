import tkinter as tk
from tkinter import filedialog, messagebox
import csv
import os
import re
import sys
from textwrap import TextWrapper
import webbrowser
import random

csv.field_size_limit(sys.maxsize)

def sanitize_filename(filename):
    return re.sub(r'[<>:"/\\|?*]', '_', filename)

def wrap_text(text, width=80):
    wrapper = TextWrapper(width=width, break_long_words=True, break_on_hyphens=False)
    return '\n'.join(wrapper.wrap(text))

def split_csv(input_file, email_count, enhance=False):
    try:
        input_file = os.path.abspath(input_file)

        with open(input_file, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            headers = next(reader)

            output_dir = filedialog.askdirectory(title="Select or Create Folder for Saving Emails")
            if not output_dir:
                messagebox.showerror("Error", "No folder selected.")
                return

            for i, row in enumerate(reader):
                if i >= email_count:
                    break

                try:
                    email_details = []
                    for j in range(len(headers)):
                        field_value = row[j]
                        if headers[j].lower() == "body" and not enhance:
                            field_value = wrap_text(field_value)
                        # Handle wrapping long texts (like the body) with more than 10 words
                        elif len(field_value.split()) > 10:
                            field_value = '\n'.join(wrap_text(field_value, width=80).splitlines())
                        email_details.append(f"{headers[j]}: {field_value}")
                    
                    email_content = "\n".join(email_details)

                    if enhance:
                        email_content = email_content.replace("Subject:", "\033[1;34mSubject:\033[0m")
                        email_content = email_content.replace("Body:", "\033[1;32mBody:\033[0m")
                        email_content = wrap_text(email_content, width=12)

                    sender = row[0]
                    sender_sanitized = sanitize_filename(sender)
                    email_file_path = os.path.join(output_dir, f'{sender_sanitized}_{i+1}.txt')
                    with open(email_file_path, 'w', encoding='utf-8') as f:
                        f.write(email_content)

                except Exception as e:
                    print(f"Skipping email {i+1} due to error: {e}")

            messagebox.showinfo("Success", f"Processed {email_count} emails! ❄️")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if file_path:
        file_label.config(text=f"File: {file_path}")
        global selected_file
        selected_file = file_path
    else:
        messagebox.showerror("Error", "No file selected.")

def process_emails():
    try:
        count = int(email_count_entry.get())
        if count <= 0 or not selected_file:
            raise ValueError
        split_csv(selected_file, count)
    except:
        messagebox.showerror("Error", "Enter a valid number and select a file.")

def process_enhanced_emails():
    try:
        count = int(email_count_entry.get())
        if count <= 0 or not selected_file:
            raise ValueError
        split_csv(selected_file, count, enhance=True)
    except:
        messagebox.showerror("Error", "Enter a valid number and select a file.")

def enhance_selected_emails():
    try:
        email_files = filedialog.askopenfilenames(title="Select Emails", filetypes=[("Text Files", "*.txt")])
        if not email_files:
            messagebox.showerror("Error", "No files selected.")
            return

        for email_file in email_files:
            with open(email_file, 'r', encoding='utf-8') as f:
                content = f.read()

            content = content.replace("Subject:", "\033[1;34mSubject:\033[0m")
            content = content.replace("Body:", "\033[1;32mBody:\033[0m")
            content = wrap_text(content, width=12)

            new_file = os.path.splitext(email_file)[0] + "_enhanced.txt"
            with open(new_file, 'w', encoding='utf-8') as f:
                f.write(content)

        messagebox.showinfo("Success", "Emails enhanced.")

    except Exception as e:
        messagebox.showerror("Error", str(e))

def open_github():
    webbrowser.open("https://github.com/Iamfazi1/Portfolio")

def open_linkedin():
    webbrowser.open("https://www.linkedin.com/in/muhmmadfaizanshakir/")

def open_email():
    webbrowser.open("mailto:f.sgamar222@gmail.com")

# ❄️ Simulated Snowflake Animation
class Snowflake:
    def __init__(self, canvas, width, height):
        self.canvas = canvas
        self.x = random.randint(0, width)
        self.y = random.randint(-height, 0)
        self.size = random.randint(2, 5)
        self.speed = random.uniform(1, 3)
        self.oval = canvas.create_oval(self.x, self.y, self.x + self.size, self.y + self.size, fill="white", outline="white")

    def fall(self):
        self.y += self.speed
        self.canvas.move(self.oval, 0, self.speed)
        if self.y > self.canvas.winfo_height():
            self.canvas.coords(self.oval, self.x, -5, self.x + self.size, self.size)
            self.y = -5

def animate_snowflakes():
    for flake in snowflakes:
        flake.fall()
    root.after(50, animate_snowflakes)

# 🎨 GUI Setup
root = tk.Tk()
root.title("Email Splitter & Enhancer by Faizan")
root.geometry("720x600")
root.resizable(False, False)

# Canvas for snowfall background
canvas = tk.Canvas(root, width=720, height=600, bg="#0a0a2a", highlightthickness=0)
canvas.pack(fill="both", expand=True)

# Snowflake animation
snowflakes = [Snowflake(canvas, 720, 600) for _ in range(80)]
animate_snowflakes()

# Widgets
title = tk.Label(root, text="CSV Email Splitter & Enhancer", font=("Helvetica", 18, "bold"), bg="#0a0a2a", fg="white")
canvas.create_window(360, 30, window=title)

browse_button = tk.Button(root, text="Browse CSV File", font=("Helvetica", 12), bg="#4CAF50", fg="white", command=browse_file)
canvas.create_window(360, 90, window=browse_button)

file_label = tk.Label(root, text="No file selected", font=("Helvetica", 10), bg="#0a0a2a", fg="white")
canvas.create_window(360, 130, window=file_label)

email_count_entry = tk.Entry(root, font=("Helvetica", 14), width=10)
canvas.create_window(360, 180, window=email_count_entry)

entry_label = tk.Label(root, text="Enter number of emails:", font=("Helvetica", 12), bg="#0a0a2a", fg="white")
canvas.create_window(360, 160, window=entry_label)

split_button = tk.Button(root, text="Split Emails", font=("Helvetica", 12), bg="#2196F3", fg="white", command=process_emails)
canvas.create_window(360, 230, window=split_button)

enhanced_split_button = tk.Button(root, text="Enhanced Split", font=("Helvetica", 12), bg="#673AB7", fg="white", command=process_enhanced_emails)
canvas.create_window(360, 270, window=enhanced_split_button)

enhance_button = tk.Button(root, text="Enhance Existing Emails", font=("Helvetica", 12), bg="#E91E63", fg="white", command=enhance_selected_emails)
canvas.create_window(360, 310, window=enhance_button)

# Footer Buttons
github_button = tk.Button(root, text="GitHub Portfolio", font=("Helvetica", 10), bg="#2E7D32", fg="white", command=open_github)
canvas.create_window(180, 560, window=github_button)

linkedin_button = tk.Button(root, text="LinkedIn Profile", font=("Helvetica", 10), bg="#0e76a8", fg="white", command=open_linkedin)
canvas.create_window(360, 560, window=linkedin_button)

email_button = tk.Button(root, text="Email Me", font=("Helvetica", 10), bg="#D84315", fg="white", command=open_email)
canvas.create_window(540, 560, window=email_button)

note = tk.Label(root, text="❄️ If any issue occurs, feel free to email me at f.sgamar222@gmail.com ❄️",
                font=("Helvetica", 9), bg="#0a0a2a", fg="white")
canvas.create_window(360, 520, window=note)

root.mainloop()
