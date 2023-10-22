from ocr import NougatOCR
from PIL import Image
from time import perf_counter
import pytest


@pytest.fixture(scope='session')
def ocr_model():
    ocr = NougatOCR()
    assert ocr is not None

    return ocr

def test_image_ocr(ocr_model):
    image = Image.open('test_image.png')
    assert image is not None

    sequence = ocr_model.process(image, sample=False, max_len=4)
    assert sequence is not None

    assert sequence[0] == 'Here \\ '

def test_pdf_conversion(ocr_model):
    with open('test_pdf.pdf', 'rb') as f:
        images = ocr_model.pdf_to_images(f)
        assert images is not None
        assert len(images) == 2

def test_pdf_ocr(ocr_model):
    with open('test_pdf.pdf', 'rb') as f:
        sequence = ocr_model.process_pdf(f, sample=False, max_len=4)
        assert sequence is not None
        assert len(sequence) == 2
        assert sequence[0] == 'Here \\ '
        assert sequence[1] == 'Here \\ '

def test_pdf_ocr_benchmark(ocr_model):
    with open('test_pdf.pdf', 'rb') as f:
        start_time = perf_counter()
        sequence = ocr_model.process_pdf(f)
        elapsed_time = perf_counter() - start_time

        assert sequence is not None
        assert elapsed_time < 30
