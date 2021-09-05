import os
from pathlib import Path
from typing import Optional

from PIL import Image
from pytesseract import pytesseract


class OCR:
    def __init__(
        self,
    ) -> None:
        pytesseract.tesseract_cmd = str(Path(os.getenv('TESSERACT_CMD')).resolve())

        self.actions = {
            'i2s': pytesseract.image_to_string,
            'i2b': pytesseract.image_to_boxes,
            'i2d': pytesseract.image_to_data,
            'i2osd': pytesseract.image_to_osd,
            'i2ax': pytesseract.image_to_alto_xml,
        }
        self.supported_langs = set(pytesseract.get_languages())

    def recognize(
        self,
        path: Path,
        action: str,
        lang: Optional[str] = None,
    ) -> str:
        if action not in self.actions.keys():
            raise ValueError(f'unsupported action {action}')

        if lang not in self.supported_langs:
            raise ValueError(f'unsupported language {lang}')

        res = self.actions[action](
            Image.open(path),
            lang=lang,
        )

        return res
