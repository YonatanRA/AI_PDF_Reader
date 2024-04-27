FROM python:3.9.19

WORKDIR /usr/src

EXPOSE 5010

COPY ./requirements.txt .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

CMD ["python" , "chat.py", "-q","(user-query)"]