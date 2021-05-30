# Copyright 2021 Hayden Young. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

import pytest

from typing import List

from fastapi.testclient import TestClient
from paste.main import create_app


@pytest.fixture
def client():
    with TestClient(create_app()) as tc:
        yield tc


# @pytest.mark.asyncio
def test_list_pastes(client: TestClient):
    res = client.get("/pastes")
    assert res.status_code == 200
    assert "message" in res.json()
    assert "data" in res.json()
    assert "error" in res.json()
    assert isinstance(res.json()['data'], List)


def test_create_paste(client: TestClient):
    res = client.post("/pastes/", json={"content": "Hey there friends!"})
    assert res.status_code == 201
    assert "message" in res.json()
    assert "data" in res.json()
    assert "error" in res.json()
    assert isinstance(res.json()['data'], str)
    assert len(res.json()['data']) == 18


def test_get_paste(client: TestClient):
    res = client.post("/pastes/", json={"content": "Hey there friends!"})
    id = res.json()['data']

    res = client.get(f"/pastes/{id}")
    assert res.status_code == 200
    assert "message" in res.json()
    assert "data" in res.json()
    assert res.json()['data']
    assert "error" in res.json()
    assert "content" in res.json()['data']
    assert res.json()['data']['content'] == "Hey there friends!"


def test_get_paste_not_found(client: TestClient):
    res = client.get("/pastes/0")
    assert res.status_code == 404
    assert res.json()['error'] == "paste_not_found"
    assert res.json()['message'] == "No such paste found."
    assert not res.json()['data']


def test_get_paste_raw(client: TestClient):
    res = client.post("/pastes/", json={"content": "Hey there friends!"})
    id = res.json()['data']

    res = client.get(f"/pastes/{id}/raw", headers={"accept": "text/plain"})
    assert res.status_code == 200
    assert isinstance(res.content, bytes)
    assert res.content.decode('utf-8')
    assert res.content.decode('utf-8') == "Hey there friends!"
    assert res.headers['Content-Type'] == "text/plain; charset=utf-8"


def test_get_paste_raw_not_found(client: TestClient):
    res = client.get("/pastes/0")
    assert res.status_code == 404
    assert res.json()['error'] == "paste_not_found"
    assert res.json()['message'] == "No such paste found."
    assert not res.json()['data']
