from typing import Optional
from uuid import uuid4

from fastapi import (
    FastAPI,
    File,
    UploadFile,
)

from app._paths import IMAGES_DIR
from ocr import OCR

app = FastAPI()
ocr = OCR()


@app.post('/ocr')
async def ocr(
    image: UploadFile = File(...),
    action: str = 'i2s',
    lang: Optional[str] = None,
):
    file_name = IMAGES_DIR / str(uuid4())

    with open(file_name, 'wb') as f:
        f.write(image.file.read())
