import os
from tree import TreeNode


def scan_and_build_tree(root_path):
    root_node = TreeNode(root_path, is_directory=True)
    build_tree(root_path, root_node)
    return root_node


def build_tree(path, parent_node):
    try:
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            if os.path.isdir(item_path):
                child_node = TreeNode(item, is_directory=True, parent=parent_node)
                parent_node.add_child(child_node)
                build_tree(item_path, child_node)
            else:
                child_node = TreeNode(item, parent=parent_node)
                parent_node.add_child(child_node)
    except PermissionError as e:
        # Handle the permission error here if needed
        print(f"PermissionError: {e}")


if __name__ == "__main__":
    root_directory = os.path.expanduser("~")
    if os.name == "posix":  # Linux or macOS
        root_directory = "/home"  # Start scanning from the root directory
    elif os.name == "nt":  # Windows
        root_directory = "C:\\"  # Start scanning from the C: drive (adjust as needed)

    root_node = scan_and_build_tree(root_directory)
