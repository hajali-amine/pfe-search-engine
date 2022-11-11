b=all

build:
	@if [ $b = "all" ] ; then docker build -t aminehajali/se-front ./front && docker build -t aminehajali/se-back ./back ; fi
	@if [ ! $b = "all" ] ; then docker build -t aminehajali/se-$b ./$b ; fi

push: build
	@if [ $b = "all" ] ; then docker push aminehajali/se-front && docker push aminehajali/se-back ; fi
	@if [ ! $b = "all" ] ; then docker push aminehajali/se-$b ; fi

create-local-cluster:
	@kind create cluster
	@kubectl cluster-info --context kind-kind

delete-local-cluster:
	@kind delete cluster

local-run:
	@docker compose up

clean:
	@find . -name "__pycache__" -exec rm -rf {} \; >> /dev/null
