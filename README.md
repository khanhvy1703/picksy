## Install 
```
1. Docker
2. NodeJS
3. NPM
4. MySQL
5. VSCode
6. Postman
```

## Setup
#### 1. In the back-end root, create `.env` file:
```
# MYSQL
MYSQL_HOST=...
MYSQL_PORT=...

MYSQL_USER=...
MYSQL_PASSWORD=...
MYSQL_ROOT_PASSWORD=...

# Main database
MYSQL_MOVIE_TVSHOW_DB=movie_tvshow
```
## Run locally:
#### 1. Back-end:
```
cd back-end
python -m src.main
```

## Run with Docker (not yet):
```
docker-compose --env-file .env up --build
```
```
docker-compose down
```