"""
To Do:
config if menus are enumerated, or what symbol to use
"""

class Menu:
    def __init__(self, entries, indentation_level=0):
        self._entries = entries
        self._indentation_level = indentation_level

    def display(self):
        for i, entries in enumerate(self._entries, 1):
            indent = "   " * self._indentation_level
            print(f"{indent}└─ {entries.get_text()}")

"""
    def handle_selection(self, choice):
        selected_entry = self._entries[choice -1 ]  # Get the chosen menu entry
        result = selected_entry.action()

        if isinstance(result, list):
            # if the result is a list, means we have a submenu
            submenu = Menu(result, self._indentation_level + 1)
            submenu.display()
        else:
            print(result)   # Display result (Text or Action
"""




# │
# ├
# └─=