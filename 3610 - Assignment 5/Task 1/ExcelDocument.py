from typing import Self
from Document import Document
class ExcelDocument(Document):

  def __init__(self):
    self.objType = "An Excel Document has been created"

  def create(self) -> Self:
    return self
