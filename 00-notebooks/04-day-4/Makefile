KUBECTL=microk8s.kubectl

up:
	${KUBECTL} create -f product-service-deployment.yaml
	# ${KUBECTL} create -f product-service-service.yaml

down:
	${KUBECTL} delete -f product-service-deployment.yaml
	${KUBECTL} delete -f product-service-service.yaml

ref:
	echo "https://kubernetes.io/docs/concepts/services-networking/connect-applications-service/"

svc:
	${KUBECTL} get svc
	${KUBECTL} describe svc product-service
	${KUBECTL} describe svc product-service|egrep '^Port|^IP'
	${KUBECTL} describe svc product-service|egrep -i 'endpoint'

exec:
	${KUBECTL} exec debugger-7b6b564788-s7mck -it bash

# Proxy
# http://kubernetes_master_address/api/v1/namespaces/namespace_name/services/[https:]service_name[:port_name]/proxy
# 

help:
	echo http://localhost:8001/api/v1/namespaces/default/services/product-service:8081/proxy/

# ubuntu@ip-10-12-69-193:~$ sudo kubectl port-forward svc/product-service 8080:8081 --address 10.12.69.193

