FROM python:3.6.12-alpine

EXPOSE 8080

RUN mkdir -p /app
COPY . /app
RUN pip install -r /app/requirements.txt

CMD python /app/main.py