FROM python:3.11-slim-bullseye

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY blogic .

EXPOSE 80

ENV FLASK_APP=app.py

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=80"]
