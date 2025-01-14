FROM python

ENV PYTHONUNBUFFERED=1
ENV OCR_PRODUCTION=1 

WORKDIR build
COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000
CMD python manage.py migrate; python manage.py collectstatic --noinput; python manage.py runserver 0.0.0.0:8000 
