# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

from ..rule_param import RuleParam

__all__ = ["ActionSetRulesParams"]


class ActionSetRulesParams(TypedDict, total=False):
    rules: Required[List[RuleParam]]
    """Array of rules"""
