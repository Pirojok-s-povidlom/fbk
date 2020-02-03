FROM tiangolo/uwsgi-nginx:python3.7
ENV UWSGI_INI /application/uwsgi.ini
ENV LISTEN_PORT 8080
EXPOSE 8080
COPY ./application /application
COPY ./nginx/nginx.conf /
COPY ./nginx/prestart.sh /app/

RUN pip install psycopg2
WORKDIR /appapplication