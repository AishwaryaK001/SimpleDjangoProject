FROM python:3.12

RUN mkdir /DEVOPSPROJECT1 
WORKDIR /DEVOPSPROJECT1 


COPY / .
RUN pip install -r requirements.txt

EXPOSE 8000
CMD ["python3","manage.py","runserver","0.0.0.0:8000"]
