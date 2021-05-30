# Copyright 2021 Hayden Young. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from fastapi import FastAPI, APIRouter
from paste.routes.pastes import router

_base_router = APIRouter()


def register_routes(app: FastAPI) -> None:
    _base_router.include_router(router)

    app.include_router(_base_router)
