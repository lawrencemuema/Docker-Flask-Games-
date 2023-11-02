# Docker+Flask
 
## Docker
### Dockerfile
```
FROM python:3.7.4-alpine3.10
WORKDIR /app
COPY . /app
RUN pip install flask
EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["app.py"]
```
### Build
```
docker build -t flask-app .
```
### Run
```
docker run -d -p 5000:5000 flask-app
```
### Stop
```
docker stop <container_id>
```
### Remove
```
docker rm <container_id>
```
### List
```
docker ps
```
### List all
```
docker ps -a
```
### Remove all
```
docker rm $(docker ps -a -q)
```
