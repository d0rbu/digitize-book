from PIL import Image
from pdf2image import convert_from_bytes

import torch as th
from transformers import NougatProcessor, VisionEncoderDecoderModel

from io import IOBase
from PIL.Image import Image as ImageObject
from typing import Sequence


class NougatOCR:
    def __init__(self):
        print('Loading Nougat Processor...')
        self.processor = NougatProcessor.from_pretrained('facebook/nougat-base')
        print('Loading Nougat Model...')
        self.model = VisionEncoderDecoderModel.from_pretrained('facebook/nougat-base')

        self.device = th.device('cuda' if th.cuda.is_available() else 'cpu')
        print(f'Using device: {self.device}')
        self.model.to(self.device)
    

    @staticmethod
    def pdf_to_images(pdf_file: IOBase) -> Sequence[ImageObject]:
        images: Sequence[ImageObject] = convert_from_bytes(pdf_file.read())

        if len(images) == 0:
            raise ValueError('No images found in PDF')
        
        return images
    

    def process_pdf(self, pdf_file: IOBase):
        images = self.pdf_to_images(pdf_file)
        return self.process(images)

    
    def process(self, image: ImageObject | Sequence[ImageObject]):
        if isinstance(image, ImageObject):
            image = [image]
        
        pixel_values = self.processor(image, return_tensors='pt').pixel_values

        # generate transcription (here we only generate 30 tokens)
        outputs = self.model.generate(
            pixel_values.to(self.device),
            min_length=1,
            max_new_tokens=30,
            bad_words_ids=[[self.processor.tokenizer.unk_token_id]],
        )

        sequence = self.processor.batch_decode(outputs, skip_special_tokens=True)[0]
        sequence = self.processor.post_process_generation(sequence, fix_markdown=False)

        return sequence
