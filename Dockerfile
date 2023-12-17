FROM jgphilpott/flask-pack:base
ADD . /root
WORKDIR /root
CMD python3 index.py