from typing import Self
from Document import Document
class WordDocument(Document):

  def __init__(self):
    self.objType = "A Word Document has been created"

  def create(self) -> Self:
    return self
