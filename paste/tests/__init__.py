# Copyright 2021 Hayden Young. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from fastapi.testclient import TestClient
from paste.main import app

client = TestClient(app)
