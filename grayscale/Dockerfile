FROM python:3-onbuild
COPY . /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python3","image_TO_gray.py"]