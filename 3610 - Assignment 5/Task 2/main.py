from abc import ABC, abstractmethod
from checkBox import Checkbox
from button import Button
from guiFactory import GUIFactory
from winButton import WinButton
from winCheckBox import WinCheckbox
from macButton import MacButton
from macCheckBox import MacCheckbox
from application import Application
from winFactory import WinFactory
from macFactory import MacFactory
from sys import platform

if platform == "win32":
  factory = WinFactory()
elif platform == "darwin":
  factory = MacFactory()
else:
  raise Exception("I don't know this OS")

app = Application(factory)
app.button.paint()
app.checkbox.paint()
