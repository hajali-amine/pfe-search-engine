b=all

build:
	@echo "What image would you like to build?\nWrite 'a' to build all of the images" ; \
	read r ; \
	if [ "$$r" = "a" ] ; then \
		./scripts/build.sh -a ; \
	else \
		./scripts/build.sh -i $$r ; \
	fi ; \

push:
	@echo "What image would you like to push?\nWrite 'a' to push all of the images" ; \
	read r ; \
	if [ "$$r" = "a" ] ; then \
		./scripts/push.sh -a ; \
	else \
		./scripts/push.sh -i $$r ; \
	fi ; \

docker-run:
	@docker run aminehajali/se-$i

create-local-cluster:
	@kind create cluster
	@kubectl cluster-info --context kind-kind

delete-local-cluster:
	@kind delete cluster

local-run:
	@docker compose up

clean:
	@find . -name "__pycache__" -exec rm -rf {} \; >> /dev/null
