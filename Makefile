generate-log:
	python3 log-generator.py

categorized-log:
	python3 log-categorized.py

json-convert-log:
	python3 log-json-convert.py

log-clean:
	bash ./remove.sh

logging-up:
	mkdir -p ./loki/data/index
	mkdir -p ./loki/data/boltdb-cache
	mkdir -p ./loki/data/chunks
	mkdir -p ./loki/data/wal
	mkdir -p ./loki/data/index/uploader
	mkdir -p ./loki/data/compactor

	sudo chown -R 1000:1000 ./loki/data
	sudo chmod -R 777 ./loki/data

	docker-compose up -d

logging-down:
	docker-compose down
	rm -rf ./loki/data