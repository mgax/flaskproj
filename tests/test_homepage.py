from flask import url_for
import pytest
from bs4 import BeautifulSoup


@pytest.fixture
def myfixture():
    return "hello world"


def test_homepage(client, myfixture):
    assert myfixture == "hello world"
    url = url_for("home")
    response = client.get(url)
    assert response.status_code == 200
    assert "Hello from flaskproj!" in response.text


@pytest.mark.parametrize("banner_text", ["Other text", "Hello from flaskproj!"])
def test__banner_is_configurable(client, config, banner_text):
    config["BANNER_TEXT"] = banner_text
    url = url_for("home")
    response = client.get(url)
    assert response.status_code == 200
    
    soup = BeautifulSoup(response.text, 'html.parser')
    banner_text = soup.find('h1').text
    assert banner_text == banner_text
