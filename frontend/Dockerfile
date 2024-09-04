FROM python:3.6

EXPOSE 5001

WORKDIR /frontend

COPY requirements.txt /frontend

RUN pip install -r requirements.txt

COPY . /frontend

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0", "--port=5001" ]
