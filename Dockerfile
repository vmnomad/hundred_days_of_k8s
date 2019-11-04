FROM python:3.7
RUN mkdir /100daysofk8s
WORKDIR /100daysofk8s
COPY requirements.txt /100daysofk8s/
RUN pip install -r requirements.txt
COPY . /100daysofk8s/
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]