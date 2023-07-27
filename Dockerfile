FROM python:3.10-slim-buster

ENV DockerHOME=/home/app  

RUN mkdir -p $DockerHOME  

WORKDIR $DockerHOME  

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  

RUN pip install --upgrade pip  

COPY . .

RUN pip install -r requirements.txt  

RUN chmod +x ./scripts/startup.sh

EXPOSE 8080

CMD ["./scripts/startup.sh"]  