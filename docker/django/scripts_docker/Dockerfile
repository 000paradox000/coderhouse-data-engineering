FROM python:3.11-bookworm

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       neovim \
       unixodbc \
       unixodbc-dev \
       mc \
       libgssapi-krb5-2 \
       libc6 \
       libstdc++6 \
       libkrb5-3 \
       libcurl4 \
       openssl \
       debconf \
       curl \
    && rm -rf /var/lib/apt/lists/*


RUN curl -sSL https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor | tee /usr/share/keyrings/microsoft-prod.gpg > /dev/null
RUN curl https://packages.microsoft.com/keys/microsoft.asc | tee /etc/apt/trusted.gpg.d/microsoft.asc
RUN curl https://packages.microsoft.com/config/debian/12/prod.list | tee /etc/apt/sources.list.d/mssql-release.list
RUN apt-get update
RUN ACCEPT_EULA=Y apt-get install -y msodbcsql18
RUN ACCEPT_EULA=Y apt-get install -y mssql-tools

WORKDIR /app

RUN mkdir /opt/scripts
COPY keep_alive.sh /opt/scripts/keep_alive.sh
RUN chmod +x /opt/scripts/keep_alive.sh

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["/opt/scripts/keep_alive.sh"]
