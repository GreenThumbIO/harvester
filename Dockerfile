FROM python:3.7.2

# We copy the rest of the codebase into the image
RUN mkdir /harvester
WORKDIR /harvester

# Flask environment is set to dev for debug purposes
ENV FLASK_ENV development

# update apt-get and install psql
RUN apt-get update -qq
RUN apt-get install -y postgresql-client

COPY requirements.txt /harvester/requirements.txt

EXPOSE 5000

# Install Python dependencies
RUN pip3 install -r requirements.txt
