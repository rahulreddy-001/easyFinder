FROM pypy:bullseye
WORKDIR /src
ADD . /src 
RUN pip install -r requirements.txt
CMD [ "python", "app.py" ]
