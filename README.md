# pyzetasql


## BUILD

Use bazel-1.0.0

```sh
cd zetasql
bazel-1.0.0 build --jobs 100 //zetasql/local_service:service
bazel-1.0.0 build --jobs 100 //zetasql/local_service:local_service_python_proto
cd -
cp zetasql/bazel-bin/zetasql/local_service/service pyzetasql/server
mkdir -p pyzetasql/proto/zetasql/local_service
cp zetasql/bazel-bin/zetasql/local_service/*_pb2.py pyzetasql/proto/zetasql/local_service/
cp zetasql/bazel-bin/zetasql/local_service/*_pb2_grpc.py pyzetasql/proto/zetasql/local_service/
mkdir -p pyzetasql/proto/zetasql/public
cp zetasql/bazel-bin/zetasql/public/**/*_pb2.py pyzetasql/proto/zetasql/public/
mkdir -p pyzetasql/proto/zetasql/public/proto
cp zetasql/bazel-bin/zetasql/public/proto/**/*_pb2.py pyzetasql/proto/zetasql/public/proto/
mkdir -p pyzetasql/proto/zetasql/proto
cp zetasql/bazel-bin/zetasql/proto/**/*_pb2.py pyzetasql/proto/zetasql/proto/
mkdir -p pyzetasql/proto/zetasql/resolved_ast
cp zetasql/bazel-bin/zetasql/resolved_ast/**/*_pb2.py pyzetasql/proto/zetasql/resolved_ast/
```