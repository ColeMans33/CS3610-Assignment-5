from typing import Type
from typing import Self
from abc import ABC, abstractmethod
from Document import Document
from WordDocument import WordDocument
from ExcelDocument import ExcelDocument
from PDFDocument import PDFDocument

class DocumentCreator:
  def __init__(self) -> None:
    self.documents: list[Type[Document]]=[]

  @staticmethod
  def create_document(objType: str) -> Document:
    try:
      if objType.lower() == "word":
        return WordDocument()
      elif objType.lower() == "pdf":
        return PDFDocument()
      elif objType.lower() == "excel":
        return ExcelDocument()
      else:
        raise Exception("I can't make this document")
    except Exception as x:
      print(x)

    return None

  def factory_method() -> Document:
    pass
