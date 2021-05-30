# Copyright 2021 Hayden Young. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from pydantic import BaseSettings

version = "0.1.0-dev"
description = """
A simple, yet feature-complete pastebin system.
"""


class PasteSettings(BaseSettings):
    production: bool = False
    debug: bool = True
    name: str = "Pastr Paste"
    database_uri: str = "postgres://paste:paste@localhost:5432/paste"
    redis_uri: str = "redis://localhost"


settings = PasteSettings()


TORTOISE_ORM = {
    "connections": {"default": PasteSettings().database_uri},
    "apps": {
        "paste": {
            "models": [
                "paste.models",
                "aerich.models"
            ],
            "default_connection": "default"
        }
    }
}