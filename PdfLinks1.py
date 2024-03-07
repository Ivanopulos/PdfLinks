import fitz  # PyMuPDF

def extract_links_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    links = []

    for page in doc:
        links.extend(page.get_links())

    return links

pdf_path = 'C:\\Users\\IMatveev\\Desktop\\ЛКЕ\\542 и сравних\\ПП_РФ_№542_Методика_расчета_показателей_для_оценки_эффективности(новый).pdf'
links = extract_links_from_pdf(pdf_path)
print(links)