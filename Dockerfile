FROM python:3.10.2

WORKDIR /Reminder_App

COPY . /Reminder_App

COPY . /requirements.txt

RUN pip install -r requirements.txt

CMD [ "cd .\src", "python", "manage.py", "runserver" ]