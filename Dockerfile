FROM python:3.9


MAINTAINER Mike Terekhov 'mike_terekhov@gmail.com'

RUN mkdir -p /usr/src/app/flask_blog
WORKDIR /usr/src/app/flask_blog

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY Blog-on-Flask .

EXPOSE 8080


CMD ["python", "run.py"]