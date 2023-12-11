FROM python:3.11-bookworm

RUN apt-get update && \
    apt-get install -y  \
      neovim  \
      mc && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY loop.sh .

RUN chmod +x loop.sh

CMD ["./loop.sh"]