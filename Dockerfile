FROM python:3.10
WORKDIR /app
COPY . /app
RUN pip install --upgrade pip
#RUN source ./venv/bin/activate
RUN pip install -r requirements.txt
EXPOSE 8090
CMD python ./main.py
