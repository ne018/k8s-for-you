## Building the container
` $ docker build -f Dockerfile -t $DOCKER_USER_ID/sample-frontend . `

## Running the container
` $ docker run -d -p 80:80 $DOCKER_USER_ID/sample-frontend `

## Pushing the container
` $ docker push $DOCKER_USER_ID/sample-frontend `