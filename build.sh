git submodule update --init --recursive
if [ ! -f "pyzetasql/server/service" ]; then
    cd zetasql
    PYTHON2_BIN_PATH=$(which python) PYTHONPATH=$(which python) bazelisk build --jobs 100 --incompatible_restrict_string_escapes=false --incompatible_require_linker_input_cc_api=false //zetasql/local_service:service
    cd -
fi
if [ ! -f "pyzetasql/proto/zetasql" ]; then
    cd zetasql
    PYTHON2_BIN_PATH=$(which python) PYTHONPATH=$(which python) bazelisk build --jobs 100 --incompatible_restrict_string_escapes=false //zetasql/local_service:local_service_python_grpc
    cd -
fi
if [ ! -f "pyzetasql/server/service" ]; then
    cp zetasql/bazel-bin/zetasql/local_service/service pyzetasql/server
fi
if [ ! -f "pyzetasql/proto/zetasql" ]; then
    rm -rf pyzetasql/proto/zetasql
    mkdir -p pyzetasql/proto/zetasql/local_service
    cp zetasql/bazel-bin/zetasql/local_service/*_pb2.py pyzetasql/proto/zetasql/local_service/
    cp zetasql/bazel-bin/zetasql/local_service/*_pb2_grpc.py pyzetasql/proto/zetasql/local_service/
    mkdir -p pyzetasql/proto/zetasql/public
    cp zetasql/bazel-bin/zetasql/public/*_pb2.py pyzetasql/proto/zetasql/public/
    mkdir -p pyzetasql/proto/zetasql/public/proto
    cp zetasql/bazel-bin/zetasql/public/proto/*_pb2.py pyzetasql/proto/zetasql/public/proto/
    mkdir -p pyzetasql/proto/zetasql/proto
    cp zetasql/bazel-bin/zetasql/proto/*_pb2.py pyzetasql/proto/zetasql/proto/
    mkdir -p pyzetasql/proto/zetasql/resolved_ast
    find zetasql/bazel-bin/zetasql/resolved_ast/ -type f | grep -i _pb2.py$ | xargs -i cp {} pyzetasql/proto/zetasql/resolved_ast/
fi