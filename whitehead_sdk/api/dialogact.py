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


# fmt: off
QUERY: List[str] = ["""
query dialogact($input: String!) {
  callDialogact(input: $input) {
    result
  }
}

"""
]


class dialogact:
    @dataclass(frozen=True)
    class dialogactData(DataClassJsonMixin):
        @dataclass(frozen=True)
        class DialogactResult(DataClassJsonMixin):
            result: str

        callDialogact: DialogactResult

    # fmt: off
    @classmethod
    def execute(cls, client: Client, input: str) -> dialogactData.DialogactResult:
        variables: Dict[str, Any] = {"input": input}
        new_variables = encode_variables(variables, custom_scalars)
        response_text = client.execute(
            gql("".join(set(QUERY))), variable_values=new_variables
        )
        res = cls.dialogactData.from_dict(response_text)
        return res.callDialogact

    # fmt: off
    @classmethod
    async def execute_async(cls, client: Client, input: str) -> dialogactData.DialogactResult:
        variables: Dict[str, Any] = {"input": input}
        new_variables = encode_variables(variables, custom_scalars)
        response_text = await client.execute_async(
            gql("".join(set(QUERY))), variable_values=new_variables
        )
        res = cls.dialogactData.from_dict(response_text)
        return res.callDialogact
