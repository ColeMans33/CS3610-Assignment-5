from abc import ABC, abstractmethod
from guiFactory import GUIFactory
from macButton import MacButton
from macCheckBox import MacCheckbox
from button import Button
from checkBox import Checkbox

class MacFactory(GUIFactory):
    def createButton(self) -> Button:
        return MacButton()

    def createCheckbox(self) -> Checkbox:
        return MacCheckbox()