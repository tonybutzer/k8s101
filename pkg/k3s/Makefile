echo:
	hi from k3s

install:
	wget -q -O - https://raw.githubusercontent.com/rancher/k3d/master/install.sh | bash


create-dev:
	k3d create --name dev --api-port 6551 --publish 8081:80

list:
	k3d list

get-kubectl:
	curl -LO https://storage.googleapis.com/kubernetes-release/release/`curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt`/bin/linux/amd64/kubectl
	chmod +x ./kubectl
	sudo mv ./kubectl /usr/local/bin/kubectl
	kubectl version --client

nodes:
	echo export KUBECONFIG="$(k3d get-kubeconfig --name='dev')"
	kubectl get nodes

cluster:
	kubectl cluster-info


metrics:
	git clone https://github.com/kubernetes-incubator/metrics-server.git
	kubectl apply -f metrics-server/deploy/kubernetes/

git:
	(cd /opt/k8s101; make)
