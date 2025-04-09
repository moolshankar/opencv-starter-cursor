# OpenCV-Based Facial Detection System

## Overview

This project is a facial detection system built using **OpenCV** for image processing and detection. It supports:

- Capturing and storing images with user-provided labels
- Training a facial recognition model using stored images
- Real-time video-based facial detection using the trained model
- Caching mechanism for recently detected faces to improve performance
- Interactive UI using **Streamlit** for managing all operations

---

## Features

### 1. Image Capture and Storage API

- RESTful API to upload a new person’s name and at least **4 images**
- Backend function to store these images in a structured directory (e.g., `dataset/<name>/img1.jpg`)
- Image validation (min. image size, face presence) is optional but recommended

#### API Specification

`POST /api/images/upload`

**Request Parameters:**
- `name`: String (person identifier)
- `images`: List of image files (min 4)

**Response:**
- `200 OK`: Confirmation of storage
- `400 Bad Request`: Missing or insufficient images

---

### 2. Model Training

- Backend function to train an OpenCV-based facial recognition model
- Uses images in the dataset folder as training data
- Generates and stores the trained model (`models/face_model.yml`)

#### API Specification

`POST /api/model/train`

**Response:**
- `200 OK`: Model trained successfully
- `500 Internal Server Error`: Any issues during training

---

### 3. Real-time Video Face Detection

- Starts webcam or video feed
- Parses frames and detects faces using the trained model
- Draws bounding boxes around detected faces
- Uses a local hashmap-based cache to store recently detected faces to avoid redundant recognition

#### API Specification

`POST /api/video/start`

**Response:**
- Stream or trigger signal for detection started

**Cache Mechanism:**
- A Python dictionary `{face_hash: timestamp}` is used
- If a face is recently detected, skip re-evaluation for `X` seconds

---

### 4. Streamlit UI

A Streamlit-powered frontend to interact with the system.

#### Functional UI Elements:

- **Upload Images**
  - Text input: Name
  - File uploader: Min 4 image files
  - Button to upload
- **Train Model**
  - Button to trigger `/api/model/train`
- **Start Face Detection**
  - Button to trigger `/api/video/start`
  - Optionally view video feed in Streamlit
