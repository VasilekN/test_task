FROM python:3.13-slim

RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    pkg-config

WORKDIR /backend

COPY . /backend/

RUN pip install -r /backend/requirements.txt

RUN chmod +x /backend/wait-for-it.sh

EXPOSE 8000

CMD ["sh", "-c", "python /backend/parse_service/manage.py migrate && python /backend/parse_service/manage.py runserver 0.0.0.0:8000"]