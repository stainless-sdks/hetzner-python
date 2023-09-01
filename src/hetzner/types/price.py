# File generated from our OpenAPI spec by Stainless.

from .._models import BaseModel

__all__ = ["Price"]


class Price(BaseModel):
    gross: str
    """Price with VAT added"""

    net: str
    """Price without VAT"""
