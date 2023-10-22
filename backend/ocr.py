from pdf2image import convert_from_bytes
from tqdm import tqdm
from utils import batched_tensor

import torch as th
from transformers import NougatProcessor, VisionEncoderDecoderModel, GenerationConfig

from io import IOBase
from PIL.Image import Image as ImageObject
from typing import Sequence


class NougatOCR:
    DEFAULT_MAX_LEN = 4096
    DEFAULT_BATCH_SIZE = 3
    MODEL = 'facebook/nougat-base'

    def __init__(self, batch_size: int = DEFAULT_BATCH_SIZE) -> None:
        print('Loading Nougat Processor...')
        self.processor = NougatProcessor.from_pretrained(self.MODEL, torch_dtype=th.bfloat16)
        print('Loading Nougat Model...')
        self.model = VisionEncoderDecoderModel.from_pretrained(self.MODEL, torch_dtype=th.bfloat16)

        self.device = th.device('cuda' if th.cuda.is_available() else 'cpu')
        print(f'Using device: {self.device}')
        self.model.to(self.device)
        self.batch_size = batch_size
    

    @staticmethod
    def pdf_to_images(pdf_file: IOBase) -> Sequence[ImageObject]:
        images: Sequence[ImageObject] = convert_from_bytes(pdf_file.read(), fmt='png', poppler_path=r'.\\poppler-windows\\Library\\bin')

        if len(images) == 0:
            raise ValueError('No images found in PDF')
        
        return images
    

    def process_pdf(self, pdf_file: IOBase, sample: bool = True, max_len: int = DEFAULT_MAX_LEN) -> Sequence[str]:
        images = self.pdf_to_images(pdf_file)
        return self.process(images, sample, max_len)

    
    def process(self, images: ImageObject | Sequence[ImageObject], sample: bool = True, max_len: int = DEFAULT_MAX_LEN) -> Sequence[str]:
        if isinstance(images, ImageObject):
            images = [images]
        
        images = [image.convert('RGB') for image in images]
        
        pixel_values = self.processor(images, return_tensors='pt').pixel_values.to(th.bfloat16)

        # generate transcription
        sequence = []
        for batch in tqdm(batched_tensor(pixel_values, self.batch_size), total=len(pixel_values) / self.batch_size + 1):
            outputs = self.model.generate(
                batch.to(self.device),
                GenerationConfig(
                    min_length=1,
                    max_new_tokens=max_len,
                    bad_words_ids=[[self.processor.tokenizer.unk_token_id]],
                    do_sample=sample,
                    use_cache=True,
                    temperature=1.04,
                    top_p=0.4,
                    repetition_penalty=1.26,
                    length_penalty=1.1,
                ),
            )

            sequence_batch = self.processor.batch_decode(outputs, skip_special_tokens=True)
            sequence_batch = self.processor.post_process_generation(sequence_batch, fix_markdown=False)

            sequence.extend(sequence_batch)

        return sequence
