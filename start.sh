
TAG=llamapy

docker build -t $TAG .

# run

NAME=$TAG

docker run \
  -ti \
  --rm \
  -v ${PWD}/models:/models \
  -v ${PWD}/datasets:/datasets \
  $TAG
