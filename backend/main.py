from fastapi import FastAPI, UploadFile, File, Response, HTTPException, status
from ocr import NougatOCR  # Import the NougatOCR class

app = FastAPI()
ocr = NougatOCR() 

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/upload", status_code=status.HTTP_201_CREATED)
async def create_upload_file(file: UploadFile = File(...), response=Response()):
    try:
        # Check if the file is a PDF
        # Process the uploaded image using NougatOCR
        result = ocr.process_pdf(file.file)

        # Return the result
        

        return {"message": "File uploaded and processed successfully"}
    except Exception as e:
        return {"error": f"Failed to upload and process file: {str(e)}"}
