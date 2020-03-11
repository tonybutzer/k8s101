build:
	docker build -t tbutzer/flasksidecar .
	docker login -u tbutzer
	docker push tbutzer/flasksidecar

#And then run the container from the image:

run:
	docker run -d -p 5000:5000 tbutzer/flasksidecar


build2:
	docker build -f Dockerfile.nginx -t tbutzer/reverse .
	docker login -u tbutzer
	docker push tbutzer/reverse
