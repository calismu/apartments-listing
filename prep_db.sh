docker exec apartments-db mysql -u root -papartmentspassword -P 3306 -e "CREATE DATABASE IF NOT EXISTS apartments; CREATE USER IF NOT EXISTS apartmentsuser IDENTIFIED BY 'apartmentsuser-pass'; GRANT ALL PRIVILEGES ON apartments.* TO apartmentsuser;";
docker exec apartments-api python3 manage.py makemigrations api
docker exec apartments-api python3 manage.py migrate
docker exec apartments-api python3 manage.py shell -c 'import fill_db'