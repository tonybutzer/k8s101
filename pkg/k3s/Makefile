echo:
	hi from k3s

install:
	wget -q -O - https://raw.githubusercontent.com/rancher/k3d/master/install.sh | bash


create-dev:
	k3d create --name dev --api-port 6551 --publish 8081:80



git:
	(cd /opt/k8s101; make)
