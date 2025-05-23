FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY run.sh .
RUN chmod +x run.sh

COPY app/ ./app/
COPY web/ ./web/

EXPOSE 5000
CMD ["./run.sh"]
