Image='tbutzer/job-wq-2'

build:
	docker build --tag ${Image} .


publish:
	docker login -u tbutzer
	docker push ${Image}


fix:
	sudo apt install gnupg2 pass
	echo for errir sayving credentials
