# Arquivo para abrir PDF, esse método é atualizado
import PyPDF2

pdfFileObj = open('python_tutorial.pdf', 'rb')
pdfReader = PyPDF2.PdfReader(pdfFileObj)
print(len(pdfReader.pages))
pageObj = pdfReader.pages[1]
print(pageObj.extract_text())
pdfFileObj.close()
