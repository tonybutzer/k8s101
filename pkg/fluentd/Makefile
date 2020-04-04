install:
	sudo curl -L https://toolbelt.treasuredata.com/sh/install-ubuntu-bionic-td-agent3.sh | sh


plugin:
	sudo /opt/td-agent/embedded/bin/fluent-gem install fluent-plugin-elasticsearch

restart:
	sudo cp ./sample-td-agent.conf /etc/td-agent/td-agent.conf
git:
	(cd /opt/k8s101; make)
