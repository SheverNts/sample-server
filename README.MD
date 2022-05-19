# Simple Flask Server:

This is simple flask app that listens on port 80 and responds on the route.

### Dependency

Below packages are the dependency for this project

1) Helm
2) Docker
3) Minkube


## To Build New Image
```bash
export DOCKER_HUB_USERNAME=<docker username>
export DOCKER_HUB_PASSWORD=<docker password>
sh Build_Deploy/built_at

```

# Run app With Docker

```bash
docker run -it -p 80:80 <repository>:<tag>
ex:
docker run -d -p 80:80 test-app:0.0.1

Output:
>> curl http://localhost
{"built_at":1627037312,"deployed_at":1627037348,"hello":"world"}
```


## To Deploy New Service
```bash

sh Build_Deploy/deployed_at <repository> <tag>

ex:
sh Build_Deploy/deployed_at "shevernts/test-app:0.0.1"
```

## To access the app
```bash

POD_NAME=$(kubectl get pods -l app.kubernetes.io/name=test-app -o custom-columns=:metadata.name -n default --no-headers)

kubectl --namespace default port-forward ${POD_NAME}  80:80
```