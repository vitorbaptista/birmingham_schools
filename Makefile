.PHONY: clean test all

all: test

test: data
	tox

data: data/birmingham_schools.csv

data/birmingham_schools.csv:
	mkdir -p data
	wget "https://data.birmingham.gov.uk/dataset/beb54f30-4942-40ce-b49f-b59f93986df9/resource/65d26f87-3e4f-495f-a6de-7018402edbb3/download/birminghamschools.csv" -O $@
	python3 scripts/clean_data.py $@

clean:
	rm -rf data
