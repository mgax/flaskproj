from flask import url_for


def test_sum(client):
    url = url_for("sum")
    response = client.get(url, query_string={"a": 1, "b": 2})
    assert response.status_code == 200
    assert response.json == {"result": 3}


# - coverage
# - ruff
