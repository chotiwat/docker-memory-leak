FROM python:2-alpine 

COPY leak.py /

CMD python /leak.py
