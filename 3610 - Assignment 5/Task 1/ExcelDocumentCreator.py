from DocumentCreator import DocumentCreator
from Document import Document
from typing import Self
from ExcelDocument import ExcelDocument
class ExcelDocumentCreator(DocumentCreator):
  def __init__(self):
    super().__init__()

  def create_document(self) -> Document:
    return ExcelDocument()

  
