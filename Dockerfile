FROM python:3.9-slim
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir pyfoma

WORKDIR /app
COPY src  /app/src

ENTRYPOINT ["python3", "app.py"]