SHELL := /bin/bash

# Colors
CCGREEN=\033[0;32m
CCYELLOW=\033[0;33m
CCRED=\033[0;31m
CCEND=\033[0m

# src=test-code/syntax-analysis/success.c
src=test-code/syntax-analysis/printstat.c
program_1=test-code/program1.c
program_2=test-code/program2.c
program_3=test-code/program3.c
program_4=test-code/program4.c

.PHONY:
all: install-poetry install run

.PHONY:
install-poetry:
	@echo -e "${CCGREEN}Installing Poetry...${CCEND}"
	@curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3 -
	@echo -e "${CCGREEN}Done!${CCEND}"
	@source ~/.poetry/env

.PHONY:
install:
	@echo -e "${CCGREEN}Installing dependencies...${CCEND}"
	@poetry install
	@echo -e "${CCGREEN}Done!${CCEND}"


.PHONY:
run:
	@echo -e "${CCGREEN}Creating output/ ${CCEND}"
	@mkdir -p output/

	@echo -e ""
	@echo -e "${CCYELLOW}--- Type Verification Test --- ${CCEND}"

	@echo -e "${CCGREEN}Executing test-code/semantic-analysis/valid-operations.c > output/operations.txt${CCEND}"
	@poetry run python src/main.py --src test-code/semantic-analysis/valid-operations.c --print-typecheck > output/operations.txt
	@echo -e "${CCGREEN}test-code/semantic-analysis/valid-operations.c does not have invalid operations.${CCEND}"

	@echo -e "${CCYELLOW}--- Variable Declaration by Scope Test --- ${CCEND}"

	@echo -e "${CCGREEN}Executing test-code/semantic-analysis/valid-variable-declaration.c > output/variable-declaration.txt${CCEND}"
	@poetry run python src/main.py --src test-code/semantic-analysis/valid-variable-declaration.c > output/variable-declaration.txt
	@echo -e "${CCGREEN}test-code/semantic-analysis/valid-variable-declaration.c does not have invalid variable declaration.${CCEND}"

	@echo -e "${CCYELLOW}--- Break Operator Test --- ${CCEND}"

	@echo -e "${CCGREEN}Executing test-code/semantic-analysis/valid-break-operator.c > output/break-operator.txt${CCEND}"
	@poetry run python src/main.py --src test-code/semantic-analysis/valid-break-operator.c > output/break-operator.txt
	@echo -e "${CCGREEN}test-code/semantic-analysis/valid-break-operator.c does not have invalid 'break's.${CCEND}"

	@echo -e "${CCYELLOW}--- Executing test programs --- ${CCEND}"

	@echo -e "${CCGREEN}Executing program1.c${CCEND}"
	@poetry run python src/main.py --src ${program_1} > output/program1.txt

	@echo -e "${CCGREEN}Executing program2.c${CCEND}"
	@poetry run python src/main.py --src ${program_2} > output/program2.txt

	@echo -e "${CCGREEN}Executing program3.c${CCEND}"
	@poetry run python src/main.py --src ${program_3} > output/program3.txt

	@echo -e "${CCGREEN}Executing program4.c${CCEND}"
	@poetry run python src/main.py --src ${program_4} > output/program4.txt

	@echo -e "${CCGREEN}Done! Outputs can be found at output/${CCEND}"


.PHONY:
example:
	@echo -e "${GREEN}Executando main lexer.py...${CCEND}"
	@echo -e "Se voce nao especificou um programa fonte"
	@echo -e "um arquivo de exemplo sera utilizado."
	@echo -e "Voce pode muda-lo utilizando o comando ${CCYELLOW}make run src=<path/to/file>${CCEND}"

	@echo -e "${CCYELLOW}Executando o arquivo de exemplo...${CCEND}"
	@poetry run python src/main.py --src ${src}
