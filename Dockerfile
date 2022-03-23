FROM ubuntu

# set work directory
WORKDIR /home/app/web

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt update \
    && apt install -y python python3 python3-pip python3-venv python3-dev libpq-dev curl cron

# RUN python3 -m venv venv
# ENV PATH="./venv/bin:$PATH"
RUN mkdir /home/app/web/static

# install dependencies
RUN pip3 install --upgrade pip
COPY ./requirements.txt .
RUN pip3 install -r requirements.txt

COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /home/app/web/entrypoint.sh
RUN chmod +x /home/app/web/entrypoint.sh

# copy project
COPY . .

ENTRYPOINT ["sh", "/home/app/web/entrypoint.sh"]