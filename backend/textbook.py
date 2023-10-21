from PIL import Image
from pdf2image import convert_from_bytes

import torch as th
from transformers import NougatProcessor, VisionEncoderDecoderModel

from io import IOBase
from PIL.Image import Image as ImageObject
from typing import Sequence


class Textbook:
    def __init__(self, textbook: Sequence[str]):
        self.raw_textbook: Sequence[str] = textbook
    
    def _extract_table_of_contents(self, textbook: Sequence[str]):
        pass
