# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from .shared import Action
from .._models import BaseModel
from .firewall import Firewall

__all__ = ["FirewallCreateResponse"]


class FirewallCreateResponse(BaseModel):
    actions: Optional[List[Action]] = None

    firewall: Optional[Firewall] = None
    """Firewalls can limit the network access to or from your resources."""
