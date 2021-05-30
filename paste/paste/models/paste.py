# Copyright 2021 Hayden Young. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from datetime import datetime
from typing import Optional
from tortoise import fields
from tortoise.models import Model
from tortoise.contrib.pydantic.creator import pydantic_model_creator


class Pastes(Model):
    """
    An individual paste
    """

    id: int = fields.BigIntField(pk=True)

    content: str = fields.TextField()
    private = fields.BooleanField(default=False)

    created_at: datetime = fields.DatetimeField(auto_now_add=True)
    updated_at: Optional[datetime] = fields.DatetimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]


Paste_Pydantic = pydantic_model_creator(Pastes, name="Paste")
PasteIn_Pydantic = pydantic_model_creator(
    Pastes,
    name="PasteIn",
    exclude_readonly=True,
    exclude=("created_at", "updated_at")
)
