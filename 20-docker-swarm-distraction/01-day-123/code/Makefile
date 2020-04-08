Image='tbutzer/stackdemo'

build:
	docker build --tag ${Image} .

publish: ## Send this image to docker hub!
	sudo docker login -u tbutzer
	sudo docker push ${Image}

gnufix:
	sudo apt install gnupg2 pass

test:
	for i in 1 2 3 4 5 6\ ; do\
		curl localhost:8000 ; \
	done

shell:
	docker run --rm -it \
		-v /data3/butzer:/data \
		--name rose ${Image} /bin/bash
