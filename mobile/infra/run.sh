docker container run\
	--name apartments-mobile\
	--network apartments-net\
	-e JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64\
	-e ANDROID_HOME=/usr/lib/android-sdk\
	-it\
	apartments:mobile\
	/bin/bash
