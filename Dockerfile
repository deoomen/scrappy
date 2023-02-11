FROM python:3.11-slim

COPY ./app /app
WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt -r tools/requirements.txt -r scripts/requirements.txt

CMD ["bash"]
