FROM python:3.11-bookworm

RUN apt-get update && \
    apt-get install -y  \
      neovim  \
      mc && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN mkdir /opt/scripts
COPY keep_alive.sh /opt/scripts/keep_alive.sh
RUN chmod +x /opt/scripts/keep_alive.sh

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["/opt/scripts/keep_alive.sh"]
