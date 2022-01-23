import pytest
from pyzetasql import zetasql_service
from pyzetasql.proto.zetasql.local_service import local_service_pb2


@pytest.fixture(autouse=True)
def setup_and_teardown():
    try:
        zetasql_service.run_server()
        yield
    finally:
        zetasql_service.close_server()


def test_run_server():
    pass


def test_communicate_server():
    client = zetasql_service.get_client()
    req = local_service_pb2.FormatSqlRequest()
    req.sql = 'SELECT 1 + 1;'
    res = client.FormatSql(req)
    assert res.sql == "SELECT\n  1 + 1;"
