import pdfplumber
import pandas as pd


# PDF
def pdf_to_text(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        pages = pdf.pages
        text = ''
        for page in pages:
            text += page.extract_text()
    return text


# Table
def text_to_table(text):

    rows = text.split('\n')


    data = [row.split() for row in rows if row.strip()]


    df = pd.DataFrame(data)
    return df



def save_to_excel(df, excel_path):
    df.to_excel(excel_path, index=False)



pdf_path = 'ornek.pdf'
excel_path = 'ornek.xlsx'


pdf_text = pdf_to_text(pdf_path)


df = text_to_table(pdf_text)


save_to_excel(df, excel_path)

print(f"Veri {excel_path} dosyasına kaydedildi.")
