from textbook import Textbook
from ocr import NougatOCR
import pickle
import numpy as np

TEXTBOOK = 'textbook2'


with open(f'{TEXTBOOK}.rtbk', 'rb') as f:
    textbook2 = pickle.load(f)
    
embeddings2 = np.load('textbook2.npy')
textbook2 = Textbook(textbook2, embeddings2)

with open(f'{TEXTBOOK}.tbk', 'wb') as f:
    pickle.dump(textbook2, f)

# ocr = NougatOCR()

# with open(f'{TEXTBOOK}.pdf', 'rb') as f:
#     sequence = ocr.process_pdf(f)

# with open(f'{TEXTBOOK}.rtbk', 'wb') as f:
#     pickle.dump(sequence, f)
