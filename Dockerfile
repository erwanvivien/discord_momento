FROM python:latest

WORKDIR /app

COPY [ "src/", "." ]
COPY [ "requirements.txt", "." ]
COPY [ "token", "."]

RUN pip install -r requirements.txt
RUN mkdir db

CMD [ "python", "launch.py" ]
