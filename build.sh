sudo docker stop timorpho
sudo docker rm $(sudo docker ps --filter status=exited -q)
sudo docker build -t ti-morpho .
sudo docker run  -d --restart unless-stopped --network=host  --name timorpho -p 5050:5050 ti-morpho:latest