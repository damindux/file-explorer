import os


class TreeNode:
    def __init__(self, name, is_directory=False, parent=None):
        self.name = name
        self.is_directory = is_directory
        self.children = []
        self.parent = parent

    def add_child(self, child_node):
        self.children.append(child_node)

    def get_child_by_name(self, name):
        for child in self.children:
            if child.name == name:
                return child
        return None

    def create_folder(self, folder_name):
        if not self.is_directory:
            raise ValueError("Cannot create folder in a non-directory node.")

        folder_path = os.path.join(self.name, folder_name)
        os.mkdir(folder_path)
        child_node = TreeNode(folder_name, is_directory=True, parent=self)
        self.add_child(child_node)
        return child_node

    def delete_folder(self, folder_name):
        if not self.is_directory:
            raise ValueError("Cannot delete folder from a non-directory node.")

        child_to_delete = self.get_child_by_name(folder_name)
        if child_to_delete and child_to_delete.is_directory:
            folder_path = os.path.join(self.name, folder_name)
            os.rmdir(folder_path)
            self.children.remove(child_to_delete)
        else:
            raise ValueError(f"Folder '{folder_name}' not found or not a directory.")


def build_tree(root_path):
    root_node = TreeNode(root_path, is_directory=True)

    for item in os.listdir(root_path):
        item_path = os.path.join(root_path, item)
        if os.path.isdir(item_path):
            child_node = TreeNode(item, is_directory=True, parent=root_node)
            root_node.add_child(child_node)
            build_subtree(item_path, child_node)
        else:
            child_node = TreeNode(item, parent=root_node)
            root_node.add_child(child_node)

    return root_node


def build_subtree(path, parent_node):
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            child_node = TreeNode(item, is_directory=True, parent=parent_node)
            parent_node.add_child(child_node)
            build_subtree(item_path, child_node)
        else:
            child_node = TreeNode(item, parent=parent_node)
            parent_node.add_child(child_node)
