FROM python:3.11-bookworm

WORKDIR /app

ADD . /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["sh", "-c", "while true; do sleep 1; done"]
