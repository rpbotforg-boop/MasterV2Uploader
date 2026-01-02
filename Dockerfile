FROM python:3.10-alpine

WORKDIR /app

RUN apk add --no-cache \
    gcc g++ musl-dev libffi-dev openssl-dev \
    python3-dev ffmpeg aria2 cargo rust

RUN pip install --upgrade pip setuptools wheel

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "main.py"]
