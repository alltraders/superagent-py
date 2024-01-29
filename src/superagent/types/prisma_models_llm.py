# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .llm_provider import LlmProvider

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class PrismaModelsLlm(pydantic.BaseModel):
    """
    Represents a LLM record
    """

    id: str
    provider: LlmProvider
    api_key: str = pydantic.Field(alias="apiKey")
    options: typing.Optional[typing.Any]
    agents: typing.Optional[typing.List[PrismaModelsAgentLlm]]
    created_at: dt.datetime = pydantic.Field(alias="createdAt")
    updated_at: dt.datetime = pydantic.Field(alias="updatedAt")
    api_user_id: str = pydantic.Field(alias="apiUserId")
    api_user: typing.Optional[PrismaModelsApiUser] = pydantic.Field(alias="apiUser")

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        json_encoders = {dt.datetime: serialize_datetime}


from .prisma_models_agent_llm import PrismaModelsAgentLlm  # noqa: E402
from .prisma_models_api_user import PrismaModelsApiUser  # noqa: E402

PrismaModelsLlm.update_forward_refs()
