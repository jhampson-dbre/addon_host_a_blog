ARG BUILD_FROM

FROM $BUILD_FROM
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
# Install system packages required by Wagtail and Django.
RUN apk add --no-cache --virtual .build-deps \
    gcc \
    linux-headers \
    mariadb-dev \
    mariadb-client\
    musl-dev \
    libpq \
    zlib \
    zlib-dev \
    jpeg-dev
# Requirements are installed here to ensure they will be cached.
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
COPY ./compose/local/web/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
COPY ./compose/local/web/start.sh /start.sh
RUN chmod +x /start.sh
WORKDIR /app
ENTRYPOINT ["/entrypoint.sh"]