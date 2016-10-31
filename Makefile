PROJECT_NAME = revolv
STATIC_LIBS_DIR = ./$(PROJECT_NAME)/static/libs

default: lint test

test:
	# Run all tests and report coverage
	# Requires coverage
	coverage run manage.py test
	coverage report -m --fail-under 80

lint-py:
	# Check for Python formatting issues
	# Requires flake8
	flake8 .

lint-js:
	# Check JS for any problems
	# Requires jshint
	find -name "*.js" -not -path "${STATIC_LIBS_DIR}*" -print0 | xargs -0 jshint

lint: lint-py lint-js

$(STATIC_LIBS_DIR):
	mkdir -p $@

update-static-libs: $(LIBS)

# Generate a random string of desired length
generate-secret: length = 32
generate-secret:
	@strings /dev/urandom | grep -o '[[:alnum:]]' | head -n $(length) | tr -d '\n'; echo

conf/%.pub.ssh:
	# Generate SSH deploy key for a given environment
	ssh-keygen -t rsa -b 4096 -f $*.priv -C "$*@${PROJECT_NAME}"
	@mv $*.priv.pub $@

staging-deploy-key: conf/staging.pub.ssh

production-deploy-key: conf/production.pub.ssh

compilemessages:
	# Compile PO files into the MO files that Django will use at runtime
	python manage.py compilemessages

setup:
	virtualenv -p `which python2.7` venv
	venv/bin/pip install -U pip wheel
	venv/bin/pip install -Ur requirements/dev.txt
	npm install
	npm update
	cp revolv/settings/local.example.py revolv/settings/local.py
	echo "DJANGO_SETTINGS_MODULE=revolv.settings.local" > .env
	createdb -E UTF-8 revolv
	venv/bin/python manage.py migrate
	if [ -e project.travis.yml ] ; then mv project.travis.yml .travis.yml; fi
	@echo
	@echo "The revolv project is now set up on your machine."
	@echo "Run the following commands to activate the virtual environment and run the"
	@echo "development server:"
	@echo
	@echo " source venv/bin/activate"
	@echo "	npm run dev"

update:
	venv/bin/pip install -U -r requirements/dev.txt
	npm install
	npm update


.PHONY: default test lint lint-py lint-js generate-secret makemessages \
		pushmessages pullmessages compilemessages

.PRECIOUS: conf/%.pub.ssh
