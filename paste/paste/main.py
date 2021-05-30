# Copyright 2021 Hayden Young. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from paste.routes import register_routes
from fastapi import FastAPI
from paste.settings import TORTOISE_ORM, version, description, PasteSettings
from tortoise.contrib.fastapi import register_tortoise


def create_app() -> FastAPI:
    app = FastAPI(
        description=description,
        title=PasteSettings().name,
        version=version,
    )

    register_routes(app)
    register_tortoise(app, TORTOISE_ORM)

    return app


app = create_app()
