#!/bin/bash

# Color codes
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${GREEN}Stopping OpenCV Face Detection System...${NC}"

# Stop FastAPI server
echo "Stopping FastAPI server..."
pkill -f "python app.py"
if [ $? -eq 0 ]; then
    echo -e "${GREEN}FastAPI server stopped${NC}"
else
    echo -e "${RED}FastAPI server was not running${NC}"
fi

# Stop Streamlit UI
echo "Stopping Streamlit UI..."
pkill -f "streamlit run streamlit_app.py"
if [ $? -eq 0 ]; then
    echo -e "${GREEN}Streamlit UI stopped${NC}"
else
    echo -e "${RED}Streamlit UI was not running${NC}"
fi

# Stop any OpenCV windows
echo "Closing OpenCV windows..."
pkill -f "opencv"
if [ $? -eq 0 ]; then
    echo -e "${GREEN}OpenCV windows closed${NC}"
else
    echo -e "${RED}No OpenCV windows were open${NC}"
fi

echo -e "${GREEN}Application stopped successfully!${NC}" 