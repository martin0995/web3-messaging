# Use an official Python runtime as a parent image
FROM python:slim-buster

# Set the working directory in the container
WORKDIR /app

RUN ["apt", "update"]

RUN ["apt", "-y", "install", "python3-pip"]

# Copy the current directory contents into the container at /app
COPY requirements.txt /app

# Install any needed packages specified in requirements.txt
RUN ["pip", "install", "-r", "requirements.txt"]

# Copy the current directory contents into the container at /app
COPY . /app

# Change the working directory to /app/bot
WORKDIR /app/bot

# Make port 5002 available to the world outside this container
EXPOSE 5002

# Run bot.py when the container launches
CMD ["python3", "-u", "bot.py"]
