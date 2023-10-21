from huggingface_hub import hf_hub_download
from PIL import Image
from PIL.Image import Image as ImageObject

from transformers import NougatProcessor, VisionEncoderDecoderModel
from datasets import load_dataset
import torch

class NougatOCR:
    def __init__(self):
        self.processor = NougatProcessor.from_pretrained('facebook/nougat-base')
        self.model = VisionEncoderDecoderModel.from_pretrained('facebook/nougat-base')

        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        print(f'Using device: {self.device}')
        self.model.to(self.device)
    
    def process(self, image: ImageObject):
        pixel_values = self.processor(image, return_tensors='pt').pixel_values

        # generate transcription (here we only generate 30 tokens)
        outputs = self.model.generate(
            pixel_values.to(self.device),
            min_length=1,
            max_new_tokens=30,
            bad_words_ids=[[processor.tokenizer.unk_token_id]],
        )

        sequence = processor.batch_decode(outputs, skip_special_tokens=True)[0]
        sequence = processor.post_process_generation(sequence, fix_markdown=False)
        pass