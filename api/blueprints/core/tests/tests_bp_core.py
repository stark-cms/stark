import pytest

from flask import url_for


@pytest.fixture
def resp(client):
    return client.get(url_for('core.home'))


def test_bp_home_status_code_ok(resp):
    assert resp.status_code == 200
