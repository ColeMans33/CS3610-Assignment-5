from typing import Self
from Document import Document
class PDFDocument(Document):

  def __init__(self):
    self.objType = "A PDF Document has been created"

  def create(self) -> Self:
    return self
