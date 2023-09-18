import os
import tkinter as tk
from tkinter import ttk
from scan import scan_and_build_tree
from user_interface import create_ui


def customize_ttk_style():
    style = ttk.Style()
    style.configure("TButton",
                    background="lightgray",
                    foreground="blue",
                    padding=(10, 5))  # Adjust padding as needed
    style.configure("TLabel", foreground="black", background="white")
    style.map("TButton",
              background=[("active", "lightblue")])  # Change button color when clicked


def main():
    root = tk.Tk()
    root.title("File Explorer")

    customize_ttk_style()  # Apply custom styles to ttk widgets

    root_directory = os.path.expanduser("~")
    # Determine the root directory based on the platform
    if os.name == "posix":  # Linux or macOS
        root_directory = "/home"  # Start scanning from the home directory
    elif os.name == "nt":  # Windows
        root_directory = "C:\\"  # Start scanning from the C: drive (adjust as needed)

    root_node = scan_and_build_tree(root_directory)

    create_ui(root, root_node)  # Pass the root_node to create_ui

    root.mainloop()


if __name__ == "__main__":
    main()
