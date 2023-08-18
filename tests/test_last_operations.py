import utils
import pytest
import os


@pytest.fixture
def os_fixture():
    return os.path.join('operations.json')


def test_last_operations(os_fixture):
    assert type(utils.last_operations(os_fixture)) is list
