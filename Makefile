create-local-cluster:
	@kind create cluster
	@kubectl cluster-info --context kind-kind

delete-local-cluster:
	@kind delete cluster

local-run:
	@docker compose up

clean:
	@find . -name "__pycache__" -exec rm -rf {} \; >> /dev/null
