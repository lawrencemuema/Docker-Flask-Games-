# Use an official Python runtime as a parent image
FROM python:3.6-slim

# Set the working directory of the container to /app, which is where the app will live
WORKDIR /app

# Copy the current/app directory contents into the container at /app
# for guessingapp
# COPY /guessingapp /app 

# for tictactoe
COPY /tictactoe /app 
#copy all files in app folder

#copy everything?
# COPY . /app

#only copy guessing.py and templates folder
# COPY guessing_app.py /app
# COPY /templates /app

# Install any needed packages specified in your requirements.txt
RUN pip install flask

# for guessingapp
# EXPOSE 8080

# for tictactoe
EXPOSE 1000
# a port number is a 16-bit integer that is put in the header appended to a message unit.
# This port number is used to identify the service to which the message should be forwarded.


# Run app.py when the container launches
# for guessingapp
# CMD ["python","guessing_app.py"]

# for tictactoe
CMD ["python","tic_tac_toe.py"]


#build the image
# docker build -t guessing_app .

#run the container
# docker run -d -p 8080:8080 guessing_app

#check the container
# docker ps

#push the image to docker hub
# docker tag guessing_app:latest <your docker hub username>/guessing_app:latest
# docker push <your docker hub username>/guessing_app:latest

#we need to tag because of the naming convention, we need to add our docker hub username to the image name

#pull the image from docker hub
# docker pull <your docker hub username>/guessing_app:latest

