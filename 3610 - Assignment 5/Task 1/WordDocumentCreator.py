from DocumentCreator import DocumentCreator
from Document import Document
from typing import Self
from WordDocument import WordDocument

class WordDocumentCreator(DocumentCreator):
  def __init__(self):
    super().__init__()

  def create_document(self) -> Document:
    return WordDocument()
