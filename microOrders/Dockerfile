FROM python:3.6

EXPOSE 5004

WORKDIR /microOrders

COPY requirements.txt /microOrders

RUN pip install -r requirements.txt

COPY . /microOrders

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0", "--port=5004" ]
