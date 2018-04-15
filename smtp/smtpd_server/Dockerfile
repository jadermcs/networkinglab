# Use an official Python runtime as a parent image
FROM ubuntu

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN apt update
RUN apt install -qy apache2
RUN apt install -qy python3
RUN apt install -qy python3-pip
RUN pip3 install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 1025

# Define environment variable
ENV NAME EMAILSERVER_A

# Run app.py when the container launches
CMD ["python3", "smtpd_server.py"]
