FROM python:2.7-stretch
RUN mkdir /data
COPY student_age.py /data/.
COPY student_age.json /data/.
RUN ls /data
#Check & installe python
RUN apt-get update -y && apt-get install python-dev python3-dev libsasl2-dev python-dev libldap2-dev libssl-dev -y
#Installe flask
RUN pip install flask flask_httpauth flask_simpleldap python-dotenv
EXPOSE 80:80
CMD [ "python", "/data/student_age.py" ]
