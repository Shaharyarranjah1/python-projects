import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.scrolledtext import ScrolledText

def new_file():
    global current_file
    if text_area.get(1.0, tk.END).strip():
        if not ask_save_changes():
            return
    text_area.delete(1.0, tk.END)
    current_file = None
    root.title("Untitled - Notepad")

def open_file():
    global current_file
    if not ask_save_changes():
        return
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "r") as file:
            text_area.delete(1.0, tk.END)
            text_area.insert(1.0, file.read())
        current_file = file_path
        root.title(f"{current_file} - Notepad")

def save_file():
    global current_file
    if current_file:
        with open(current_file, "w") as file:
            file.write(text_area.get(1.0, tk.END).strip())
        root.title(f"{current_file} - Notepad")
    else:
        save_as()

def save_as():
    global current_file
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(text_area.get(1.0, tk.END).strip())
        current_file = file_path
        root.title(f"{current_file} - Notepad")

def ask_save_changes():
    if text_area.edit_modified():
        response = messagebox.askyesnocancel("Save Changes", "Do you want to save changes to your document?")
        if response:  # Yes
            save_file()
        return response is not None
    return True

def cut():
    text_area.event_generate("<<Cut>>")

def copy():
    text_area.event_generate("<<Copy>>")

def paste():
    text_area.event_generate("<<Paste>>")

def undo():
    text_area.event_generate("<<Undo>>")

def select_all():
    text_area.tag_add("sel", "1.0", tk.END)

# Create main application window
root = tk.Tk()
root.title("Untitled - Notepad")
root.geometry("800x600")

# Current file
current_file = None

# Create text area with scrollbar
text_area = ScrolledText(root, wrap=tk.WORD, undo=True, font=("Arial", 12))
text_area.pack(expand=1, fill=tk.BOTH)
text_area.focus_set()

# Create menu bar
menu_bar = tk.Menu(root)

# File menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As", command=save_as)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=lambda: root.destroy() if ask_save_changes() else None)
menu_bar.add_cascade(label="File", menu=file_menu)

# Edit menu
edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Undo", command=undo)
edit_menu.add_separator()
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)
edit_menu.add_separator()
edit_menu.add_command(label="Select All", command=select_all)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

# Help menu
help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=lambda: messagebox.showinfo("About Notepad", "Notepad in Python\nVersion 1.0"))
menu_bar.add_cascade(label="Help", menu=help_menu)

root.config(menu=menu_bar)

# Run application
root.protocol("WM_DELETE_WINDOW", lambda: root.destroy() if ask_save_changes() else None)
root.mainloop()
