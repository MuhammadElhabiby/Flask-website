# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire app to the container
COPY . .

# Create the database directory
RUN mkdir -p /app/db

# Set permissions for the db directory
RUN chmod -R 777 /app/db

# Set the PYTHONPATH
ENV PYTHONPATH=/app

# Set the environment variable for Flask
ENV FLASK_APP=run.py
ENV FLASK_ENV=production

# Expose the port that the app runs on
EXPOSE 5000

# Run the Flask app
CMD ["flask", "run", "--host=0.0.0.0"]
