#! /bin/bash

docker service create --name portainer --publish 80:9000  --constraint 'node.role == manager'  --mount type=bind,src=/var/run/docker.sock,dst=/var/run/docker.sock  portainer/portainer -H unix:///var/run/docker.sock


