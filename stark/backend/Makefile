.PHONY: requirements run build up


help:  ## Display this help
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n\nTargets:\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-10s\033[0m %s\n", $$1, $$2 }' $(MAKEFILE_LIST)

requirements: ## builds requirements.txt from poetry
	poetry export -f requirements.txt > requirements.txt

run: ## runs locally on port 8000
	poetry run uvicorn main:app --reload

build: ## builds docker images
	docker-compose build

up: ## spin development server in development mode at port 8009 using docker
	docker-compose up
