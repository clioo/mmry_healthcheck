
FROM python:3.11.4-bookworm

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

RUN python -m compileall /code/app

EXPOSE 80

RUN chmod +x /usr/local/bin/uvicorn

ENTRYPOINT ["uvicorn app.main:app --host 0.0.0.0 --port 80"]
