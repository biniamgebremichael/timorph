FROM python:3.9-slim
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir pyfoma

WORKDIR /
RUN mkdir /src
ADD src  /src/
COPY ti_score.txt  /src/
WORKDIR /src
ENTRYPOINT ["python3", "api.py"]