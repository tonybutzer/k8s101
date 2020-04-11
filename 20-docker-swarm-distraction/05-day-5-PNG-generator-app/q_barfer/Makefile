Image='tbutzer/q_barfer'

build:
	docker build --tag ${Image} .

publish: ## Send this image to docker hub!
	sudo docker login -u tbutzer
	sudo docker push ${Image}
