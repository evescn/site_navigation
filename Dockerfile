FROM python:3.8.7-alpine3.11

WORKDIR /site_navigation
COPY ./ ./
RUN pip install -r /site_navigation/requirements.txt

EXPOSE 8080
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
