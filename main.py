from Utility.entries import MenuItem, SubMenu
from Utility.controller import Menu

class IAction:
    def action(self):
        pass

if __name__ == "__main__":
    main_menu = [
        MenuItem("Option 1", ""),
        SubMenu("Submenu 1", [
            MenuItem("Sub-option 1", ""),
            MenuItem("Sub-option 2", "")
        ]),
        MenuItem("Option 2", "")
    ]

    controller = Menu(main_menu)
    controller.display()


"""
Problem:
The menu is displayed first, then the submenus are loaded, making them apper under 
Place state responsibility at menuEntry or the controller?
Flexibility and agility over methods (MVC)?
Separation of concerns?
"""
