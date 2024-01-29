# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .llm_provider import LlmProvider

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class AppModelsRequestAgent(pydantic.BaseModel):
    is_active: typing.Optional[bool] = pydantic.Field(alias="isActive")
    name: str
    initial_message: typing.Optional[str] = pydantic.Field(alias="initialMessage")
    prompt: typing.Optional[str]
    llm_model: typing.Optional[str] = pydantic.Field(alias="llmModel")
    llm_provider: typing.Optional[LlmProvider] = pydantic.Field(alias="llmProvider")
    description: str
    avatar: typing.Optional[str]

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
