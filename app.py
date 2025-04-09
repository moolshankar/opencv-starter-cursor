from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import os
import shutil
from typing import List
import face_detector
import model_trainer

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create necessary directories
os.makedirs("dataset", exist_ok=True)
os.makedirs("models", exist_ok=True)

@app.post("/api/images/upload")
async def upload_images(name: str, images: List[UploadFile] = File(...)):
    if len(images) < 4:
        raise HTTPException(status_code=400, detail="At least 4 images are required")
    
    # Create directory for the person
    person_dir = os.path.join("dataset", name)
    os.makedirs(person_dir, exist_ok=True)
    
    # Save images
    for i, image in enumerate(images):
        file_path = os.path.join(person_dir, f"img{i+1}.jpg")
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(image.file, buffer)
    
    return {"message": f"Successfully uploaded {len(images)} images for {name}"}

@app.post("/api/model/train")
async def train_model():
    try:
        model_trainer.train_model()
        return {"message": "Model trained successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/video/start")
async def start_face_detection():
    try:
        face_detector.start_detection()
        return {"message": "Face detection started"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 