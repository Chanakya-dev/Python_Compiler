# Use an official Python runtime as a parent image
FROM python:3.13.0-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port your FastAPI app runs on
EXPOSE 8080

# Command to run the FastAPI app
CMD ["uvicorn", "compiler.main:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]
