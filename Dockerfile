FROM python:3.10

# set the working directory
WORKDIR /app

RUN apt-get update
RUN apt-get install -y fluidsynth
RUN apt-get install -y ffmpeg libavcodec-extra
RUN apt-get install -y pulseaudio jackd2 alsa-utils dbus-x11
RUN apt-get install -y kmod
RUN touch /etc/modprobe.d/myalias.conf
RUN echo "alias char-major-116 snd" >> /etc/modprobe.d/myalias.conf
RUN echo "alias snd-card-0 snd-dummy" >> /etc/modprobe.d/myalias.conf
# CMD ["uname", "-a"]

# install dependencies
COPY ./requirements.txt /app
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# copy the scripts to the folder
COPY . /app

# start the server
CMD ["gunicorn", "-k", "gevent", "-w", "1", "-b", "0.0.0.0:80", "main:app"]
