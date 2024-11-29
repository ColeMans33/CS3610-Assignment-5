from abc import ABC, abstractmethod
from checkBox import Checkbox
from button import Button
from guiFactory import GUIFactory
from winButton import WinButton
from winCheckBox import WinCheckbox

class WinFactory(GUIFactory):
    def createButton(self) -> Button:
        return WinButton()

    def createCheckbox(self) -> Checkbox:
        return WinCheckbox()
