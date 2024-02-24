docker network create apartments-net
docker container run\
	--name apartments-db\
	--network apartments-net\
	-p 3306:3306\
	-e MYSQL_ROOT_PASSWORD='apartmentspassword'\
	-d\
	mysql:8.0-bullseye