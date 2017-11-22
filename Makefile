.PHONY: clean test all

all: test

test: data/birmingham_schools.csv
	tox

data/birmingham_schools.csv:
	mkdir -p data
	wget "https://data.birmingham.gov.uk/dataset/beb54f30-4942-40ce-b49f-b59f93986df9/resource/65d26f87-3e4f-495f-a6de-7018402edbb3/download/birminghamschools.csv" -O $@

clean:
	rm -rf data
