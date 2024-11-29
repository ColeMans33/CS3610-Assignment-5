from abc import ABC, abstractmethod
from button import Button

class MacButton(Button):
    def paint(self):
        print("Mac Button")