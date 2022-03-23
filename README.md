App project manual

Before you may pull this project from git!
Depends programs `docker`, `docker-compose`

1) Creating .env files, you need create .env and .env_db
```
    # .env example
    DJANGO_SECRET=Your token

    ####  database configs  ####
    DB=some_db
    DB_USER=some_user
    DB_PASSWORD=some_password
    DB_HOST=some_host
    DB_PORT=some_port
```

```
    # .env_db example
    POSTGRES_PASSWORD=some_user
    POSTGRES_USER=some_password
    POSTGRES_DB=some_db
```

2) Make Your ENTRYPOINT Scripts Executable

    `sudo chmod +x entrypoint.sh`

3) Up docker compose 

    `docker-compose up`

4) Make migrations and migrate

```
    docker-compose exec web python3 manage.py makemigration
    docker-compose exec web python3 manage.py migrate
```

5) Create super user and collect static

```
    docker-compose exec web python3 manage.py createsuperuser
    docker-compose exec web python3 manage.py collectstatic
```

6) Start cron tasks 

    ```docker-compose exec web python3 manage.py crontab add```

restart container with command "`docker-compose restart`"


Add systemcd service for docker compose autorestart

1) Create `/etc/systemd/system/docker-compose-app.service` file and write

```
    [Unit]
    Description=Docker Compose Application Service
    Requires=docker.service
    After=docker.service

    [Service]
    WorkingDirectory=/{your project path}
    ExecStart=docker-compose up
    ExecStop=docker-compose down
    TimeoutStartSec=0
    Restart=on-failure
    StartLimitIntervalSec=60
    StartLimitBurst=3

    [Install]
    WantedBy=multi-user.target
```


Project host:   `130.162.211.28`

github: `https://github.com/Bakdolot/dev_today_proj`

postman:    `https://www.postman.com/joint-operations-explorer-51599287/workspace/test-project/collection/16782161-f01d74bf-817c-414f-a088-638a58f56ef6?action=share&creator=16782161`
