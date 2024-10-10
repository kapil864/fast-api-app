#!/bin/sh
echo "Applying alembic changes"
alembic upgrade head
echo "Starting app service"
fastapi run backend/main.py