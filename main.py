from Utility.entries import MenuItem, SubMenu
from Utility.controller import Menu

class IAction:
    def action(self):
        pass

if __name__ == "__main__":
    menuEntry1 = MenuItem("option 1", "no action currently set")
    menuEntry2 = MenuItem("option 2", "no action currently set")

    mainMenu = Menu([menuEntry1, menuEntry2])
    mainMenu.display()
