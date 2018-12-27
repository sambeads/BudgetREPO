FROM python:3.6

RUN apt-get update 

COPY cli.py / 
COPY requirements.txt .

RUN pip install -r requirements.txt

CMD ["python","./cli.py"]