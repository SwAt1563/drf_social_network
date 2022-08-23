# syntax = edrevo/dockerfile-plus
INCLUDE+ docker/dockerfiles/base.Dockerfile


COPY . .
RUN pip3 install -r ./docker/requirements/production.txt
