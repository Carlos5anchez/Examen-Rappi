#imagen base
FROM python:3.8-slim-buster
RUN apt-get update
RUN apt-get install nano
COPY . /home/administrador/server
WORKDIR /home/administrador/server
RUN pip3 install psycopg2-binary requests
RUN pip3 install -r requirements.txt 
CMD ["uvicorn","server:app","--reload","--host","0.0.0.0","--port","8000"]