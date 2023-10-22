from fastapi import FastAPI, UploadFile, File, Response, HTTPException, status
from ocr import NougatOCR  # Import the NougatOCR class
from textbook import Textbook
import pickle
import numpy as np

app = FastAPI()
ocr = NougatOCR() 

with open('textbook2.rtbk', 'rb') as f:
    textbook2 = pickle.load(f)
    
embeddings2 = np.load('textbook2.npy')
textbook2 = Textbook(textbook2, embeddings2)

print("Textbook loaded")

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/upload", status_code=status.HTTP_201_CREATED)
async def create_upload_file(file: UploadFile = File(...), response=Response()):
    pass

@app.get("/chapters", status_code=status.HTTP_200_OK)
def get_chapters():
    if textbook2 is not None:
        chapters = []

        for chapter in textbook2.chapters:
            chapter_data = {
                "title": chapter.title,
                "activities": [],
            }

            for activity in chapter.activities:
                activity_data = {
                    "name": activity.name,
                }

                if isinstance(activity, Textbook.Summary):
                    activity_data["content"] = activity.content
                    activity_data["type"] = "summary"
                elif isinstance(activity, Textbook.Quiz):
                    activity_data["questions"] = [
                        {
                            "question": question.question,
                            "options": question.options,
                            "answer": question.answer,
                        }
                        for question in activity.questions
                    ]
                    activity_data["type"] = "quiz"
                elif isinstance(activity, Textbook.Flashcards):
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

