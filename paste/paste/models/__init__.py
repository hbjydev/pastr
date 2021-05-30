# Copyright 2021 Hayden Young. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Any, Optional
from pydantic import BaseModel
from paste.models.paste import Pastes, Paste_Pydantic, PasteIn_Pydantic


class APIResponse(BaseModel):
    message: str
    data: Optional[Any]
    error: Optional[str]
