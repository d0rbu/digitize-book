from ocr import NougatOCR
from PIL import Image
import pytest


@pytest.fixture(scope='session')
def ocr_model():
    ocr = NougatOCR()
    assert ocr is not None

    return ocr

def test_image_ocr(ocr_model):
    image = Image.open('test_image.png')
    assert image is not None

    sequence = ocr_model.process(image)
    assert sequence is not None

    print(sequence)

    assert sequence == 'Hello World'

def test_pdf_conversion(ocr_model):
    with open('test_pdf.pdf', 'rb') as f:
        images = ocr_model.pdf_to_images(f)
        assert images is not None
        assert len(images) == 1

def test_pdf_ocr(ocr_model):
    with open('test_pdf.pdf', 'rb') as f:
        sequence = ocr_model.process_pdf(f)
        assert sequence is not None

        print(sequence)

        assert sequence[0] == 'Hello World'