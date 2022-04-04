docker-compose down
#Delete all containers using the following command:
docker rm -f $(docker ps -a -q)
#Delete all volumes using the following command:
docker volume rm $(docker volume ls -q)