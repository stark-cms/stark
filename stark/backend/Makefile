.PHONY: requirements run

requirements:
	poetry export -f requirements.txt > requirements.txt

run:
	poetry run uvicorn main:app --reload