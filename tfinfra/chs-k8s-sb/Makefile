init:
	terraform init

apply:
	terraform apply

destroy:
	terraform destroy
	./renameDefunct.sh butzer-k8s-sb

bash:
	docker run -i -t -v `pwd`/:/tfinfra tbutzer/terraform bash
