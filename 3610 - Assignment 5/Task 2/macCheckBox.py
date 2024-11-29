from abc import ABC, abstractmethod
from checkBox import Checkbox

class MacCheckbox(Checkbox):
    def paint(self):
        print("Mac Checkbox")