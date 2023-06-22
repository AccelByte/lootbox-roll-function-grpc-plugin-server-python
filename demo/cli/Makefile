PIP_EXEC_PATH = bin/pip
PYTHON_EXEC_PATH = bin/python
CLI_DIR = app
VENV_DIR = venv

setup:
	rm -rf ${VENV_DIR}
		docker run --rm -t -u $$(id -u):$$(id -g) -v $$(pwd):/data -w /data -e PIP_CACHE_DIR=/data/.cache/pip --entrypoint /bin/sh python:3.9-slim \
				-c 'python -m venv ${VENV_DIR} \
						&& ${VENV_DIR}/${PIP_EXEC_PATH} install --upgrade pip \
						&& ${VENV_DIR}/${PIP_EXEC_PATH} install -r requirements.txt'

run:
	docker run --rm -t -u $$(id -u):$$(id -g) -v $$(pwd):/data -w /data -e PIP_CACHE_DIR=/data/.cache/pip --entrypoint /bin/sh python:3.9-slim \
			-c 'PYTHONPATH=${CLI_DIR} ${VENV_DIR}/${PYTHON_EXEC_PATH} -m app'
