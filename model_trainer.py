import os
import cv2
import numpy as np
from typing import List, Tuple

def get_images_and_labels(dataset_path: str) -> Tuple[List[np.ndarray], List[int]]:
    """Get all face images and their corresponding labels from the dataset"""
    face_images = []
    labels = []
    label_id = 0
    label_map = {}
    
    # Ensure models directory exists
    os.makedirs("models", exist_ok=True)
    
    # Clear existing label map
    if os.path.exists("models/label_map.txt"):
        os.remove("models/label_map.txt")
    
    for person_name in sorted(os.listdir(dataset_path)):
        person_dir = os.path.join(dataset_path, person_name)
        if not os.path.isdir(person_dir):
            continue
            
        label_map[label_id] = person_name
        
        for image_name in os.listdir(person_dir):
            image_path = os.path.join(person_dir, image_name)
            image = cv2.imread(image_path)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            
            # Detect face in the image
            face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            
            for (x, y, w, h) in faces:
                face_img = gray[y:y+h, x:x+w]
                face_images.append(face_img)
                labels.append(label_id)
        
        label_id += 1
    
    # Save label mapping
    with open("models/label_map.txt", "w") as f:
        for label_id, name in label_map.items():
            f.write(f"{label_id}:{name}\n")
    
    return face_images, labels

def train_model():
    """Train the face recognition model using the dataset"""
    dataset_path = "dataset"
    if not os.path.exists(dataset_path):
        raise Exception("Dataset directory not found")
    
    # Get training data
    face_images, labels = get_images_and_labels(dataset_path)
    
    if not face_images:
        raise Exception("No face images found in the dataset")
    
    # Create and train the recognizer
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.train(face_images, np.array(labels))
    
    # Save the trained model
    os.makedirs("models", exist_ok=True)
    recognizer.save("models/face_model.yml")
    
    return "Model trained successfully" 