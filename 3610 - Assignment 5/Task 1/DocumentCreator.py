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

  def create_document() -> Document:
    pass
