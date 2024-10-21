from abc import ABC, abstractmethod

# underscore in front of private or protected variables
# Python does not have a formal interface implementation.
# Effectively implementing an interface by using the "pythonic way" of an abstract class only consisting of

class MenuEntry(ABC):
    def __init__(self, text):
        self._text = text

    def get_text(self):
        """Return the text to display for this menu entry (Default implementation)."""
        return self._text


    @abstractmethod
    def action(self):
        """Perform the action associated with the menu entry."""
        pass


class MenuItem(MenuEntry):
    def __init__(self, text, action):
        super().__init__(text)
        self._action_callback = action

    def action(self):
        if self._action_callback:    # if an action is configured, it will be executed.
            return self._action_callback()
        else:
            return self._text        # if no action is configured, it will display the text


class SubMenu(MenuEntry):
    def __init__(self, text, submenu_entries):
        super().__init__(text)
        self._submenu_entries = submenu_entries

    def action(self):
        return self._submenu_entries