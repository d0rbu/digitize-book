from fastapi import FastAPI, UploadFile, File, Response, HTTPException, status
from ocr import NougatOCR  # Import the NougatOCR class
from textbook import Textbook, Summary, Quiz, Flashcards
import pickle
import numpy as np

app = FastAPI()

# ocr = NougatOCR() 
with open('textbook2.tbk', 'rb') as f:
    textbook2 = pickle.load(f)
# with open('textbook2.rtbk', 'rb') as f:
    # textbook2_raw = pickle.load(f)
# with open('textbook2.npy', 'rb') as f:
    # textbook2_embeddings = np.load(f)
print("Textbook loaded")

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/upload", status_code=status.HTTP_201_CREATED)
async def create_upload_file(file: UploadFile = File(...), response=Response()):
    textbook = textbook2
    # textbook = Textbook(textbook2_raw, textbook2_embeddings)

    if textbook is not None:
        toc = textbook.table_of_contents

        return {"table_of_contents": [{"title": chapter.title, "start_page": chapter.start_page.item(), "end_page": chapter.end_page.item()} for chapter in toc]}
    else:
        raise HTTPException(status_code=404, detail="Textbook not found")

@app.get("/chapters", status_code=status.HTTP_200_OK)
def get_chapters():
    textbook = textbook2
    # textbook = Textbook(textbook2_raw, textbook2_embeddings)

    if textbook is not None:
        chapters = []

        for chapter in textbook.chapters:
            chapter_data = {
                "title": chapter.title,
                "activities": [],
            }

            for activity in chapter.activities:
                activity_data = {
                    "name": activity.name,
                }

                if isinstance(activity, Summary):
                    activity_data["content"] = activity.content
                    activity_data["type"] = "summary"
                elif isinstance(activity, Quiz):
                    activity_data["questions"] = [
                        {
                            "question": question.question,
                            "options": question.options,
                            "answer": question.answer,
                        }
                        for question in activity.questions
                    ]
                    activity_data["type"] = "quiz"
                elif isinstance(activity, Flashcards):
                    activity_data["cards"] = [
                        {
                            "front": card.front,
                            "back": card.back,
                        }
                        for card in activity.cards
                    ]
                    activity_data["type"] = "flashcards"

                chapter_data["activities"].append(activity_data)

            chapters.append(chapter_data)

        return {"chapters": chapters}
    else:
        raise HTTPException(status_code=404, detail="Textbook not found")

