import pytest
from flask import url_for


@pytest.fixture
def resp(client):
    return client.get(url_for('core.home'))


def test_bp_core_status_code(resp):
    assert resp.status_code == 200
