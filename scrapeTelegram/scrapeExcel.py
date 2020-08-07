import pandas as pd
import requests
from bs4 import BeautifulSoup
from PyPDF2 import PdfFileWriter, PdfFileReader
from urllib.request import urlopen
from io import StringIO, BytesIO


url = 'http://www.industrialchemistry.org/PDF/r3574.pdf'
writer = PdfFileWriter()

remoteFiles = urlopen(url)
remoteFile = remoteFiles.read()
memoryFile = BytesIO(remoteFile)
pdfFile = PdfFileReader(memoryFile)

for pageNum in range(pdfFile.getNumPages()):
        currentPage = pdfFile.getPage(pageNum)
        #currentPage.mergePage(watermark.getPage(0))
        writer.addPage(currentPage)

pageObj = pdfFile.getPage(0)
print(pageObj.extractText())
pdf
# outputStream = open("output.pdf","wb")
# writer.write(outputStream)
# outputStream.close()
