default: ## Run app
	. ./venv/bin/activate && python __main__.py

env: ## Sets up an environment
	@-virtualenv venv
	. ./venv/bin/activate && pip install -r requirements.txt

freeze: ## Freeze python dependencies
	@. ./venv/bin/activate && pip freeze > requirements.txt

help: ## Prints help for targets with comments
	@cat $(MAKEFILE_LIST) | grep -E '^[a-zA-Z_-]+:.*?## .*$$' | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
