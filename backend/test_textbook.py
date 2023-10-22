from textbook import Textbook
from ocr import NougatOCR
import pytest
import pickle
import numpy as np


@pytest.fixture(scope='session')
def textbooks():
    # ocr = NougatOCR()
    
    # with open('test_pdf2.pdf', 'rb') as f:
    #     sequence = ocr.process_pdf(f)
    
    # textbook1 = Textbook(sequence)
    
    # with open('test_pdf3.pdf', 'rb') as f:
    #     sequence = ocr.process_pdf(f)
    
    # textbook2 = Textbook(sequence)

    # with open('textbook1.rtbk', 'rb') as f:
    #     textbook1 = pickle.load(f)
    
    # embeddings1 = np.load('textbook1.npy')
    # textbook1 = Textbook(textbook1, embeddings1)

    with open('textbook2.rtbk', 'rb') as f:
        textbook2 = pickle.load(f)
    
    embeddings2 = np.load('textbook2.npy')
    textbook2 = Textbook(textbook2, embeddings2)

    return textbook1, textbook2

def test_extract_table_of_contents(textbooks):
    textbook1, textbook2 = textbooks
    
    toc_raw = textbook1._extract_table_of_contents()
    print(repr(toc_raw[0]))

    assert toc_raw is not None
    assert len(toc_raw) == 1
