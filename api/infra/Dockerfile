FROM python:3

EXPOSE 8000

WORKDIR /app

RUN apt-get update
RUN apt-get install default-libmysqlclient-dev build-essential pkg-config -y

COPY ./source/requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY ./source/apartments .

CMD ["gunicorn", "apartments.wsgi:application", "--bind", "0.0.0.0:8000", "--workers=1", "--max-requests=1", "--timeout=100", "--log-level=debug"]