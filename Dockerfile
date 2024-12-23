FROM python:3.9-slim
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir pyfoma

WORKDIR /
COPY src  /src
COPY ti_score.txt  /src/
WORKDIR /src
ENTRYPOINT ["python3", "app.py"]