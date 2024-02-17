FROM --platform=linux/amd64 python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD [ "gunicorn", "-b", "0.0.0.0:8000", "-k", "gevent", "app:create_app()" ]
