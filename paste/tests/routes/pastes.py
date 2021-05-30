# Copyright 2021 Hayden Young. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import List
from tests import client


def test_list_pastes():
    res = client.get("/pastes")
    assert res.status_code == 200
    assert "message" in res.json()
    assert "data" in res.json()
    assert "error" in res.json()
    assert isinstance(res.json()['data'], List)
