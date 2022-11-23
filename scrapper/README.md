# Protocol Buffer Notes

To generate the go protobuff class, we run the following command:

``` shell
protoc --go_out=. --go-grpc_out=. types/job.proto
```

## Requirements

Install the protocol compiler _protoc_ and its plugins for Go using the following commands:

``` shell
go install google.golang.org/protobuf/cmd/protoc-gen-go@v1.28
go install google.golang.org/grpc/cmd/protoc-gen-go-grpc@v1.2
```

Update your PATH so that the protoc compiler can find the plugins:

``` shell
export PATH="$PATH:$GOPATH/bin"
```
