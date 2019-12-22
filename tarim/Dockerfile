FROM python:3.8

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

COPY . .
RUN pip install --upgrade pip --no-cache-dir -r requirements.txt

CMD [ "python", "./run.py" ]