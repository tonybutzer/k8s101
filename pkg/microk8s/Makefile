help:
	echo installs microk8s
	echo 
	echo make install`



install:
	#sudo snap install microk8s --classic --channel=1.17/stable
	#DOCKER was removed in all later versions of microk8s
	sudo snap install microk8s --classic --channel=1.13/stable
	sudo usermod -a -G microk8s ${USER}
	echo logout and log back in
