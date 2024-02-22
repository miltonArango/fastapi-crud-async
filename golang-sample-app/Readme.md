# Codefresh Go example

Original source: https://github.com/callicoder/go-docker

## Build locally

Multi-stage build (fully optimized) - image size is 16 MB

`docker build . -f Dockerfile.multistage -t go-sample-app-multi`

## Run locally

`docker run -p 8080:8080 go-sample-app-multi`

and then visit in your browser

* http://localhost:8080/
* http://localhost:8080/?name=John

## Build in Codefresh

Sample pipelines:

* [Simple pipeline](codefresh.yml)
* [Pipeline with Go modules and unit tests](codefresh-gomod.yml)
* [Multistage Docker image and embedded unit tests](codefresh-multi-stage.yml)

Read https://codefresh.io/docs/docs/learn-by-example/golang/golang-hello-world/ for more details



