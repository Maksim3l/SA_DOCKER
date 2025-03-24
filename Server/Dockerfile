FROM python:3.8-slim

WORKDIR /app

COPY . /app

RUN apt-get update && \
    apt-get install -y libgl1-mesa-glx && \
    pip install --no-cache-dir -r req.txt

EXPOSE 5000

ENV FLASK_APP=app/app.py

CMD ["flask", "run", "--host=0.0.0.0"]
