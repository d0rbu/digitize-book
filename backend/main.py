from fastapi import FastAPI, UploadFile, File, Response, HTTPException, status

app = FastAPI()



@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/upload", status_code=status.HTTP_201_CREATED)
async def create_upload_file(file: UploadFile = File(...), response=Response()):
    try:
        # Read the content of the uploaded file into memory

        return {"message": "File uploaded and processed successfully"}
    except Exception as e:
        return {"error": f"Failed to upload and process file: {str(e)}"}
