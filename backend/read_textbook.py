from textbook import Textbook
from ocr import NougatOCR
import pickle
import numpy as np

TEXTBOOK = 'textbook1'


with open(f'{TEXTBOOK}.rtbk', 'rb') as f:
    textbook = pickle.load(f)
    
embeddings = np.load(f'{TEXTBOOK}.npy')

print('Loaded textbook')
textbook = Textbook(textbook, embeddings)

with open(f'{TEXTBOOK}.tbk', 'wb') as f:
    pickle.dump(textbook, f)

# ocr = NougatOCR()

# with open(f'{TEXTBOOK}.pdf', 'rb') as f:
#     sequence = ocr.process_pdf(f)

# with open(f'{TEXTBOOK}.rtbk', 'wb') as f:
#     pickle.dump(sequence, f)
