FROM python:3.7-alpine

LABEL MAINTAINER="Adrian Roque adrian.w.roque@gmail.com"

WORKDIR /usr/src/app

ENV GROUP_ID=1000 \
	USER_ID=1000

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN rm Dockerfile

RUN addgroup -g $GROUP_ID app
RUN adduser -D -u $USER_ID -G app app -s /bin/sh
USER app

EXPOSE 3000

#ENV MONGO_URL mongodb://${MONGODB_USERNAME:$MONGODB_PASSWORD@$MONGODB_HOSTNAME:27017/$MONGODB_DATABASE
#ENV MONGO_URL mongodb://aroque:aroque@mongodb:27017/api

#CMD ["gunicorn", "-w", "4", "--bind", "0.0.0.0:3000", "wsgi"]
#CMD ["python", "app.py", "echo ${MONGO_URL}]
CMD ["gunicorn", "-w", "4", "--bind", "0.0.0.0:3000", "wsgi"]
#CMD ["python", "app.py"]
