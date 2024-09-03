# Vblog
A FastAPI backend for a creating blogs by category for authors.

## Run 🏃‍♀️

Clone the project

```bash
  git clone https://github.com/kapil864/fast-api-app.git
```
If you have docker installed that will be helpful for running a posgres db via docker compose, if not then you can configure your own database.


Run postgresdb docker
```
docker compose -f docker-compose.yaml -d
```

Update the SQLALCHEMY_DATABASE_URL if you are using your own relational db at backend/database.py

Install requirements for project i.e python3.10 or above, and required python packages
```
pip3 install -r requirements.txt
```
Run in production mode

```
fastapi run backend/main.py
```

Run in dev mode
```
fastapi dev backend/main.py
```

This will run the fastAPI and you can access swagger docs at http://127.0.0.1:8000/docs

The above will run fastAPI app, but is has some problems i.e secrets are scattered all over the place so.

I will be updating the project so that it can run via docker containers. 😎

## Testing 

Unit tests are there to ensure smooth working of project, run unit tests using below cmd

```
pytest
```
