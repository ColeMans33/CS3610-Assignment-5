from ExcelDocumentCreator import ExcelDocumentCreator
from PDFDocumentCreator import PDFDocumentCreator
from WordDocumentCreator import WordDocumentCreator

objList = ["word", "pdf", "excel"]
for objType in objList:
    
    try:
        if objType.lower() == "word":
            wordDoc = WordDocumentCreator()
            print(wordDoc.create_document())
        elif objType.lower() == "pdf":
            pdfDoc = PDFDocumentCreator()
            print(pdfDoc.create_document())
        elif objType.lower() == "excel":
            excelDoc = ExcelDocumentCreator()
            print(excelDoc.create_document())
        else:
            raise Exception("I can't make this document")
    
    except Exception as x:
        print(x)
