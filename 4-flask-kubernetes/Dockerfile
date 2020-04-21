FROM python:stretch

# Copy project files into docker image
# and set working directory
COPY . ./app

WORKDIR /app

# Upgrade pip and install dependencies
# triggering change in codepipeline
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

ENTRYPOINT ["gunicorn", "--bind", ":8080", "main:APP"]