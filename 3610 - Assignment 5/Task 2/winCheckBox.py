from abc import ABC, abstractmethod
from checkBox import Checkbox


class WinCheckbox(Checkbox):
    def paint(self):
        print("Windows Checkbox")