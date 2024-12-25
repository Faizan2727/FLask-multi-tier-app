FROM redhat8/ubi8

RUN yum install python3 -y

RUN pip3 install flask 

RUN pip3 install flask-mysql

WORKDIR /myapp

COPY app.py faizan.py

ENTRYPOINT ["python3","faizan.py"]
