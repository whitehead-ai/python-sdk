#!/usr/bin/env python3
# @generated AUTOGENERATED file. Do not Change!

from dataclasses import dataclass, field as _field
from ..schema_config.json_scalar import custom_scalars
from gql_client.runtime.variables import encode_variables
from gql import gql, Client
from gql.transport.exceptions import TransportQueryError
from functools import partial
from numbers import Number
from typing import Any, AsyncGenerator, Dict, List, Generator, Optional
from time import perf_counter
from dataclasses_json import DataClassJsonMixin, config

from .input.turn import Turn


# fmt: off
QUERY: List[str] = ["""
query parseContext($history: [Turn!]!) {
  result: callParseContext(history: $history) {
    context: result {
      input
      mentions {
        evokes
        phrase
      }
    }
  }
}

"""
]


class parseContext:
    @dataclass(frozen=True)
    class parseContextData(DataClassJsonMixin):
        @dataclass(frozen=True)
        class ContextResult(DataClassJsonMixin):
            @dataclass(frozen=True)
            class SlingDocument(DataClassJsonMixin):
                @dataclass(frozen=True)
                class SlingMention(DataClassJsonMixin):
                    evokes: Optional[List[str]]
                    phrase: Optional[str]

                input: Optional[str]
                mentions: Optional[List[SlingMention]]

            context: Optional[List[SlingDocument]]

        result: Optional[ContextResult]

    # fmt: off
    @classmethod
    def execute(cls, client: Client, history: List[Turn] = []) -> Optional[parseContextData.ContextResult]:
        variables: Dict[str, Any] = {"history": history}
        new_variables = encode_variables(variables, custom_scalars)
        response_text = client.execute(
            gql("".join(set(QUERY))), variable_values=new_variables
        )
        res = cls.parseContextData.from_dict(response_text)
        return res.result

    # fmt: off
    @classmethod
    async def execute_async(cls, client: Client, history: List[Turn] = []) -> Optional[parseContextData.ContextResult]:
        variables: Dict[str, Any] = {"history": history}
        new_variables = encode_variables(variables, custom_scalars)
        response_text = await client.execute_async(
            gql("".join(set(QUERY))), variable_values=new_variables
        )
        res = cls.parseContextData.from_dict(response_text)
        return res.result
