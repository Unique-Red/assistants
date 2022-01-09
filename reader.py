import pyttsx3
import PyPDF2

book = open("Miguel_Grinberg_Flask_Web_Development_Developing_Web_Applications.pdf", "rb")
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)

speaker = pyttsx3.init()
page = pdfReader.getPage(100)
text = page.extractText()
speaker.say(text)
speaker.runAndWait()