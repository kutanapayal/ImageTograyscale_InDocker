FROM python:3.6
#COPY . /usr/src/app
EXPOSE 80
WORKDIR /usr/src/app
COPY . .

#RUN mkdir /usr/src/app/v1

#VOLUME /usr/src/app/v1 : /usr/src/app

#COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt
CMD ["python3","./image_TO_gray.py"]
#CMD ["uvicorn", "app.main:app", "--host", "ec2-3-84-239-94.compute-1.amazonaws.com", "--port", "80"]
