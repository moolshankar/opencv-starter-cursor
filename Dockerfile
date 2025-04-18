# Use Python 3.9 as base image
FROM python:3.9-slim

# Install system dependencies required for OpenCV
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Create necessary directories
RUN mkdir -p dataset models

# Expose ports for FastAPI and Streamlit
EXPOSE 8000 8501

# Set environment variable for OpenCV to work in headless mode
ENV DISPLAY=:99

# Create entrypoint script
RUN echo '#!/bin/bash\n\
if [ "$SERVICE" = "fastapi" ]; then\n\
    python app.py\n\
elif [ "$SERVICE" = "streamlit" ]; then\n\
    streamlit run streamlit_app.py\n\
else\n\
    echo "Please specify SERVICE=fastapi or SERVICE=streamlit"\n\
    exit 1\n\
fi' > /app/entrypoint.sh && chmod +x /app/entrypoint.sh

# Set the entrypoint
ENTRYPOINT ["/app/entrypoint.sh"] 