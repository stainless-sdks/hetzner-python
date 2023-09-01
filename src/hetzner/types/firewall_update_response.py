# File generated from our OpenAPI spec by Stainless.

from .._models import BaseModel
from .firewall import Firewall

__all__ = ["FirewallUpdateResponse"]


class FirewallUpdateResponse(BaseModel):
    firewall: Firewall
    """Firewalls can limit the network access to or from your resources."""
