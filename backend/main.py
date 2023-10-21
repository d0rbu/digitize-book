from fastapi import FastAPI, UploadFile, File

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

# @app.post("/upload")
# def create_upload_file(file: UploadFile = File(...)):
#     try:
#         # Save the uploaded file
#         file_path = os.path.join(upload_dir, file.filename)
#         with open(file_path, "wb") as f:
#             f.write(file.file.read())
#         return JSONResponse(content={"message": "File uploaded successfully", "file_path": file_path})
#     except Exception as e:
#         return JSONResponse(content={"error": f"Failed to upload file: {str(e)}"}, status_code=500)

#     return {"filename": file.filename}
