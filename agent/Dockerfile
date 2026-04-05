FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install openai pdfplumber pydantic requests

CMD ["python", "main.py"]