generate-log:
	python3 log-generator.py

generate-log-interval:
	python3 log-generator.py -interval 20 -log-directory ~/Documents/sample.log -line 20

categorized-log:
	python3 log-categorized.py

json-convert-log:
	python3 log-json-convert.py

log-clean:
	bash ./remove.sh

compose-up:
	mkdir -p ./loki/data/index
	mkdir -p ./loki/data/boltdb-cache
	mkdir -p ./loki/data/chunks
	mkdir -p ./loki/data/wal
	mkdir -p ./loki/data/index/uploader
	mkdir -p ./loki/data/compactor

	sudo chown -R 1000:1000 ./loki/data
	sudo chmod -R 777 ./loki/data

	mkdir -p ./promtail/log
	sudo chown -R 1000:1000 ./promtail/log
	sudo chmod -R 777 ./promtail/log

	# docker-compose up -d
	docker-compose up --build -d


compose-down:
	docker-compose down
	rm -rf ./loki/data
	rm -rf ./promtail/log