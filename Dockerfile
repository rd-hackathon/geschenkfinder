FROM python:3.9-alpine
WORKDIR /app
COPY requirements.txt /app
RUN pip3 install -r requirements.txt
COPY . /app
ENV FLASK_APP=app:app
CMD ["flask", "run", "--host", "0.0.0.0"]