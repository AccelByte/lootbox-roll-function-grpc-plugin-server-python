PIP_EXEC_PATH = bin/pip
PROTO_DIR = app/proto
PYTHON_EXEC_PATH = bin/python
SOURCE_DIR = src
TESTS_DIR = tests
VENV_DIR = venv
VENV_DEV_DIR = venv-dev

IMAGE_NAME := $(shell basename "$$(pwd)")-app
BUILDER := grpc-plugin-server-builder

setup:
	rm -rf ${VENV_DEV_DIR}
	docker run --rm -t -u $$(id -u):$$(id -g) -v $$(pwd):/data -w /data -e PIP_CACHE_DIR=/data/.cache/pip --entrypoint /bin/sh python:3.9-slim \
			-c 'python -m venv ${VENV_DEV_DIR} \
					&& ${VENV_DEV_DIR}/${PIP_EXEC_PATH} install --upgrade pip \
					&& ${VENV_DEV_DIR}/${PIP_EXEC_PATH} install -r requirements-dev.txt'

	rm -rf ${VENV_DIR}
		docker run --rm -t -u $$(id -u):$$(id -g) -v $$(pwd):/data -w /data -e PIP_CACHE_DIR=/data/.cache/pip --entrypoint /bin/sh python:3.9-slim \
				-c 'python -m venv ${VENV_DIR} \
						&& ${VENV_DIR}/${PIP_EXEC_PATH} install --upgrade pip \
						&& ${VENV_DIR}/${PIP_EXEC_PATH} install -r requirements.txt'

clean:
	rm -f ${SOURCE_DIR}/${PROTO_DIR}/*_grpc.py
	rm -f ${SOURCE_DIR}/${PROTO_DIR}/*_pb2.py
	rm -f ${SOURCE_DIR}/${PROTO_DIR}/*_pb2.pyi
	rm -f ${SOURCE_DIR}/${PROTO_DIR}/*_pb2_grpc.py

proto: clean
	docker run -t --rm -u $$(id -u):$$(id -g) -v $$(pwd):/data/ -w /data/ rvolosatovs/protoc:4.0.0 \
		--proto_path=${PROTO_DIR}=${SOURCE_DIR}/${PROTO_DIR} \
		--python_out=${SOURCE_DIR} \
		--grpc-python_out=${SOURCE_DIR} \
		${SOURCE_DIR}/${PROTO_DIR}/*.proto

build: proto

image:
	docker buildx build -t ${IMAGE_NAME} --load .

imagex:
	docker buildx inspect $(BUILDER) || docker buildx create --name $(BUILDER) --use
	docker buildx build -t ${IMAGE_NAME} --platform linux/arm64/v8,linux/amd64 .
	docker buildx build -t ${IMAGE_NAME} --load .
	docker buildx rm --keep-state $(BUILDER)

imagex_push:
	@test -n "$(IMAGE_VERSION)" || (echo "IMAGE_VERSION is not set"; exit 1)
	docker buildx inspect $(BUILDER) || docker buildx create --name $(BUILDER) --use
	docker buildx build -t ${IMAGE_PREFIX}${IMAGE_NAME}:${IMAGE_VERSION} --platform linux/arm64/v8,linux/amd64 --push .
	docker buildx rm --keep-state $(BUILDER)