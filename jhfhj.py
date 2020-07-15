
import PyPDF2
pdfFileObj = open('jerin.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print(pdfReader.numPages)
pageObj = pdfReader.getPage(0)
pageObj.rotateCounterClockwise(180)
pagewrobj=PyPDF2.PdfFileWriter()
pagewrobj.addPage(pageObj)
ss=open('tilt.pdf','wb')
pagewrobj.write(ss)
pdfFileObj.close()