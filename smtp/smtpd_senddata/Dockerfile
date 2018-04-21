# Use an official Python runtime as a parent image
FROM ubuntu

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN apt update
RUN apt install -qy python3 ssh ftp telnet
RUN apt install -qy python3-pip
RUN apt install -qy curl
RUN pip3 install --trusted-host pypi.python.org -r requirements.txt

# Define environment variable
ENV NAME CLIENT_A

# Run app.py when the container launches
# CMD ["python3", "smtpd_senddata.py"]
