FROM python:3.10

WORKDIR /bot

COPY requirements.txt .
COPY . /bot

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]
