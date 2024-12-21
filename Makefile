COMPOSE_FILE = docker-compose.yml

start:
	docker-compose -f $(COMPOSE_FILE) up -d

stop:
	docker-compose -f $(COMPOSE_FILE) down

restart:
	docker-compose -f $(COMPOSE_FILE) down
	docker-compose -f $(COMPOSE_FILE) up -d

clean:
	docker-compose -f $(COMPOSE_FILE) down -v

help:
	@echo "Available targets:"
	@echo "  start   - Start the services in detached mode"
	@echo "  stop    - Stop and remove the services"
	@echo "  restart - Restart the services"
	@echo "  clean   - Stop and remove containers, networks, and volumes"
