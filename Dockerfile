FROM python:3.8-alpine3.14

COPY yaml_merge.py /yaml_merge
COPY requirements.txt /opt/deps/requirements.txt
RUN mkdir /app
RUN apk add --no-cache --virtual .build-deps gcc musl-dev \
    && pip install --no-cache-dir -r /opt/deps/requirements.txt \
    && apk del .build-deps
WORKDIR /app
ENTRYPOINT [ "/yaml_merge" ]
