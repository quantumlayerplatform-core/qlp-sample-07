# Use an official Python runtime as a parent image
FROM python:3.9-slim as builder

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application into the container
COPY . .

# Run tests
RUN pytest

# Use a smaller base image for the runtime environment
FROM python:3.9-alpine

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy only the necessary artifacts from the builder stage
COPY --from=builder /usr/src/app .

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Run the application
CMD ["flask", "run"]