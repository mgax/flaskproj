from flask import url_for
import pytest


@pytest.fixture
def myfixture():
    return "hello world"


def test_homepage(client, myfixture):
    assert myfixture == "hello world"
    url = url_for("home")
    response = client.get(url)
    assert response.status_code == 200
    assert response.text == "Hello from flaskproj!"
