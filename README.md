# Docker+Flask

## APPs in this repo
* guessing_app
* tic_tac_toe
 
## Docker

### pull from docker hub
```
docker pull lawrencetchop/guessing_app
```
```
docker pull lawrencetchop/tictactoe
```

### run from docker hub
```
docker run -d -p 8080:8080 lawrencetchop/guessing_app
```
```
docker run -d -p 1000:1000 lawrencetchop/tictactoe
```

### Build
```
docker build -t guessing_app .
```
### Run
```
docker run -d -p 8080:8080 guessing_app
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
### push to docker hub
```
docker login
docker tag guessing_app <docker_hub_username>/guessing_app  
docker push <docker_hub_username>/guessing_app
```
### pull from docker hub
```
docker pull <docker_hub_username>/guessing_app
```
### run from docker hub
```
docker run -d -p 8080:8080 <docker_hub_username>/guessing_app
```