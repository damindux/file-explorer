import os
import tkinter as tk
from tkinter import simpledialog, messagebox

current_directory = [os.getcwd()]
current_node = None


def populate_listbox(listbox, folder):
    listbox.delete(0, tk.END)

    if folder != "/":
        listbox.insert(tk.END, "..")

    items = os.listdir(folder)
    for item in items:
        item_path = os.path.join(folder, item)
        # Check if the item is a directory and not hidden
        if os.path.isdir(item_path) and not item.startswith("."):
            listbox.insert(tk.END, item)
        # Check if the item is a file and not hidden
        elif os.path.isfile(item_path) and not item.startswith("."):
            listbox.insert(tk.END, item)

def create_new_folder():
    global current_directory, listbox

    new_folder_name = simpledialog.askstring("Input", "Enter folder name:")
    if new_folder_name:
        new_folder_path = os.path.join(current_directory[0], new_folder_name)
        try:
            os.mkdir(new_folder_path)
            populate_listbox(listbox, current_directory[0])
        except OSError as e:
            messagebox.showerror("Error", f"Failed to create folder: {e}")

def delete_selected_folder():
    global current_directory, listbox

    selected_indices = listbox.curselection()
    if selected_indices:
        selected_index = selected_indices[0]
        selected_item = listbox.get(selected_index)

        if selected_item != "..":
            folder_to_delete = os.path.join(current_directory[0], selected_item)
            try:
                if os.path.isdir(folder_to_delete):
                    os.rmdir(folder_to_delete)
                else:
                    os.remove(folder_to_delete)
                populate_listbox(listbox, current_directory[0])
            except OSError as e:
                messagebox.showerror("Error", f"Failed to delete folder/file: {e}")


def on_double_click(event):
    global current_directory

    selected_indices = listbox.curselection()
    if selected_indices:
        selected_index = selected_indices[0]
        selected_item = listbox.get(selected_index)

        if selected_item == "..":
            if len(current_directory[0]) > 1:
                current_directory[0] = os.path.dirname(current_directory[0])  # Get the parent directory
        else:
            new_folder = os.path.join(current_directory[0], selected_item)
            current_directory[0] = new_folder  # Update the current directory

        populate_listbox(listbox, current_directory[0])


def create_ui(root, root_node, initial_directory=os.path.expanduser("~")):  # Specify the initial directory here
    global current_node, listbox

    root.geometry(f"750x500")

    # Rest of your UI creation code
    listbox = tk.Listbox(root)
    listbox.pack(fill=tk.BOTH, expand=True)

    current_directory[0] = initial_directory

    current_node = root_node

    populate_listbox(listbox, initial_directory)

    listbox.bind("<Double-Button-1>", on_double_click)

    new_folder_button = tk.Button(root, text="New Folder", command=create_new_folder)
    new_folder_button.pack(side=tk.LEFT, padx=10)
    delete_folder_button = tk.Button(root, text="Delete Folder/File", command=delete_selected_folder)
    delete_folder_button.pack(side=tk.LEFT, padx=10)