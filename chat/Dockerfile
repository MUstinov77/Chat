FROM python:3.12

WORKDIR /chat

COPY requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

COPY . .

CMD ["fastapi", "run", "main.py"]