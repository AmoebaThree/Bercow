FROM python:3.8-slim-buster
RUN apt-get update && apt-get install --yes alsa-utils
RUN pip install redis
WORKDIR /src
COPY . .
CMD ["python", "bercow.py"]