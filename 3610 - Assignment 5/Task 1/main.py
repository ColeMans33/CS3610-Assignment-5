from ExcelDocumentCreator import ExcelDocumentCreator
from PDFDocumentCreator import PDFDocumentCreator
from WordDocumentCreator import WordDocumentCreator

wordDoc = WordDocumentCreator()
wordDoc.factory_method()
pdfDoc = PDFDocumentCreator()
pdfDoc.factory_method()
excelDoc = ExcelDocumentCreator()
excelDoc.factory_method()
