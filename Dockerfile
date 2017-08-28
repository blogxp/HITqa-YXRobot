FROM python:2.7
MAINTAINER zhangxinghua "xing_hua_zhang@126.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN python manage.py db upgrade
RUN python manage.py db migrate
ENTRYPOINT ["python"]
CMD ["hitqa.py"]

