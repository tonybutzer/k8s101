echo:
	echo JUST ECHO - nothing to see here
myjup:
	python3 -m notebook --allow-root --ip="0.0.0.0" --NotebookApp.token='yaml' --port=8080


install:
	(cd /opt/k8s101/pkg/jupyter/ ; make install)


git:
	(cd /opt/k8s101; make)


init-swarm:
	docker swarm init --listen-addr 0.0.0.0:8080 > 0000Instructions


join-swarm-workers:
	sshx='ssh -i /home/ubuntu//CHS-LSDSDPAS-butzer.pem ' ; \
	cmd=`grep join 0000Instructions | awk -F" " '{print $$1, $$2, $$3, $$4, $$5, $$6}' \
	| sed 's/To add .*$$//'` ; \
	for ship in `grep ship /etc/hosts | awk '{print $$2}'`; do \
		echo $$sshx $$ship  $$cmd; \
		$$sshx $$ship  $$cmd; \
	done


node:
	docker node ls


