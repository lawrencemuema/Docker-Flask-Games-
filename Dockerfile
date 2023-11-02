
# specify the base image/application : python
FROM python:3.7.4-alpine3.10

#which the working directory to the application
WORKDIR /app

#copy the content in the working directory to the container space.. /app
COPY . /app

#install dependancies
RUN pip install flask

#make a port available
EXPOSE 5000

#run the application
CMD ["python","guessing_app.py"]