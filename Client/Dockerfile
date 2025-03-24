FROM python:3.8-slim

RUN apt-get update && apt-get install -y iputils-ping

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r req.txt

EXPOSE 8000

ENV FLASK_APP=app/app.py

CMD ["flask", "run", "--host=0.0.0.0", "--port=8000"]
