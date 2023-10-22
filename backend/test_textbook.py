from textbook import Textbook
from ocr import NougatOCR
import pytest
import pickle


@pytest.fixture(scope='session')
def textbooks():
    ocr = NougatOCR()
    
    with open('test_pdf3.pdf', 'rb') as f:
        sequence = ocr.process_pdf(f)
    
    textbook2 = Textbook(sequence)

    with open('test_textbook2.tbk', 'wb') as f:
        pickle.dump(textbook2, f)

    with open('test_textbook1.tbk', 'rb') as f:
        textbook1 = pickle.load(f)

    return textbook1, None

def test_extract_table_of_contents(textbooks):
    textbook1, textbook2 = textbooks
    
    toc_raw = Textbook._extract_table_of_contents(textbook1.raw_textbook)
    print(repr(toc_raw[0]))

    assert toc_raw is not None
    assert len(toc_raw) == 1

def test_parse_table_of_contents(textbooks):
    textbook1, textbook2 = textbooks
    
    toc_raw = Textbook._extract_table_of_contents(textbook1.raw_textbook)
    toc = Textbook._parse_table_of_contents(toc_raw)

    assert toc is not None
    assert len(toc) == 7
