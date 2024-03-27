FROM python:3.10-slim-bookworm

# set the working directory
WORKDIR /app

RUN apt-get update
RUN apt-get install -y fluidsynth
RUN apt-get install -y ffmpeg libavcodec-extra
# CMD ["uname", "-a"]

# install dependencies
COPY ./requirements.txt /app
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# copy the scripts to the folder
COPY . /app

# start the server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
