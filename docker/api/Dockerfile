FROM aids_prediction_mlops:latest

# Set working directory
WORKDIR /app

# Copy API-specific files
COPY api/ /app/api/

# Command to run the API
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
