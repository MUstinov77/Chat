FROM python:3.12

WORKDIR /backend

COPY requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

COPY . .

CMD ["fastapi", "run", "chat/main.py"]