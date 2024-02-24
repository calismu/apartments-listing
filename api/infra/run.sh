docker container run\
	--name apartments-api\
	--network apartments-net\
	-p 8000:8000\
	-d\
	apartments:api