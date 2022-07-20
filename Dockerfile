FROM python:3.10.2

WORKDIR /Reminder_App

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src .
