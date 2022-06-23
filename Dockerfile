FROM python:3.10

ENV FLASK_APP="api.main"

COPY ./requirements.txt /app/requirements.txt
COPY api/* app/api/

WORKDIR /app
RUN pip3 install -r requirements.txt
EXPOSE 5000

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=80"]
