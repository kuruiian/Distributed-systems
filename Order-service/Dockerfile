# Use official Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy everything
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Expose Flask port
EXPOSE 5002

# Run the app
CMD ["python", "app.py"]
