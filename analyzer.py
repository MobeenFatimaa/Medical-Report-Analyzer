import fitz
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def extract_text(file_path):

    text = ""

    if file_path.lower().endswith(".pdf"):

        doc = fitz.open(file_path)

        for page in doc:

            page_text = page.get_text()

            text += page_text

        doc.close()

    else:

        image = Image.open(file_path)

        text = pytesseract.image_to_string(image)

    return text.strip()