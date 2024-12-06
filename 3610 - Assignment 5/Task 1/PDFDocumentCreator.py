from DocumentCreator import DocumentCreator
from Document import Document
from typing import Self
from PDFDocument import PDFDocument

class PDFDocumentCreator(DocumentCreator):
  def __init__(self):
    super().__init__()

  def create_document(self) -> Document:
    return PDFDocument()
