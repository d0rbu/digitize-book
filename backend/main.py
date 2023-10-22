from fastapi import FastAPI, UploadFile, File, Response, HTTPException, status
from ocr import NougatOCR  # Import the NougatOCR class
from textbook import Textbook

app = FastAPI()
ocr = NougatOCR() 

textbook = Textbook()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/upload", status_code=status.HTTP_201_CREATED)
async def create_upload_file(file: UploadFile = File(...), response=Response()):
    try:
        # Check if the file is a PDF
        # Process the uploaded image using NougatOCR

        # result = ocr.process_pdf(file.file)

        # with open(file.file, 'rb') as f:
        #     contents = f.read()

        # summary = textbook.generate_summary(...)
        # flashcards = textbook.generate_flashcards(...)
        # quiz = textbook.generate_quiz(...)

        # Return the result
        
        return {"message": "File uploaded and processed successfully"}
    except Exception as e:
        return {"error": f"Failed to upload and process file: {str(e)}"}
