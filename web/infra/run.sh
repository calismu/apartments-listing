docker container run\
	--name apartments-web\
	--network apartments-net\
	-p 3000:3000\
	-d\
	apartments:web