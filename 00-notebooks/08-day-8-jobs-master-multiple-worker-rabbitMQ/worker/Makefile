Image='tbutzer/job-wq-1'

build:
	docker build --tag ${Image} .


publish:
	docker login -u tbutzer
	docker push ${Image}


fix:
	sudo apt install gnupg2 pass
	echo for error sayving credentials
