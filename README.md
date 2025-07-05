## Install 
```
1. Docker
2. NodeJS
3. NPM
```

## Setup
#### 1. In the root `.env`
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

## Run:
```
docker-compose --env-file .env up --build
```
```
docker-compose down
```