import sys
import subprocess


def build(setup_kwargs):
    scripts = '''
cd zetasql && \
PYTHON2_BIN_PATH=$(which python) PYTHONPATH=$(which python) bazel build --jobs 100 --incompatible_restrict_string_escapes=false --incompatible_require_linker_input_cc_api=false //zetasql/local_service:service && \
PYTHON2_BIN_PATH=$(which python) PYTHONPATH=$(which python) bazel build --jobs 100 --incompatible_restrict_string_escapes=false //zetasql/local_service:local_service_python_grpc && \
cd - && \
rm -rf pyzetasql/proto/zetasql && \
cp zetasql/bazel-bin/zetasql/local_service/service pyzetasql/server && \
mkdir -p pyzetasql/proto/zetasql/local_service && \
cp zetasql/bazel-bin/zetasql/local_service/*_pb2.py pyzetasql/proto/zetasql/local_service/ && \
cp zetasql/bazel-bin/zetasql/local_service/*_pb2_grpc.py pyzetasql/proto/zetasql/local_service/ && \
mkdir -p pyzetasql/proto/zetasql/public && \
cp zetasql/bazel-bin/zetasql/public/**/*_pb2.py pyzetasql/proto/zetasql/public/ && \
mkdir -p pyzetasql/proto/zetasql/public/proto && \
cp zetasql/bazel-bin/zetasql/public/proto/**/*_pb2.py pyzetasql/proto/zetasql/public/proto/ && \
mkdir -p pyzetasql/proto/zetasql/proto && \
cp zetasql/bazel-bin/zetasql/proto/**/*_pb2.py pyzetasql/proto/zetasql/proto/ && \
mkdir -p pyzetasql/proto/zetasql/resolved_ast && \
cp zetasql/bazel-bin/zetasql/resolved_ast/**/*_pb2.py pyzetasql/proto/zetasql/resolved_ast/
    '''
    subprocess.check_call(scripts, shell=True, stdout=sys.stdout, stderr=sys.stderr)
