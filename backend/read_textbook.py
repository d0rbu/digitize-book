from textbook import Textbook
from ocr import NougatOCR
import pickle

TEXTBOOK = 'textbook2'


ocr = NougatOCR()

with open(f'{TEXTBOOK}.pdf', 'rb') as f:
    sequence = ocr.process_pdf(f)

with open(f'{TEXTBOOK}.rtbk', 'wb') as f:
    pickle.dump(sequence, f)
