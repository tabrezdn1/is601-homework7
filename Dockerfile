# Use the official Python image from the Python Docker Hub repository as the base image
FROM python:3.12-slim-bullseye

# Set the working directory to /app in the container
WORKDIR /app

# Create a non-root user named 'tabrezdn1' with a home directory
RUN useradd -m tabrezdn1

# Copy the requirements.txt file to the container to install Python dependencies
COPY requirements.txt ./

# Install the Python packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Before copying the application code, create the logs and qr_code directories
# and ensure they are owned by the non-root user
RUN mkdir logs qr_code && chown tabrezdn1:tabrezdn1 logs qr_code

# Copy the rest of the application's source code into the container, setting ownership to 'tabrezdn1'
COPY --chown=tabrezdn1:tabrezdn1 . .

# Switch to the 'tabrezdn1' user to run the application
USER tabrezdn1

# Set the entrypoint as the Python interpreter
ENTRYPOINT ["python"]

# Set the default command to run the main.py script, which starts the application
CMD ["main.py"]