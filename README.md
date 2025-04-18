# OpenCV Face Detection System

A facial detection and recognition system built with OpenCV, FastAPI, and Streamlit.

## Features

- Upload images for face recognition training
- Train the model with uploaded images
- Real-time face detection and recognition using webcam
- User-friendly web interface

## Prerequisites

- Python 3.9 or higher
- Webcam access
- Git

## Installation & Running

You can run this application in two ways:

### Method 1: Using Shell Scripts (Local Setup)

1. Clone the repository:
```bash
git clone https://github.com/moolshankar/opencv-starter-cursor.git
cd opencv-starter-cursor
```

2. Start the application:
```bash
./start.sh
```
This script will:
- Create and activate a virtual environment
- Install required dependencies
- Start the FastAPI server and Streamlit UI

3. Stop the application:
```bash
./stop.sh
```
This script will:
- Stop the FastAPI server
- Stop the Streamlit UI
- Close any OpenCV windows

### Method 2: Using Docker (Containerized Setup)

1. Clone the repository:
```bash
git clone https://github.com/moolshankar/opencv-starter-cursor.git
cd opencv-starter-cursor
```

2. Start the application:
```bash
docker-compose up --build
```
This will:
- Build the Docker images
- Start the FastAPI server and Streamlit UI in containers
- Mount the dataset and models directories for persistence

3. Stop the application:
```bash
docker-compose down
```
This will:
- Stop and remove the containers
- Keep the dataset and models intact

## Accessing the Application

Once started (by either method), access:
- Web UI: http://localhost:8501
- API: http://localhost:8000

## Usage

1. **Upload Images**:
   - Navigate to "Upload Images" in the sidebar
   - Enter a person's name
   - Upload at least 4 images of the person
   - Click "Upload" to save the images

2. **Train Model**:
   - Navigate to "Train Model" in the sidebar
   - Click "Train Model" to start training
   - Wait for the success message

3. **Face Detection**:
   - Navigate to "Face Detection" in the sidebar
   - Click "Start Face Detection" to begin
   - A window will open showing the webcam feed with face detection
   - Press 'q' to stop the detection

## Project Structure

```
opencv-starter-cursor/
├── app.py              # FastAPI server
├── streamlit_app.py    # Streamlit UI
├── face_detector.py    # Face detection logic
├── model_trainer.py    # Model training logic
├── dataset/           # Directory for training images
├── models/            # Directory for trained models
├── start.sh          # Script to start the application locally
├── stop.sh           # Script to stop the application locally
├── Dockerfile        # Docker image definition
├── docker-compose.yml # Docker services configuration
└── requirements.txt   # Python dependencies
```

## Notes

- When using Docker on macOS or Windows, webcam access might require additional configuration
- The dataset and models directories are persisted even when using Docker
- Both methods (shell scripts and Docker) provide the same functionality

## Contributing

Feel free to open issues or submit pull requests for improvements.

## License

MIT License 