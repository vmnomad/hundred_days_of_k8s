FROM python:3.7-alpine
RUN mkdir /hundred_days_of_k8s
WORKDIR /hundred_days_of_k8s
COPY requirements.txt /hundred_days_of_k8s/
RUN apk add --no-cache --update gcc build-base nginx &&  pip install -r requirements.txt
COPY . /hundred_days_of_k8s/
# init database
RUN python3 manage.py makemigrations && python3 manage.py migrate
RUN chmod +x entrypoint.sh
CMD ./entrypoint.sh