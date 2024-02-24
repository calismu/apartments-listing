FROM node:21-bullseye

WORKDIR /app

RUN apt-get update
RUN apt-get install adb openjdk-17-jdk -y

ARG JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ARG ANDROID_HOME=/usr/lib/android-sdk

RUN cd /usr/lib/android-sdk && wget https://dl.google.com/android/repository/commandlinetools-linux-11076708_latest.zip && unzip commandlinetools-linux-11076708_latest.zip
RUN yes | /usr/lib/android-sdk/cmdline-tools/bin/sdkmanager --licenses --sdk_root=.

COPY ./source/apartments .

CMD ["npm", "start"]