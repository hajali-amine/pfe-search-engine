# Protocol Buffer Notes

To generate the python protobuff class, we run the following command:

``` shell
$ protoc --proto_path=data_loader/types --python_out=data_loader/types data_loader/types/job.proto
```
