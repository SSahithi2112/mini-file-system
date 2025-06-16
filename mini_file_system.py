class Node:
    def __init__(self, name, is_file=False):
        self.name = name
        self.is_file = is_file
        self.children = []

def add_node(parent, name, is_file=False):
    new_node = Node(name, is_file)
    parent.children.append(new_node)

def change_directory(current, folder_name):
    for child in current.children:
        if not child.is_file and child.name == folder_name:
            return child
    print("Folder not found.")
    return current

def delete_node(current, name):
    for child in current.children:
        if child.name == name:
            current.children.remove(child)
            print(f"{name} deleted.")
            return
    print(f"{name} not found.")

def display_structure(node, indent=0):
    print("  " * indent + ("[File] " if node.is_file else "[Folder] ") + node.name)
    for child in node.children:
        display_structure(child, indent + 1)

def search(node, name):
    if node.name == name:
        return node
    for child in node.children:
        result = search(child, name)
        if result:
            return result
    return None

# Create root directory
root = Node("root")

def menu():
    global root
    while True:
        print("\nCurrent Folder:", root.name)
        print("1. Add Folder")
        print("2. Add File")
        print("3. Change Directory")
        print("4. Delete Node")
        print("5. View Folder Structure")
        print("6. Search")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter folder name: ")
            add_node(root, name, is_file=False)

        elif choice == "2":
            name = input("Enter file name: ")
            add_node(root, name, is_file=True)

        elif choice == "3":
            name = input("Enter folder name to change directory to: ")
            new_dir = change_directory(root, name)
            if new_dir:
                root = new_dir

        elif choice == "4":
            name = input("Enter name to delete: ")
            delete_node(root, name)

        elif choice == "5":
            display_structure(root)

        elif choice == "6":
            name = input("Enter name to search: ")
            found = search(root, name)
            if found:
                print(f"{name} found! Type: {'File' if found.is_file else 'Folder'}")
            else:
                print(f"{name} not found.")

        elif choice == "7":
            print("Exiting...")
            break

        else:
            print("Invalid choice.")

# Start the menu
menu()
