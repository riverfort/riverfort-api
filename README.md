# api-rf

## Setup virtual environment
```
cd riverfort-api
python3 -m venv venv
source venv/bin/activate
```

## Install
```
cd riverfort-api
pip install -r requirements.txt
```

## Create .env
See .env.example and supply values
```
touch .env
```

## Deployment
The command for build a docker image is: 
```
docker build -t riverfort/riverfort-api:<VERSION> .
```

The command for run the docker image is: 
```
docker run -d \
--name riverfort-api-<VERSION> \
--env-file env \
-p 80:8000 \
sriverfort/riverfort-api:<VERSION>
```
where:
* `<VERSION>` is a string, e.g. `docker build -t riverfort/riverfort-api:v1.0.0 .`
* `env` is a file containing a list of environment variables and their values, e.g. see `.env.example`.

The command for push the image to registry (DockerHub) is:
```
docker push riverfort/riverfort-api:<VERSION>
```