# Copyright 2021 Hayden Young. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

# from base64 import b64encode
# from datetime import datetime
from typing import List, Optional

from paste.models import APIResponse
from paste.models.paste import PasteIn_Pydantic, Paste_Pydantic, Pastes
from fastapi import APIRouter, status, Response, File
from sonyflake import SonyFlake
from tortoise.exceptions import DoesNotExist

router = APIRouter(prefix="/pastes")


class ListIndex(APIResponse):
    data: List[Paste_Pydantic]


class CreateResponse(APIResponse):
    data: Paste_Pydantic


class SingleResponse(APIResponse):
    data: Optional[Paste_Pydantic]


@router.get("/", response_model=ListIndex)
async def list_pastes() -> APIResponse:
    pastes = await Paste_Pydantic.from_queryset(Pastes.all())
    return APIResponse(**{"message": f"Found {len(pastes)} paste(s).", "data": pastes})


@router.post("/", response_model=CreateResponse, status_code=201)
async def create_paste(paste: PasteIn_Pydantic, response: Response) -> APIResponse:
    paste_dict = paste.dict(exclude_unset=True)
    paste_dict['id'] = SonyFlake().next_id()
    paste_obj = await Pastes.create(**paste_dict)
    response.status_code = status.HTTP_201_CREATED
    return APIResponse(**{
        "message": "Successfully created a new paste.",
        "data": await Paste_Pydantic.from_tortoise_orm(paste_obj)
    })


@router.get("/{id}", response_model=SingleResponse, responses={404: {"model": APIResponse}})
async def get_paste(id: int, response: Response):
    try:
        pastes = await Pastes.get(id=id)
        return SingleResponse(**{
            "message": f"Successfully found a paste for ID {id}.",
            "data": await Paste_Pydantic.from_tortoise_orm(pastes)
        })
    except DoesNotExist:
        response.status_code = 404
        return SingleResponse(**{
            "message": "No such paste found.",
            "data": None,
            "error": "paste_not_found"
        })
