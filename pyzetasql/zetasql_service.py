import sys
import pathlib
import subprocess
import grpc
from pyzetasql.proto.zetasql.local_service import local_service_pb2_grpc

__process: subprocess.Popen = None


def run_server():
    global __process
    if __process is None:
        service_path = pathlib.Path().absolute().joinpath('pyzetasql/server/service')
        __process = subprocess.Popen([str(service_path)], stdout=sys.stdout, stderr=sys.stderr)


def close_server():
    global __process
    if __process is not None:
        __process.terminate()
        __process.wait()
        __process = None


def get_client():
    channel = grpc.insecure_channel('localhost:4050')
    return local_service_pb2_grpc.ZetaSqlLocalServiceStub(channel)
