FROM python:3.7.2

# We copy the rest of the codebase into the image
RUN mkdir /harvester
WORKDIR /harvester
RUN apt-get update -qq
RUN apt-get install -y postgresql-client
COPY requirements.txt /harvester/requirements.txt
# Install Python dependencies
RUN pip install -r requirements.txt
