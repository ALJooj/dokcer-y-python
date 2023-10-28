FROM python:3.11.0

WORKDIR /app

COPY . .

RUN pip install matplotlib

ENTRYPOINT [ "python", "main.py" ]