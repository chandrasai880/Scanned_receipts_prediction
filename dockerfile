#Deriving the latest base image
FROM python:latest

WORKDIR /usr/app/src

ADD web_app.py .

RUN pip3 install --upgrade pip

RUN pip3 install streamlit

RUN pip3 install statsmodels

COPY / ./

CMD [ "streamlit","run", "web_app.py" ]