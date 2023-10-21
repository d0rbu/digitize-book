from dataclasses import dataclass

from io import IOBase
from PIL.Image import Image as ImageObject
from typing import Sequence, Collection
import re


@dataclass
class Page:
    text: str


@dataclass
class Question:
    question: str
    options: Sequence[str]
    answer: int

@dataclass
class Flashcard:
    front: str
    back: str


@dataclass
class Activity:
    name: str
    pages: int


@dataclass
class Summary(Activity):
    content: str


@dataclass
class Quiz(Activity):
    questions: Sequence[Question]


@dataclass
class Flashcards(Activity):
    cards: Sequence[Flashcard]


@dataclass
class Chapter:
    title: str
    pages: Sequence[Page]
    activities: Collection[Activity]


@dataclass
class ToCEntry:
    title: str
    start_page: int
    end_page: int  # non-inclusive


class Textbook:
    def __init__(self, textbook: Sequence[str]):
        self.raw_textbook: Sequence[str] = textbook
        table_of_contents_raw: Sequence[str] = self._extract_table_of_contents(self.raw_textbook)  # pages representing the table of contents
        table_of_contents: Sequence[ToCEntry] = self._parse_table_of_contents(table_of_contents_raw)  # get chapters and their associated pages

        # self.chapters: Sequence[Chapter] = self._parse_chapters(table_of_contents, self.raw_textbook)  # get the actual chapters
    
    @staticmethod
    def _count_numbers(page: str) -> int:  # count the number of separate instances of numbers in the page; i.e. 34 34 1 has 3 numbers
        tokens = page.split()
        numbers = [token for token in tokens if token.isnumeric()]
        return len(numbers)
    
    @staticmethod
    def _extract_table_of_contents(textbook: Sequence[str]) -> Sequence[str]:
        start_keywords = ["table of contents", "contents", "toc"]
        end_condition = lambda page: Textbook._count_numbers(page) < 10  # if there are less than 10 numbers on the page, we assume it's the end of the table of contents

        start_page_number = -1
        end_page_number = -1
        is_in_table_of_contents = False
        for i, page in enumerate(textbook):
            if end_page_number != -1:
                break

            if is_in_table_of_contents:
                if end_condition(page.lower()):
                    end_page_number = i
                    break
            else:
                for start_keyword in start_keywords:
                    if start_keyword in page.lower():
                        is_in_table_of_contents = True
                        start_page_number = i
                        break

        return textbook[start_page_number:end_page_number]
    
    @staticmethod
    def _parse_table_of_contents(table_of_contents_raw: Sequence[str]) -> Sequence[ToCEntry]:
        table_of_contents = '\n'.join(table_of_contents_raw)

        toc_entries = []

        # Define a regular expression pattern to match chapter titles and their associated page numbers
        pattern = r'([IVXLCDM]+|[0-9]+)([A-Za-z]+)\s*(\d+)'

        matches = re.finditer(pattern, table_of_contents)
        
        last_chapter = None
        for match in matches:
            chapter_title = match.group(2)
            start_page = int(match.group(3))
            toc_entry = ToCEntry(title=chapter_title, start_page=start_page)
            toc_entries.append(toc_entry)

            if last_chapter is not None:
                last_chapter.end_page = start_page
        
        toc_entries[-1].end_page = len(table_of_contents_raw)

        return toc_entries
        
    @staticmethod
    def _parse_chapters(table_of_contents: Sequence[ToCEntry], textbook: Sequence[str]) -> Sequence[Chapter]:
        chapters = []

        for toc_entry in table_of_contents:
            start_page = toc_entry.start_page
            end_page = toc_entry.end_page
            chapter_title = toc_entry.title

            # Extract the content of the chapter between start_page and end_page
            chapter_content = Textbook._extract_chapter_content(textbook, start_page, end_page)

            # Create a Chapter object and add it to the chapters list
            chapter = Chapter(title=chapter_title, pages=chapter_content, activities=[])  # TODO: fill activities later
            chapters.append(chapter)

        return chapters

    @staticmethod
    def _extract_chapter_content(textbook: Sequence[str], start_page: int, end_page: int) -> Sequence[Page]:
        # Extract the content between start_page (inclusive) and end_page (exclusive)
        chapter_content = textbook[start_page:end_page]
        
        # Create Page objects for the content
        chapter_pages = [Page(text=page_content) for page_content in chapter_content]

        return chapter_pages
