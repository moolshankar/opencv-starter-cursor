#!/bin/bash

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${GREEN}Starting OpenCV Face Detection System Setup...${NC}"

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}Python 3 is not installed. Please install Python 3 and try again.${NC}"
    exit 1
fi

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo -e "${RED}pip3 is not installed. Please install pip3 and try again.${NC}"
    exit 1
fi

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo -e "${YELLOW}Creating virtual environment...${NC}"
    python3 -m venv venv
fi

# Activate virtual environment
echo -e "${YELLOW}Activating virtual environment...${NC}"
source venv/bin/activate

# Install dependencies
echo -e "${YELLOW}Installing dependencies...${NC}"
pip install -r requirements.txt

# Create necessary directories
echo -e "${YELLOW}Creating necessary directories...${NC}"
mkdir -p dataset models

# Start FastAPI server in background
echo -e "${YELLOW}Starting FastAPI server...${NC}"
python app.py &
FASTAPI_PID=$!

# Start Streamlit UI
echo -e "${YELLOW}Starting Streamlit UI...${NC}"
echo -e "${GREEN}The application is now running!${NC}"
echo -e "${GREEN}FastAPI Server: http://localhost:8000${NC}"
echo -e "${GREEN}Streamlit UI: http://localhost:8501${NC}"
echo -e "${YELLOW}Press Ctrl+C to stop the application${NC}"

# Wait for user to press Ctrl+C
trap "kill $FASTAPI_PID; echo -e '\n${GREEN}Stopping application...${NC}'; exit" INT
streamlit run streamlit_app.py

# Cleanup
kill $FASTAPI_PID
echo -e "${GREEN}Application stopped.${NC}" 