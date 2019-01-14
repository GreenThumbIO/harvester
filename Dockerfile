FROM python:3.7.2

# We copy the rest of the codebase into the image
RUN mkdir /harvester
WORKDIR /harvester

COPY requirements.txt /harvester/requirements.txt
# Install Python dependencies
RUN pip install -r requirements.txt
