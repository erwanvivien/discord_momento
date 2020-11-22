FROM python:latest

WORKDIR /app

COPY [ "src/", "." ]
COPY [ "requirements.txt", "." ]
COPY [ "token", "."]

RUN ls -1 2>&1
RUN pip install -r requirements.txt


CMD [ "python", "launch.py" ]
