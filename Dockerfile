FROM python:3.11.2-alpine3.17

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["python", "app.py"]

# docker build -t openai:1.0 .
# docker run -d -p 5000:5000 --name openai openai:1.0