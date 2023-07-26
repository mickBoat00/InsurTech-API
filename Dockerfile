FROM python:3.10-alpine  

ENV DockerHOME=/home/app  

RUN mkdir -p $DockerHOME  

WORKDIR $DockerHOME  

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  

RUN pip install --upgrade pip  

COPY . $DockerHOME  

RUN pip install -r requirements.txt  

RUN python manage.py makemigrations --no-input

# RUN python manage.py migrate --no-input

EXPOSE 8000  

CMD python manage.py runserver