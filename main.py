from Utility.entries import MenuItem, SubMenu
from Utility.controller import Menu

class IAction:
    def action(self):
        pass

if __name__ == "__main__":
    main_menu = [
        MenuItem("Option 1", "no action defined"),
        SubMenu("Submenu 1", [
            MenuItem("Sub-option 1", "no action defined"),
            MenuItem("Sub-option 2", "no action defined")
        ]),
        MenuItem("Option 3", "no action defined")
    ]

    controller = Menu(main_menu)
    controller.display()
    controller.handle_selection(2)


"""
Problem:
The menu is displayed first, then the submenus are loaded, making the 
"""
