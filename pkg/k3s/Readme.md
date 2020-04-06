# Reference

From this article - thanks:
https://medium.com/@yannalbou/k3d-k3s-k8s-perfect-match-for-dev-and-testing-896c8953acc0
by Yann Albou



K3d is a wrapper to easily launch a Kubernetes cluster using the very lightweight Rancher k3s distribution.
It fits particularly well in a development environnement when you want to test your application with the k8s manifests in real condition or as an administrator to validate behaviours or evaluate new k8s features.
In this blog post I will explain how to install it, how to create a full Kubernetes cluster with worker nodes and how it works.


## k3s/k3d ?

First a bit of explanation on k3s. As mentioned in the Rancher web site the idea behind k3s is to get a very efficient and lightweight fully compliant Kubernetes distribution.
The Rancher team did a great job by reducing the binary to less than 40 mb removing all unnecessary components (Legacy, alpha, non-default features, …)
K3s used the following components:
- Flannel is a very simple overlay network that satisfies the Kubernetes requirements. This is a CNI plugin (Container Network Interface), such as Calico, Romana, Weave-net
- CoreDNS is a flexible, extensible DNS server that can serve as the Kubernetes cluster DNS
- Traefik is a modern HTTP reverse proxy and load balancer
- SQLite: the Storage Backends used by default (but support also MySQL, Postgres, and etcd)
- Containerd is a runtime container like docker without the image build part. I will come back later on this important piece…

K3s can be install either through a simple script that will download and configure a linux binary (less than 40Mb) plus a ‘k3s’ cli.
Or, which is my prefer way, through a docker image or with a pre-configured docker-compose. and this is where ‘k3d’ comes in.

> k3d is a utility designed to easily run k3s in Docker, it provides a simple CLI to create, run, delete a full compliance Kubernetes cluster with 0 to n worker nodes.

## Installation
First the installation (of course you need to have docker installed and the kubectl cli).
Launch the following install script that will detect your processor architecture (386, amd64) and your OS (linux, darwin, windows) and then install the cli tool :

```
wget -q -O - https://raw.githubusercontent.com/rancher/k3d/master/install.sh | bash
```
### Create your first cluster:
```
k3d create --name dev --api-port 6551 --publish 8081:80
```
- ‘dev’ is the name of your Kubernetes that expose the api server port to 6551 and publish k3s node ports to the host on port 8081

#### Once created you can check the cluster status:

#### K3d list
+ — — — + — — — — — — — — — — — — — — — + — — — — -+ — — — — -+
| NAME  | IMAGE                         | STATUS   | WORKERS  |
+ — — — + — — — — — — — — — — — — — — — + — — — — -+ — — — — -+
| dev   | docker.io/rancher/k3s:v0.7.0  | running  | 0/0      |
+ — — — + — — — — — — — — — — — — — — — + — — — — -+ — — — — -+
and to connect to it (the kubeconfig is stored in your user directory but it can easily be retrieved with a simple k3d command):

```
export KUBECONFIG="$(k3d get-kubeconfig --name='dev')"
kubectl cluster-info
kubectl get nodes
NAME            STATUS  ROLES   AGE   VERSION
k3d-dev-server  Ready   master  6d1h  v1.14.4-k3s.1
```
One missing piece is the metric server which is a cluster-wide aggregator of resource usage data. It collects metrics like CPU or memory consumption for containers or nodes, exposed by Kubelet on each node.
So, if you want to use k8s’ features like horizontal pod autoscaler or even to be able to use kubectl top command you need to use the metrics-server (which replace Heapster that was marked as deprecated with Kubernetes version 1.11 and retired in 1.13)
To install it :

```
git clone https://github.com/kubernetes-incubator/metrics-server.git
kubectl apply -f metrics-server/deploy/1.8+/
```
Wait 1 or 2 minutes and then you can now use the following commands:
```
kubectl top node
kubectl top pod --all-namespaces
```
### Deploy a nginx server
you can now deploy a simple nginx server using a deployment, a service and an Ingress manifest.

I used the declarative versus imperative approach (see my previous blog on the declarative approach with the desire state)
```
kubectl apply -f https://raw.githubusercontent.com/myannou/k3d-demo/master/nginx.yaml
```

Once pods are running (kubectl get pods) you can access to nginx using localhost and the k3d publish port (8081 in our case):
```
curl http://localhost:8081
```
## Several clusters on 1 machine !
Now repeat those steps creating 2 others k8s clusters (one with 1 worker node and the other with 2 worker nodes:
```
k3d create --name stag --api-port 6552 --publish 8082:80 --workers 1
k3d create --name prod --api-port 6553 --publish 8083:80 --workers 2
```
and then for instance you can scale up to 3 pods in the « prod » cluster:

```
kubectl scale --replicas=3 deployment/nginx

### Just Wait!
**I am running 3 kubernetes clusters on my local macbook pro**  with respectively 1 master, 1 master with 1 worker node and 1 master with 2 worker nodes !
I also did the test with an old MacBook with less memory and I couldn’t run the third cluster but it was easy with the k3d command to stop the other clusters:
```
k3d stop --name=dev
k3d stop --name=stag
```
and you can restart them later (k3d start --name=dev) retrieving the same state as before
You can even decide to create a cluster with a specific version of the k3s docker image which target a specific version of Kubernetes :
```
k3d create --name dev-0-8-1 --api-port 6554 --publish 8084:80 --version=0.8.1
```
it will target a 1.14.6 kubernetes version !
see the available k3s version: https://github.com/rancher/k3s/releases
But how it works to bundle everything in a docker image ?
A « docker ps » shows that the only started docker containers are the one from the master and the workers, you don’t see any docker container for your nginx images we previously started:
```
docker ps
IMAGE                COMMAND                  NAMES
rancher/k3s:v0.7.0   "/bin/k3s agent"         k3d-prod-worker-1
rancher/k3s:v0.7.0   "/bin/k3s agent"         k3d-prod-worker-0
rancher/k3s:v0.7.0   "/bin/k3s server --h…"   k3d-prod-server
rancher/k3s:v0.7.0   "/bin/k3s agent"         k3d-stag-worker-0
rancher/k3s:v0.7.0   "/bin/k3s server --h…"   k3d-stag-server
rancher/k3s:v0.7.0   "/bin/k3s server --h…"   k3d-dev-server
```
So how it works to do docker in docker without mapping the docker socket ?
To understand execute the following commands in the k3d-dev-server docker container:
```
docker exec -it k3d-dev-server crictl images
IMAGE                             TAG      IMAGE ID       SIZE
docker.io/coredns/coredns         1.3.0    2ee68ed074c6e  12.3MB
docker.io/library/nginx           latest   5a3221f0137be  50.7MB
docker.io/library/traefik         1.7.9    98768a8bf3fed  19.9MB
docker.io/rancher/klipper-helm    v0.1.5   c1e4f72eb6760  27.1MB
docker.io/rancher/klipper-lb      v0.1.1   4a065d8dfa588  2.71MB
k8s.gcr.io/metrics-server-amd64   v0.3.3   c6b5d3e48b43d  10.5MB
k8s.gcr.io/pause                  3.1      da86e6ba6ca19  317kB

docker exec -it k3d-dev-server crictl ps
CONTAINER ID   IMAGE          STATE    NAME          
2796b478f1422  c6b5d3e48b43d  Running  metrics-server
e524745ae7fc9  5a3221f0137be  Running  nginx         
d331d0f08e225  98768a8bf3fed  Running  traefik       
50a618c636f6e  4a065d8dfa588  Running  lb-port-443   
44d89c5d598e2  2ee68ed074c6e  Running  coredns       
444f2b203f128  4a065d8dfa588  Running  lb-port-80
```
As previously mentioned k3s relies on the « Containerd » runtime container.
Docker, Containerd, and CRI-O are all container engines for Kubernetes and are all CRI (Container Runtime Interface) compatible
CRI was introduced in Kubernetes 1.5 and acts as a bridge between the kubelet and the container runtime
Like any API, CRI give you an abstraction layer that theoretically allows end users, Cloud providers and even Kubernetes distributions to switch from implementation. K3s allows to switch to docker although it is not recommended:
k3s includes and defaults to containerd. Why? Because it’s just plain better. If you want to run with Docker first stop and think, “Really? Do I really want more headache?” If still yes then you just need to run the agent with the --docker flag
Containerd was initially developed by Docker but was donated in 2017 to CNCF to serve as the industry standard for container management daemon. Docker is still using Containerd, but Containerd is independent now and doesn’t require docker at all (especially the Docker daemon).
We can interact with a CRI runtime directly using the « crictl » tool (like the docker cli)
Containerd adopters are Rancher, Google,… whereas Red Hat is investing heavily in CRI-O.
Conclusion
K3s relies on standards with CRI implemented through Containerd which makes it possible to run inside a Docker image without using ugly and non secured tricks.
The Rancher team did a great job with k3s and k3d making very easy, simple and efficient to run several instances of Kubernetes clusters on a single machine.
Usages are multiples and very adapted to Kubernetes development, testing and training.

