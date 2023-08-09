from PyPDF2 import PdfWriter, PdfReader

pdfwriter = PdfWriter()
pdfreader = PdfReader('Дизайн-методичка.pdf')

''' encrypt '''
# Add all pages to the writer
for page in pdfreader.pages:
    pdfwriter.add_page(page)

# Add a password to the new PDF
pdfwriter.encrypt('my-secret-password')

# Save the new PDF to a file
with open('protected.pdf', 'wb') as file:
    pdfwriter.write(file)


# ''' decrypt '''
# reader = PdfReader("protected.pdf")
# writer = PdfWriter()
#
# if pdfreader.is_encrypted:
#     pdfreader.decrypt("my-secret-password")
#
# # Add all pages to the writer
# for page in pdfreader.pages:
#     pdfwriter.add_page(page)
#
# # Save the new PDF to a file
# with open("decrypted-pdf.pdf", "wb") as f:
#     pdfwriter.write(f)
