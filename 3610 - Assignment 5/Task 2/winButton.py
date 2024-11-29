from abc import ABC, abstractmethod
from button import Button

class WinButton(Button):
    def paint(self):
        print("Windows Button")