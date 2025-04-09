import cv2
import numpy as np
import os
import time
from typing import Dict, Tuple

class FaceDetector:
    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        self.recognizer = cv2.face.LBPHFaceRecognizer_create()
        self.face_cache: Dict[str, Tuple[str, float]] = {}  # {face_hash: (name, timestamp)}
        self.cache_duration = 5  # seconds
        self.label_map = self._load_label_map()
        
        # Load trained model if exists
        model_path = "models/face_model.yml"
        if os.path.exists(model_path):
            self.recognizer.read(model_path)

    def _load_label_map(self) -> Dict[int, str]:
        """Load the label map from file"""
        label_map = {}
        try:
            with open("models/label_map.txt", "r") as f:
                for line in f:
                    label_id, name = line.strip().split(":")
                    label_map[int(label_id)] = name
        except FileNotFoundError:
            pass
        return label_map

    def _get_face_hash(self, face_img: np.ndarray) -> str:
        """Generate a simple hash for a face image"""
        return str(hash(face_img.tobytes()))

    def _is_in_cache(self, face_hash: str) -> Tuple[bool, str]:
        """Check if face is in cache and return name if valid"""
        if face_hash in self.face_cache:
            name, timestamp = self.face_cache[face_hash]
            if time.time() - timestamp < self.cache_duration:
                return True, name
            else:
                del self.face_cache[face_hash]
        return False, ""

    def detect_faces(self, frame: np.ndarray) -> np.ndarray:
        """Detect faces in the frame and draw bounding boxes"""
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)
        
        for (x, y, w, h) in faces:
            face_img = gray[y:y+h, x:x+w]
            face_hash = self._get_face_hash(face_img)
            
            # Check cache first
            in_cache, name = self._is_in_cache(face_hash)
            if in_cache:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                cv2.putText(frame, name, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
                continue
            
            # Try to recognize face
            try:
                label, confidence = self.recognizer.predict(face_img)
                if confidence < 100:  # Lower confidence is better
                    name = self.label_map.get(label, f"Person_{label}")
                    self.face_cache[face_hash] = (name, time.time())
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                    cv2.putText(frame, name, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
                else:
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
                    cv2.putText(frame, "Unknown", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
            except:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
                cv2.putText(frame, "Unknown", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
        
        return frame

def start_detection():
    detector = FaceDetector()
    cap = cv2.VideoCapture(0)
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
            
        frame = detector.detect_faces(frame)
        cv2.imshow('Face Detection', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows() 