SHELL := /bin/bash

# Colors
CCGREEN=\033[0;32m
CCYELLOW=\033[0;33m
CCRED=\033[0;31m
CCEND=\033[0m

.PHONY:
all: run

.PHONY:
install-poetry:
	@echo -e "${CCGREEN}Installing Poetry...${CCEND}"
	@curl -sSL https://install.python-poetry.org | python3 -
	@echo -e "${CCGREEN}Done!${CCEND}"

.PHONY:
install:
	@echo -e "${CCGREEN}Downloading dependencies using Poetry...${CCEND}"
	@poetry install
	@echo -e "${CCGREEN}Done!${CCEND}"

.PHONY:
run:
	@echo -e "${CCGREEN}Beggining lexical analysis!${CCEND}"
	@poetry run python main.py
	@echo -e "${CCGREEN}You can find the results at output/${CCEND}"