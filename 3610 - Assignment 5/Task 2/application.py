from abc import ABC, abstractmethod
from guiFactory import GUIFactory


class Application:
  def __init__(self, factory: GUIFactory):
    self.button = factory.createButton()
    self.checkbox = factory.createCheckbox()

  def paint(self):
    self.button.paint()
    self.checkbox.paint()

  def createUI(self):
    self.button = self.factory.createButton()
    self.checkbox = self.factory.createCheckbox()

