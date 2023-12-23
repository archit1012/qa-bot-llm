FROM python:3.9-slim-buster

# set environment variables


RUN pip install -r ./requirement.txt

# make cache dir for models
RUN mkdir /temp

# Set working dir
WORKDIR /app

# copy project
COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
#ENTRYPOINT ["./docker-entrypoint.sh"]
