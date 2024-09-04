FROM python:3.6

EXPOSE 5002

WORKDIR /microUsers

COPY requirements.txt /microUsers

RUN pip install -r requirements.txt

COPY . /microUsers

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0", "--port=5002" ]
