FROM python:3.7
WORKDIR /usr/src/app
COPY . /usr/src/app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 65010
CMD ["gunicorn", "wsgi:app", "-w 2", "-b 0.0.0.0:65010", "-t 30"]

# CMD ["pwd"]


