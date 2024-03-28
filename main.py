from pypdf import PdfReader
from deep_translator import GoogleTranslator

new_file = open("output.txt","w+")

#PDF to text
while True:
    pdf_loc = input("pdf full location: ")
    tar_get = input("Enter your target language: ")
    try:
        readed_pdf = PdfReader(pdf_loc)
        break
    except:
        pass
for pages in readed_pdf.pages:
    text = pages.extract_text()

#Translater
    translated = GoogleTranslator(source="auto", target=tar_get).translate(text)
    print(translated)

#This part isn't working well
    new_file.write(f"\n{translated}")
new_file.close()