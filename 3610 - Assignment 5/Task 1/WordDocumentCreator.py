from DocumentCreator import DocumentCreator
from Document import Document
from typing import Self
class WordDocumentCreator(DocumentCreator):
  def __init__(self):
    super().__init__()

  def factory_method(self) -> Document:
    myDocument = DocumentCreator.create_document("Word")
    print(myDocument.objType)
    self.documents.append(myDocument)
