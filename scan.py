import os
from tree import TreeNode, build_tree


def scan_and_build_tree(root_path):
    root_node = None
    try:
        root_node = build_tree(root_path)
    except PermissionError as e:
        print(f"PermissionError: {e}")
    return root_node


if __name__ == "__main__":
    root_directory = os.path.expanduser("~")
    if os.name == "posix":  # Linux or macOS
        root_directory = "/"  # Start scanning from the root directory
    elif os.name == "nt":  # Windows
        root_directory = "C:\\"  # Start scanning from the C: drive (adjust as needed)

    root_node = scan_and_build_tree(root_directory)
