FROM aids_prediction_mlops:latest

# Set working directory
WORKDIR /app

# Copy API-specific files
COPY api/ /app/api/

# Install FastAPI dependencies if they are not in requirements.txt
RUN pip install fastapi uvicorn

# Command to run the API
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
