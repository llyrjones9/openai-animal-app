# Download Base Python image
FROM python:3.11.2-alpine3.17

# Create `app` folder within container and set as working directory
WORKDIR /app

# Copy requirements from local env to container
COPY requirements.txt requirements.txt

# Install requirements within container
RUN pip install -r requirements.txt

# Copy rest of application assets to container
COPY ./flaskr .

# Run flask app
ENTRYPOINT ["python", "app.py"]

# Build cmd commands
# docker build -t openai:1.0 .
# docker run -d -p 5000:5000 --name openai openai:1.0