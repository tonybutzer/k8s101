run:
	sudo docker run --name RattyDAVE19.04 \
           --privileged=true \
           -p 8389:3389 \
           -v `pwd`/createusers.txt:/root/createusers.txt \
           -v /home:/home \
           -dit --restart unless-stopped \
           rattydave/docker-ubuntu-xrdp-mate-custom:19.04


stop:
	sudo docker kill RattyDAVE19.04
	sudo docker rm RattyDAVE19.04
