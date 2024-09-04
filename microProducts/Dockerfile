FROM python:3.6

EXPOSE 5003

WORKDIR /microProducts

COPY requirements.txt /microProducts

RUN pip install -r requirements.txt

COPY . /microProducts

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0", "--port=5003" ]
