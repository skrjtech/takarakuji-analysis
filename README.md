# 環境構築
## Docker 
```
docker run -it --name takarakuji --shm-size 1g --privileged -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix:rw -v ..:/ws skrjtech/scraping:debian-python3.11.1
```
## Docker Compose
```
docker compose -f .docker/docker-compose.yml up
docker exec -it takarakuji bash
```
## Conda 
```
conda create -n takarakuji python=3.11.1
conda activate takarakuji
pip install -r requirements.txt
```
### pip
```
pip install -r requirements.txt
```