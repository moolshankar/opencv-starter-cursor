# OpenCV-Based Facial Detection System

A facial detection and recognition system built using OpenCV and Streamlit. This system allows you to:
- Upload and store images of people
- Train a facial recognition model
- Perform real-time face detection and recognition

## Setup

1. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the FastAPI server:
```bash
python app.py
```

2. In a new terminal, start the Streamlit UI:
```bash
streamlit run streamlit_app.py
```

3. Open your browser and navigate to `http://localhost:8501`

## Features

### Upload Images
- Upload at least 4 images of a person
- Images are stored in the `dataset/<name>` directory
- Each person should have their own directory

### Train Model
- Train the facial recognition model using uploaded images
- The trained model is saved in `models/face_model.yml`

### Face Detection
- Start real-time face detection using your webcam
- Detected faces are highlighted with bounding boxes
- Recognized faces are labeled with the person's name
- Press 'q' to stop detection

## Project Structure

```
.
├── app.py              # FastAPI server
├── face_detector.py    # Face detection logic
├── model_trainer.py    # Model training logic
├── streamlit_app.py    # Streamlit UI
├── requirements.txt    # Dependencies
├── dataset/           # Stored images
└── models/            # Trained models
```

## Notes

- Make sure you have a webcam connected for face detection
- The system requires at least 4 images per person for training
- Face detection works best with well-lit, front-facing images
- The model is trained using the LBPH (Local Binary Patterns Histograms) algorithm 