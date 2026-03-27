from services.ocr import ocr, crop
from sysvars import SysVars as svar
from google import genai
from PIL import Image


def extract_document(is_crlv):
    """
    The complete chain to extract document data

    args:
    - is_crlv: boolean indicating whether it's a crlv image or not
    """
    
    GEMINI_KEY = svar.GEMINI_KEY

    image = Image.open(svar.UPLOADS_PATH / "document.png")

    croped_image = crop(image)
    croped_image.save(svar.DATA_ROOT / "uploads" / "document.png")

    client = genai.Client(api_key=GEMINI_KEY)

    return ocr([croped_image], client, is_crlv)