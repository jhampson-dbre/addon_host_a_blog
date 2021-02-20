FROM python:3.8-slim-buster
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
# Install system packages required by Wagtail and Django.
RUN apt-get update --yes --quiet && apt-get install --yes --quiet --no-install-recommends \
    build-essential \
    libpq-dev \
    libmariadbclient-dev \
    libjpeg62-turbo-dev \
    zlib1g-dev \
    libwebp-dev \
    mariadb-client \
    && rm -rf /var/lib/apt/lists/*
# Requirements are installed here to ensure they will be cached.
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
COPY ./compose/local/web/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
COPY ./compose/local/web/start.sh /start.sh
RUN chmod +x /start.sh
WORKDIR /app
ENTRYPOINT ["/entrypoint.sh"]