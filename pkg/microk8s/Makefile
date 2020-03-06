help:
	echo installs microk8s
	echo 
	echo make install`



install:
	sudo snap install microk8s --classic --channel=1.17/stable


user:
	sudo usermod -a -G microk8s ${USER}
	echo logout and log back in
