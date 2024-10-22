from abc import ABC, abstractmethod

# Underscore in front of private or protected variables
# Python does not have a formal interface implementation.
# Effectively implementing an interface by using the "pythonic way" of an abstract class only consisting of
# an abstract method


class IAction(ABC):
    @abstractmethod
    def action(self):
        """Perform the action associated with the menu entry."""
        pass


class TextMixin(ABC):   # A Mixin is a class that provides certain functionality to classes without being complete
    def __init__(self, text):
        self._text = text

    def get_text(self):
        return self._text


class MenuItem(IAction, TextMixin):
    def __init__(self, text, action):
        super().__init__(text,)     # Calling the TextMixin contructor
        self._action_callback = action

    def action(self):   # Implementing IAction interface
        if self._action_callback:    # if an action is configured, it will be executed.
            return self._action_callback()
        else:
            return "No action defined!"


class SubMenu(TextMixin):
    def __init__(self, text, submenu_entries):
        super().__init__(text)
        self._submenu_entries = submenu_entries

    def get_submenu_entries(self):
        return self._submenu_entries