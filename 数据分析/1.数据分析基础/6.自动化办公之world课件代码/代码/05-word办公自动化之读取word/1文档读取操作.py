from docx import Document

doc = Document('test.docx')
paragraphs = doc.paragraphs
# print(len(paragraphs))
for paragraph in paragraphs:
    print(paragraph.text)