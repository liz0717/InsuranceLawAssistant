import pdfplumber


def extract_text_from_pdf(uploaded_file):
    """
    讀取 PDF 並回傳全部文字
    """

    text = ""

    with pdfplumber.open(uploaded_file) as pdf:

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text
