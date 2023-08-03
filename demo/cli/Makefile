PIP_EXEC_PATH = bin/pip
PYTHON_EXEC_PATH = bin/python
CLI_DIR = app
VENV_DIR = venv

setup:
	rm -rf ${VENV_DIR}
	python3.9 -m venv ${VENV_DIR} \
			&& ${VENV_DIR}/${PIP_EXEC_PATH} install --upgrade pip \
			&& ${VENV_DIR}/${PIP_EXEC_PATH} install -r requirements.txt

run:
	PYTHONPATH=${CLI_DIR} ${VENV_DIR}/${PYTHON_EXEC_PATH} -m app
