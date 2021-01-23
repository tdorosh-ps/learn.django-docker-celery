FROM python:3.9
ENV PYTHONUNBUFFERED=1
WORKDIR /dataschema
COPY requirements.txt /dataschema/
RUN pip install -r requirements.txt
COPY . /dataschema/
