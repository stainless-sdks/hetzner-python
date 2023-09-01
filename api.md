# Shared Types

```python
from hetzner.types import Action, HealthStatus, ResponseMeta, SortParam, StatusParam
```

# Actions

Types:

```python
from hetzner.types import ActionRetrieveResponse, ActionListResponse
```

Methods:

- <code title="get /actions/{id}">client.actions.<a href="./src/hetzner/resources/actions.py">retrieve</a>(id) -> <a href="./src/hetzner/types/action_retrieve_response.py">ActionRetrieveResponse</a></code>
- <code title="get /actions">client.actions.<a href="./src/hetzner/resources/actions.py">list</a>(\*\*<a href="src/hetzner/types/action_list_params.py">params</a>) -> <a href="./src/hetzner/types/action_list_response.py">ActionListResponse</a></code>

# Certificates

Types:

```python
from hetzner.types import (
    Certificate,
    CertificateCreateResponse,
    CertificateRetrieveResponse,
    CertificateUpdateResponse,
    CertificateListResponse,
)
```

Methods:

- <code title="post /certificates">client.certificates.<a href="./src/hetzner/resources/certificates/certificates.py">create</a>(\*\*<a href="src/hetzner/types/certificate_create_params.py">params</a>) -> <a href="./src/hetzner/types/certificate_create_response.py">CertificateCreateResponse</a></code>
- <code title="get /certificates/{id}">client.certificates.<a href="./src/hetzner/resources/certificates/certificates.py">retrieve</a>(id) -> <a href="./src/hetzner/types/certificate_retrieve_response.py">CertificateRetrieveResponse</a></code>
- <code title="put /certificates/{id}">client.certificates.<a href="./src/hetzner/resources/certificates/certificates.py">update</a>(id, \*\*<a href="src/hetzner/types/certificate_update_params.py">params</a>) -> <a href="./src/hetzner/types/certificate_update_response.py">CertificateUpdateResponse</a></code>
- <code title="get /certificates">client.certificates.<a href="./src/hetzner/resources/certificates/certificates.py">list</a>(\*\*<a href="src/hetzner/types/certificate_list_params.py">params</a>) -> <a href="./src/hetzner/types/certificate_list_response.py">CertificateListResponse</a></code>
- <code title="delete /certificates/{id}">client.certificates.<a href="./src/hetzner/resources/certificates/certificates.py">delete</a>(id) -> None</code>

## Actions

Types:

```python
from hetzner.types.certificates import (
    ActionRetrieveResponse,
    ActionListResponse,
    ActionRetryResponse,
)
```

Methods:

- <code title="get /certificates/{id}/actions/{action_id}">client.certificates.actions.<a href="./src/hetzner/resources/certificates/actions.py">retrieve</a>(id, action_id) -> <a href="./src/hetzner/types/certificates/action_retrieve_response.py">ActionRetrieveResponse</a></code>
- <code title="get /certificates/{id}/actions">client.certificates.actions.<a href="./src/hetzner/resources/certificates/actions.py">list</a>(id, \*\*<a href="src/hetzner/types/certificates/action_list_params.py">params</a>) -> <a href="./src/hetzner/types/certificates/action_list_response.py">ActionListResponse</a></code>
- <code title="post /certificates/{id}/actions/retry">client.certificates.actions.<a href="./src/hetzner/resources/certificates/actions.py">retry</a>(id) -> <a href="./src/hetzner/types/certificates/action_retry_response.py">ActionRetryResponse</a></code>

# Datacenters

Types:

```python
from hetzner.types import DatacenterRetrieveResponse, DatacenterListResponse
```

Methods:

- <code title="get /datacenters/{id}">client.datacenters.<a href="./src/hetzner/resources/datacenters.py">retrieve</a>(id) -> <a href="./src/hetzner/types/datacenter_retrieve_response.py">DatacenterRetrieveResponse</a></code>
- <code title="get /datacenters">client.datacenters.<a href="./src/hetzner/resources/datacenters.py">list</a>(\*\*<a href="src/hetzner/types/datacenter_list_params.py">params</a>) -> <a href="./src/hetzner/types/datacenter_list_response.py">DatacenterListResponse</a></code>

# Firewalls

Types:

```python
from hetzner.types import (
    Firewall,
    Rule,
    FirewallCreateResponse,
    FirewallRetrieveResponse,
    FirewallUpdateResponse,
    FirewallListResponse,
)
```

Methods:

- <code title="post /firewalls">client.firewalls.<a href="./src/hetzner/resources/firewalls/firewalls.py">create</a>(\*\*<a href="src/hetzner/types/firewall_create_params.py">params</a>) -> <a href="./src/hetzner/types/firewall_create_response.py">FirewallCreateResponse</a></code>
- <code title="get /firewalls/{id}">client.firewalls.<a href="./src/hetzner/resources/firewalls/firewalls.py">retrieve</a>(id) -> <a href="./src/hetzner/types/firewall_retrieve_response.py">FirewallRetrieveResponse</a></code>
- <code title="put /firewalls/{id}">client.firewalls.<a href="./src/hetzner/resources/firewalls/firewalls.py">update</a>(id, \*\*<a href="src/hetzner/types/firewall_update_params.py">params</a>) -> <a href="./src/hetzner/types/firewall_update_response.py">FirewallUpdateResponse</a></code>
- <code title="get /firewalls">client.firewalls.<a href="./src/hetzner/resources/firewalls/firewalls.py">list</a>(\*\*<a href="src/hetzner/types/firewall_list_params.py">params</a>) -> <a href="./src/hetzner/types/firewall_list_response.py">FirewallListResponse</a></code>
- <code title="delete /firewalls/{id}">client.firewalls.<a href="./src/hetzner/resources/firewalls/firewalls.py">delete</a>(id) -> None</code>

## Actions

Types:

```python
from hetzner.types.firewalls import (
    ActionRetrieveResponse,
    ActionListResponse,
    ActionApplyToResourcesResponse,
    ActionRemoveFromResourcesResponse,
    ActionSetRulesResponse,
)
```

Methods:

- <code title="get /firewalls/{id}/actions/{action_id}">client.firewalls.actions.<a href="./src/hetzner/resources/firewalls/actions.py">retrieve</a>(id, action_id) -> <a href="./src/hetzner/types/firewalls/action_retrieve_response.py">ActionRetrieveResponse</a></code>
- <code title="get /firewalls/{id}/actions">client.firewalls.actions.<a href="./src/hetzner/resources/firewalls/actions.py">list</a>(id, \*\*<a href="src/hetzner/types/firewalls/action_list_params.py">params</a>) -> <a href="./src/hetzner/types/firewalls/action_list_response.py">ActionListResponse</a></code>
- <code title="post /firewalls/{id}/actions/apply_to_resources">client.firewalls.actions.<a href="./src/hetzner/resources/firewalls/actions.py">apply_to_resources</a>(id, \*\*<a href="src/hetzner/types/firewalls/action_apply_to_resources_params.py">params</a>) -> <a href="./src/hetzner/types/firewalls/action_apply_to_resources_response.py">ActionApplyToResourcesResponse</a></code>
- <code title="post /firewalls/{id}/actions/remove_from_resources">client.firewalls.actions.<a href="./src/hetzner/resources/firewalls/actions.py">remove_from_resources</a>(id, \*\*<a href="src/hetzner/types/firewalls/action_remove_from_resources_params.py">params</a>) -> <a href="./src/hetzner/types/firewalls/action_remove_from_resources_response.py">ActionRemoveFromResourcesResponse</a></code>
- <code title="post /firewalls/{id}/actions/set_rules">client.firewalls.actions.<a href="./src/hetzner/resources/firewalls/actions.py">set_rules</a>(id, \*\*<a href="src/hetzner/types/firewalls/action_set_rules_params.py">params</a>) -> <a href="./src/hetzner/types/firewalls/action_set_rules_response.py">ActionSetRulesResponse</a></code>

# FloatingIps

Types:

```python
from hetzner.types import (
    FloatingIp,
    FloatingIpCreateResponse,
    FloatingIpRetrieveResponse,
    FloatingIpUpdateResponse,
)
```

Methods:

- <code title="post /floating_ips">client.floating_ips.<a href="./src/hetzner/resources/floating_ips/floating_ips.py">create</a>(\*\*<a href="src/hetzner/types/floating_ip_create_params.py">params</a>) -> <a href="./src/hetzner/types/floating_ip_create_response.py">FloatingIpCreateResponse</a></code>
- <code title="get /floating_ips/{id}">client.floating_ips.<a href="./src/hetzner/resources/floating_ips/floating_ips.py">retrieve</a>(id) -> <a href="./src/hetzner/types/floating_ip_retrieve_response.py">FloatingIpRetrieveResponse</a></code>
- <code title="put /floating_ips/{id}">client.floating_ips.<a href="./src/hetzner/resources/floating_ips/floating_ips.py">update</a>(id, \*\*<a href="src/hetzner/types/floating_ip_update_params.py">params</a>) -> <a href="./src/hetzner/types/floating_ip_update_response.py">FloatingIpUpdateResponse</a></code>
- <code title="get /floating_ips">client.floating_ips.<a href="./src/hetzner/resources/floating_ips/floating_ips.py">list</a>(\*\*<a href="src/hetzner/types/floating_ip_list_params.py">params</a>) -> <a href="./src/hetzner/types/floating_ip.py">SyncFloatingIpsPage[FloatingIp]</a></code>
- <code title="delete /floating_ips/{id}">client.floating_ips.<a href="./src/hetzner/resources/floating_ips/floating_ips.py">delete</a>(id) -> None</code>

## Actions

Types:

```python
from hetzner.types.floating_ips import (
    ActionRetrieveResponse,
    ActionListResponse,
    ActionAssignResponse,
    ActionChangeDnsPtrResponse,
    ActionChangeProtectionResponse,
    ActionUnassignResponse,
)
```

Methods:

- <code title="get /floating_ips/{id}/actions/{action_id}">client.floating_ips.actions.<a href="./src/hetzner/resources/floating_ips/actions.py">retrieve</a>(id, action_id) -> <a href="./src/hetzner/types/floating_ips/action_retrieve_response.py">ActionRetrieveResponse</a></code>
- <code title="get /floating_ips/{id}/actions">client.floating_ips.actions.<a href="./src/hetzner/resources/floating_ips/actions.py">list</a>(id, \*\*<a href="src/hetzner/types/floating_ips/action_list_params.py">params</a>) -> <a href="./src/hetzner/types/floating_ips/action_list_response.py">ActionListResponse</a></code>
- <code title="post /floating_ips/{id}/actions/assign">client.floating_ips.actions.<a href="./src/hetzner/resources/floating_ips/actions.py">assign</a>(id, \*\*<a href="src/hetzner/types/floating_ips/action_assign_params.py">params</a>) -> <a href="./src/hetzner/types/floating_ips/action_assign_response.py">ActionAssignResponse</a></code>
- <code title="post /floating_ips/{id}/actions/change_dns_ptr">client.floating_ips.actions.<a href="./src/hetzner/resources/floating_ips/actions.py">change_dns_ptr</a>(id, \*\*<a href="src/hetzner/types/floating_ips/action_change_dns_ptr_params.py">params</a>) -> <a href="./src/hetzner/types/floating_ips/action_change_dns_ptr_response.py">ActionChangeDnsPtrResponse</a></code>
- <code title="post /floating_ips/{id}/actions/change_protection">client.floating_ips.actions.<a href="./src/hetzner/resources/floating_ips/actions.py">change_protection</a>(id, \*\*<a href="src/hetzner/types/floating_ips/action_change_protection_params.py">params</a>) -> <a href="./src/hetzner/types/floating_ips/action_change_protection_response.py">ActionChangeProtectionResponse</a></code>
- <code title="post /floating_ips/{id}/actions/unassign">client.floating_ips.actions.<a href="./src/hetzner/resources/floating_ips/actions.py">unassign</a>(id) -> <a href="./src/hetzner/types/floating_ips/action_unassign_response.py">ActionUnassignResponse</a></code>

# Images

Types:

```python
from hetzner.types import ImageRetrieveResponse, ImageUpdateResponse, ImageListResponse
```

Methods:

- <code title="get /images/{id}">client.images.<a href="./src/hetzner/resources/images/images.py">retrieve</a>(id) -> <a href="./src/hetzner/types/image_retrieve_response.py">ImageRetrieveResponse</a></code>
- <code title="put /images/{id}">client.images.<a href="./src/hetzner/resources/images/images.py">update</a>(id, \*\*<a href="src/hetzner/types/image_update_params.py">params</a>) -> <a href="./src/hetzner/types/image_update_response.py">ImageUpdateResponse</a></code>
- <code title="get /images">client.images.<a href="./src/hetzner/resources/images/images.py">list</a>(\*\*<a href="src/hetzner/types/image_list_params.py">params</a>) -> <a href="./src/hetzner/types/image_list_response.py">ImageListResponse</a></code>
- <code title="delete /images/{id}">client.images.<a href="./src/hetzner/resources/images/images.py">delete</a>(id) -> None</code>

## Actions

Types:

```python
from hetzner.types.images import (
    ActionRetrieveResponse,
    ActionListResponse,
    ActionChangeProtectionResponse,
)
```

Methods:

- <code title="get /images/{id}/actions/{action_id}">client.images.actions.<a href="./src/hetzner/resources/images/actions.py">retrieve</a>(id, action_id) -> <a href="./src/hetzner/types/images/action_retrieve_response.py">ActionRetrieveResponse</a></code>
- <code title="get /images/{id}/actions">client.images.actions.<a href="./src/hetzner/resources/images/actions.py">list</a>(id, \*\*<a href="src/hetzner/types/images/action_list_params.py">params</a>) -> <a href="./src/hetzner/types/images/action_list_response.py">ActionListResponse</a></code>
- <code title="post /images/{id}/actions/change_protection">client.images.actions.<a href="./src/hetzner/resources/images/actions.py">change_protection</a>(id, \*\*<a href="src/hetzner/types/images/action_change_protection_params.py">params</a>) -> <a href="./src/hetzner/types/images/action_change_protection_response.py">ActionChangeProtectionResponse</a></code>

# Isos

Types:

```python
from hetzner.types import IsoRetrieveResponse, IsoListResponse
```

Methods:

- <code title="get /isos/{id}">client.isos.<a href="./src/hetzner/resources/isos.py">retrieve</a>(id) -> <a href="./src/hetzner/types/iso_retrieve_response.py">IsoRetrieveResponse</a></code>
- <code title="get /isos">client.isos.<a href="./src/hetzner/resources/isos.py">list</a>(\*\*<a href="src/hetzner/types/iso_list_params.py">params</a>) -> <a href="./src/hetzner/types/iso_list_response.py">IsoListResponse</a></code>

# LoadBalancerTypes

Types:

```python
from hetzner.types import LoadBalancerTypeRetrieveResponse, LoadBalancerTypeListResponse
```

Methods:

- <code title="get /load_balancer_types/{id}">client.load_balancer_types.<a href="./src/hetzner/resources/load_balancer_types.py">retrieve</a>(id) -> <a href="./src/hetzner/types/load_balancer_type_retrieve_response.py">LoadBalancerTypeRetrieveResponse</a></code>
- <code title="get /load_balancer_types">client.load_balancer_types.<a href="./src/hetzner/resources/load_balancer_types.py">list</a>(\*\*<a href="src/hetzner/types/load_balancer_type_list_params.py">params</a>) -> <a href="./src/hetzner/types/load_balancer_type_list_response.py">LoadBalancerTypeListResponse</a></code>

# LoadBalancers

Types:

```python
from hetzner.types import (
    LoadBalancer,
    LoadBalancerServiceModel,
    LoadBalancerTargetIp,
    LoadBalancerCreateResponse,
    LoadBalancerRetrieveResponse,
    LoadBalancerUpdateResponse,
    LoadBalancerListResponse,
)
```

Methods:

- <code title="post /load_balancers">client.load_balancers.<a href="./src/hetzner/resources/load_balancers/load_balancers.py">create</a>(\*\*<a href="src/hetzner/types/load_balancer_create_params.py">params</a>) -> <a href="./src/hetzner/types/load_balancer_create_response.py">LoadBalancerCreateResponse</a></code>
- <code title="get /load_balancers/{id}">client.load_balancers.<a href="./src/hetzner/resources/load_balancers/load_balancers.py">retrieve</a>(id) -> <a href="./src/hetzner/types/load_balancer_retrieve_response.py">LoadBalancerRetrieveResponse</a></code>
- <code title="put /load_balancers/{id}">client.load_balancers.<a href="./src/hetzner/resources/load_balancers/load_balancers.py">update</a>(id, \*\*<a href="src/hetzner/types/load_balancer_update_params.py">params</a>) -> <a href="./src/hetzner/types/load_balancer_update_response.py">LoadBalancerUpdateResponse</a></code>
- <code title="get /load_balancers">client.load_balancers.<a href="./src/hetzner/resources/load_balancers/load_balancers.py">list</a>(\*\*<a href="src/hetzner/types/load_balancer_list_params.py">params</a>) -> <a href="./src/hetzner/types/load_balancer_list_response.py">LoadBalancerListResponse</a></code>
- <code title="delete /load_balancers/{id}">client.load_balancers.<a href="./src/hetzner/resources/load_balancers/load_balancers.py">delete</a>(id) -> None</code>

## Actions

Types:

```python
from hetzner.types.load_balancers import (
    ActionRetrieveResponse,
    ActionListResponse,
    ActionAddServiceResponse,
    ActionAssTargetResponse,
    ActionAttachToNetworkResponse,
    ActionChangeAlgorithmResponse,
    ActionChangeDnsPtrResponse,
    ActionChangeProtectionResponse,
    ActionChangeTypeResponse,
    ActionDeleteServiceResponse,
    ActionDetachFromNetworkResponse,
    ActionDisablePublicInterfaceResponse,
    ActionEnablePublicInterfaceResponse,
    ActionRemoveTargetResponse,
    ActionUpdateServiceResponse,
)
```

Methods:

- <code title="get /load_balancers/{id}/actions/{action_id}">client.load_balancers.actions.<a href="./src/hetzner/resources/load_balancers/actions.py">retrieve</a>(id, action_id) -> <a href="./src/hetzner/types/load_balancers/action_retrieve_response.py">ActionRetrieveResponse</a></code>
- <code title="get /load_balancers/{id}/actions">client.load_balancers.actions.<a href="./src/hetzner/resources/load_balancers/actions.py">list</a>(id, \*\*<a href="src/hetzner/types/load_balancers/action_list_params.py">params</a>) -> <a href="./src/hetzner/types/load_balancers/action_list_response.py">ActionListResponse</a></code>
- <code title="post /load_balancers/{id}/actions/add_service">client.load_balancers.actions.<a href="./src/hetzner/resources/load_balancers/actions.py">add_service</a>(id, \*\*<a href="src/hetzner/types/load_balancers/action_add_service_params.py">params</a>) -> <a href="./src/hetzner/types/load_balancers/action_add_service_response.py">ActionAddServiceResponse</a></code>
- <code title="post /load_balancers/{id}/actions/add_target">client.load_balancers.actions.<a href="./src/hetzner/resources/load_balancers/actions.py">ass_target</a>(id, \*\*<a href="src/hetzner/types/load_balancers/action_ass_target_params.py">params</a>) -> <a href="./src/hetzner/types/load_balancers/action_ass_target_response.py">ActionAssTargetResponse</a></code>
- <code title="post /load_balancers/{id}/actions/attach_to_network">client.load_balancers.actions.<a href="./src/hetzner/resources/load_balancers/actions.py">attach_to_network</a>(id, \*\*<a href="src/hetzner/types/load_balancers/action_attach_to_network_params.py">params</a>) -> <a href="./src/hetzner/types/load_balancers/action_attach_to_network_response.py">ActionAttachToNetworkResponse</a></code>
- <code title="post /load_balancers/{id}/actions/change_algorithm">client.load_balancers.actions.<a href="./src/hetzner/resources/load_balancers/actions.py">change_algorithm</a>(id, \*\*<a href="src/hetzner/types/load_balancers/action_change_algorithm_params.py">params</a>) -> <a href="./src/hetzner/types/load_balancers/action_change_algorithm_response.py">ActionChangeAlgorithmResponse</a></code>
- <code title="post /load_balancers/{id}/actions/change_dns_ptr">client.load_balancers.actions.<a href="./src/hetzner/resources/load_balancers/actions.py">change_dns_ptr</a>(id, \*\*<a href="src/hetzner/types/load_balancers/action_change_dns_ptr_params.py">params</a>) -> <a href="./src/hetzner/types/load_balancers/action_change_dns_ptr_response.py">ActionChangeDnsPtrResponse</a></code>
- <code title="post /load_balancers/{id}/actions/change_protection">client.load_balancers.actions.<a href="./src/hetzner/resources/load_balancers/actions.py">change_protection</a>(id, \*\*<a href="src/hetzner/types/load_balancers/action_change_protection_params.py">params</a>) -> <a href="./src/hetzner/types/load_balancers/action_change_protection_response.py">ActionChangeProtectionResponse</a></code>
- <code title="post /load_balancers/{id}/actions/change_type">client.load_balancers.actions.<a href="./src/hetzner/resources/load_balancers/actions.py">change_type</a>(id, \*\*<a href="src/hetzner/types/load_balancers/action_change_type_params.py">params</a>) -> <a href="./src/hetzner/types/load_balancers/action_change_type_response.py">ActionChangeTypeResponse</a></code>
- <code title="post /load_balancers/{id}/actions/delete_service">client.load_balancers.actions.<a href="./src/hetzner/resources/load_balancers/actions.py">delete_service</a>(id, \*\*<a href="src/hetzner/types/load_balancers/action_delete_service_params.py">params</a>) -> <a href="./src/hetzner/types/load_balancers/action_delete_service_response.py">ActionDeleteServiceResponse</a></code>
- <code title="post /load_balancers/{id}/actions/detach_from_network">client.load_balancers.actions.<a href="./src/hetzner/resources/load_balancers/actions.py">detach_from_network</a>(id, \*\*<a href="src/hetzner/types/load_balancers/action_detach_from_network_params.py">params</a>) -> <a href="./src/hetzner/types/load_balancers/action_detach_from_network_response.py">ActionDetachFromNetworkResponse</a></code>
- <code title="post /load_balancers/{id}/actions/disable_public_interface">client.load_balancers.actions.<a href="./src/hetzner/resources/load_balancers/actions.py">disable_public_interface</a>(id) -> <a href="./src/hetzner/types/load_balancers/action_disable_public_interface_response.py">ActionDisablePublicInterfaceResponse</a></code>
- <code title="post /load_balancers/{id}/actions/enable_public_interface">client.load_balancers.actions.<a href="./src/hetzner/resources/load_balancers/actions.py">enable_public_interface</a>(id) -> <a href="./src/hetzner/types/load_balancers/action_enable_public_interface_response.py">ActionEnablePublicInterfaceResponse</a></code>
- <code title="post /load_balancers/{id}/actions/remove_target">client.load_balancers.actions.<a href="./src/hetzner/resources/load_balancers/actions.py">remove_target</a>(id, \*\*<a href="src/hetzner/types/load_balancers/action_remove_target_params.py">params</a>) -> <a href="./src/hetzner/types/load_balancers/action_remove_target_response.py">ActionRemoveTargetResponse</a></code>
- <code title="post /load_balancers/{id}/actions/update_service">client.load_balancers.actions.<a href="./src/hetzner/resources/load_balancers/actions.py">update_service</a>(id, \*\*<a href="src/hetzner/types/load_balancers/action_update_service_params.py">params</a>) -> <a href="./src/hetzner/types/load_balancers/action_update_service_response.py">ActionUpdateServiceResponse</a></code>

## Metrics

Types:

```python
from hetzner.types.load_balancers import MetricListResponse
```

Methods:

- <code title="get /load_balancers/{id}/metrics">client.load_balancers.metrics.<a href="./src/hetzner/resources/load_balancers/metrics.py">list</a>(id, \*\*<a href="src/hetzner/types/load_balancers/metric_list_params.py">params</a>) -> <a href="./src/hetzner/types/load_balancers/metric_list_response.py">MetricListResponse</a></code>

# Locations

Types:

```python
from hetzner.types import LocationRetrieveResponse, LocationListResponse
```

Methods:

- <code title="get /locations/{id}">client.locations.<a href="./src/hetzner/resources/locations.py">retrieve</a>(id) -> <a href="./src/hetzner/types/location_retrieve_response.py">LocationRetrieveResponse</a></code>
- <code title="get /locations">client.locations.<a href="./src/hetzner/resources/locations.py">list</a>(\*\*<a href="src/hetzner/types/location_list_params.py">params</a>) -> <a href="./src/hetzner/types/location_list_response.py">LocationListResponse</a></code>

# Networks

Types:

```python
from hetzner.types import (
    NetworkCreateResponse,
    NetworkRetrieveResponse,
    NetworkUpdateResponse,
    NetworkListResponse,
)
```

Methods:

- <code title="post /networks">client.networks.<a href="./src/hetzner/resources/networks/networks.py">create</a>(\*\*<a href="src/hetzner/types/network_create_params.py">params</a>) -> <a href="./src/hetzner/types/network_create_response.py">NetworkCreateResponse</a></code>
- <code title="get /networks/{id}">client.networks.<a href="./src/hetzner/resources/networks/networks.py">retrieve</a>(id) -> <a href="./src/hetzner/types/network_retrieve_response.py">NetworkRetrieveResponse</a></code>
- <code title="put /networks/{id}">client.networks.<a href="./src/hetzner/resources/networks/networks.py">update</a>(id, \*\*<a href="src/hetzner/types/network_update_params.py">params</a>) -> <a href="./src/hetzner/types/network_update_response.py">NetworkUpdateResponse</a></code>
- <code title="get /networks">client.networks.<a href="./src/hetzner/resources/networks/networks.py">list</a>(\*\*<a href="src/hetzner/types/network_list_params.py">params</a>) -> <a href="./src/hetzner/types/network_list_response.py">NetworkListResponse</a></code>
- <code title="delete /networks/{id}">client.networks.<a href="./src/hetzner/resources/networks/networks.py">delete</a>(id) -> None</code>

## Actions

Types:

```python
from hetzner.types.networks import (
    ActionRetrieveResponse,
    ActionListResponse,
    ActionAddRouteResponse,
    ActionAddSubnetResponse,
    ActionChangeIpRangeResponse,
    ActionChangeProtectionResponse,
    ActionDeleteRouteResponse,
    ActionDeleteSubnetResponse,
)
```

Methods:

- <code title="get /networks/{id}/actions/{action_id}">client.networks.actions.<a href="./src/hetzner/resources/networks/actions.py">retrieve</a>(id, action_id) -> <a href="./src/hetzner/types/networks/action_retrieve_response.py">ActionRetrieveResponse</a></code>
- <code title="get /networks/{id}/actions">client.networks.actions.<a href="./src/hetzner/resources/networks/actions.py">list</a>(id, \*\*<a href="src/hetzner/types/networks/action_list_params.py">params</a>) -> <a href="./src/hetzner/types/networks/action_list_response.py">ActionListResponse</a></code>
- <code title="post /networks/{id}/actions/add_route">client.networks.actions.<a href="./src/hetzner/resources/networks/actions.py">add_route</a>(id, \*\*<a href="src/hetzner/types/networks/action_add_route_params.py">params</a>) -> <a href="./src/hetzner/types/networks/action_add_route_response.py">ActionAddRouteResponse</a></code>
- <code title="post /networks/{id}/actions/add_subnet">client.networks.actions.<a href="./src/hetzner/resources/networks/actions.py">add_subnet</a>(id, \*\*<a href="src/hetzner/types/networks/action_add_subnet_params.py">params</a>) -> <a href="./src/hetzner/types/networks/action_add_subnet_response.py">ActionAddSubnetResponse</a></code>
- <code title="post /networks/{id}/actions/change_ip_range">client.networks.actions.<a href="./src/hetzner/resources/networks/actions.py">change_ip_range</a>(id, \*\*<a href="src/hetzner/types/networks/action_change_ip_range_params.py">params</a>) -> <a href="./src/hetzner/types/networks/action_change_ip_range_response.py">ActionChangeIpRangeResponse</a></code>
- <code title="post /networks/{id}/actions/change_protection">client.networks.actions.<a href="./src/hetzner/resources/networks/actions.py">change_protection</a>(id, \*\*<a href="src/hetzner/types/networks/action_change_protection_params.py">params</a>) -> <a href="./src/hetzner/types/networks/action_change_protection_response.py">ActionChangeProtectionResponse</a></code>
- <code title="post /networks/{id}/actions/delete_route">client.networks.actions.<a href="./src/hetzner/resources/networks/actions.py">delete_route</a>(id, \*\*<a href="src/hetzner/types/networks/action_delete_route_params.py">params</a>) -> <a href="./src/hetzner/types/networks/action_delete_route_response.py">ActionDeleteRouteResponse</a></code>
- <code title="post /networks/{id}/actions/delete_subnet">client.networks.actions.<a href="./src/hetzner/resources/networks/actions.py">delete_subnet</a>(id, \*\*<a href="src/hetzner/types/networks/action_delete_subnet_params.py">params</a>) -> <a href="./src/hetzner/types/networks/action_delete_subnet_response.py">ActionDeleteSubnetResponse</a></code>

# PlacementGroups

Types:

```python
from hetzner.types import (
    PlacementGroup,
    PlacementGroupCreateResponse,
    PlacementGroupRetrieveResponse,
    PlacementGroupUpdateResponse,
    PlacementGroupListResponse,
)
```

Methods:

- <code title="post /placement_groups">client.placement_groups.<a href="./src/hetzner/resources/placement_groups.py">create</a>(\*\*<a href="src/hetzner/types/placement_group_create_params.py">params</a>) -> <a href="./src/hetzner/types/placement_group_create_response.py">PlacementGroupCreateResponse</a></code>
- <code title="get /placement_groups/{id}">client.placement_groups.<a href="./src/hetzner/resources/placement_groups.py">retrieve</a>(id) -> <a href="./src/hetzner/types/placement_group_retrieve_response.py">PlacementGroupRetrieveResponse</a></code>
- <code title="put /placement_groups/{id}">client.placement_groups.<a href="./src/hetzner/resources/placement_groups.py">update</a>(id, \*\*<a href="src/hetzner/types/placement_group_update_params.py">params</a>) -> <a href="./src/hetzner/types/placement_group_update_response.py">PlacementGroupUpdateResponse</a></code>
- <code title="get /placement_groups">client.placement_groups.<a href="./src/hetzner/resources/placement_groups.py">list</a>(\*\*<a href="src/hetzner/types/placement_group_list_params.py">params</a>) -> <a href="./src/hetzner/types/placement_group_list_response.py">PlacementGroupListResponse</a></code>
- <code title="delete /placement_groups/{id}">client.placement_groups.<a href="./src/hetzner/resources/placement_groups.py">delete</a>(id) -> None</code>

# Pricing

Types:

```python
from hetzner.types import (
    FloatingIpPriceDetails,
    Price,
    PricePerTimeMonthly,
    PricingRetrieveResponse,
)
```

Methods:

- <code title="get /pricing">client.pricing.<a href="./src/hetzner/resources/pricing.py">retrieve</a>() -> <a href="./src/hetzner/types/pricing_retrieve_response.py">PricingRetrieveResponse</a></code>

# PrimaryIps

Types:

```python
from hetzner.types import (
    PrimaryIp,
    PrimaryIpCreateResponse,
    PrimaryIpRetrieveResponse,
    PrimaryIpUpdateResponse,
    PrimaryIpListResponse,
)
```

Methods:

- <code title="post /primary_ips">client.primary_ips.<a href="./src/hetzner/resources/primary_ips/primary_ips.py">create</a>(\*\*<a href="src/hetzner/types/primary_ip_create_params.py">params</a>) -> <a href="./src/hetzner/types/primary_ip_create_response.py">PrimaryIpCreateResponse</a></code>
- <code title="get /primary_ips/{id}">client.primary_ips.<a href="./src/hetzner/resources/primary_ips/primary_ips.py">retrieve</a>(id) -> <a href="./src/hetzner/types/primary_ip_retrieve_response.py">PrimaryIpRetrieveResponse</a></code>
- <code title="put /primary_ips/{id}">client.primary_ips.<a href="./src/hetzner/resources/primary_ips/primary_ips.py">update</a>(id, \*\*<a href="src/hetzner/types/primary_ip_update_params.py">params</a>) -> <a href="./src/hetzner/types/primary_ip_update_response.py">PrimaryIpUpdateResponse</a></code>
- <code title="get /primary_ips">client.primary_ips.<a href="./src/hetzner/resources/primary_ips/primary_ips.py">list</a>(\*\*<a href="src/hetzner/types/primary_ip_list_params.py">params</a>) -> <a href="./src/hetzner/types/primary_ip_list_response.py">PrimaryIpListResponse</a></code>
- <code title="delete /primary_ips/{id}">client.primary_ips.<a href="./src/hetzner/resources/primary_ips/primary_ips.py">delete</a>(id) -> None</code>

## Actions

Types:

```python
from hetzner.types.primary_ips import (
    ActionRetrieveResponse,
    ActionListResponse,
    ActionAssignResponse,
    ActionChangeDnsPtrResponse,
    ActionChangeProtectionResponse,
    ActionUnassignResponse,
)
```

Methods:

- <code title="get /primary_ips/actions/{id}">client.primary_ips.actions.<a href="./src/hetzner/resources/primary_ips/actions.py">retrieve</a>(id) -> <a href="./src/hetzner/types/primary_ips/action_retrieve_response.py">ActionRetrieveResponse</a></code>
- <code title="get /primary_ips/actions">client.primary_ips.actions.<a href="./src/hetzner/resources/primary_ips/actions.py">list</a>(\*\*<a href="src/hetzner/types/primary_ips/action_list_params.py">params</a>) -> <a href="./src/hetzner/types/primary_ips/action_list_response.py">ActionListResponse</a></code>
- <code title="post /primary_ips/{id}/actions/assign">client.primary_ips.actions.<a href="./src/hetzner/resources/primary_ips/actions.py">assign</a>(id, \*\*<a href="src/hetzner/types/primary_ips/action_assign_params.py">params</a>) -> <a href="./src/hetzner/types/primary_ips/action_assign_response.py">ActionAssignResponse</a></code>
- <code title="post /primary_ips/{id}/actions/change_dns_ptr">client.primary_ips.actions.<a href="./src/hetzner/resources/primary_ips/actions.py">change_dns_ptr</a>(id, \*\*<a href="src/hetzner/types/primary_ips/action_change_dns_ptr_params.py">params</a>) -> <a href="./src/hetzner/types/primary_ips/action_change_dns_ptr_response.py">ActionChangeDnsPtrResponse</a></code>
- <code title="post /primary_ips/{id}/actions/change_protection">client.primary_ips.actions.<a href="./src/hetzner/resources/primary_ips/actions.py">change_protection</a>(id, \*\*<a href="src/hetzner/types/primary_ips/action_change_protection_params.py">params</a>) -> <a href="./src/hetzner/types/primary_ips/action_change_protection_response.py">ActionChangeProtectionResponse</a></code>
- <code title="post /primary_ips/{id}/actions/unassign">client.primary_ips.actions.<a href="./src/hetzner/resources/primary_ips/actions.py">unassign</a>(id) -> <a href="./src/hetzner/types/primary_ips/action_unassign_response.py">ActionUnassignResponse</a></code>

# ServerTypes

Types:

```python
from hetzner.types import ServerTypeRetrieveResponse, ServerTypeListResponse
```

Methods:

- <code title="get /server_types/{id}">client.server_types.<a href="./src/hetzner/resources/server_types.py">retrieve</a>(id) -> <a href="./src/hetzner/types/server_type_retrieve_response.py">ServerTypeRetrieveResponse</a></code>
- <code title="get /server_types">client.server_types.<a href="./src/hetzner/resources/server_types.py">list</a>(\*\*<a href="src/hetzner/types/server_type_list_params.py">params</a>) -> <a href="./src/hetzner/types/server_type_list_response.py">ServerTypeListResponse</a></code>

# Servers

Types:

```python
from hetzner.types import (
    Server,
    ServerPublicNet,
    ServerCreateResponse,
    ServerRetrieveResponse,
    ServerUpdateResponse,
    ServerDeleteResponse,
)
```

Methods:

- <code title="post /servers">client.servers.<a href="./src/hetzner/resources/servers/servers.py">create</a>(\*\*<a href="src/hetzner/types/server_create_params.py">params</a>) -> <a href="./src/hetzner/types/server_create_response.py">ServerCreateResponse</a></code>
- <code title="get /servers/{id}">client.servers.<a href="./src/hetzner/resources/servers/servers.py">retrieve</a>(id) -> <a href="./src/hetzner/types/server_retrieve_response.py">ServerRetrieveResponse</a></code>
- <code title="put /servers/{id}">client.servers.<a href="./src/hetzner/resources/servers/servers.py">update</a>(id, \*\*<a href="src/hetzner/types/server_update_params.py">params</a>) -> <a href="./src/hetzner/types/server_update_response.py">ServerUpdateResponse</a></code>
- <code title="get /servers">client.servers.<a href="./src/hetzner/resources/servers/servers.py">list</a>(\*\*<a href="src/hetzner/types/server_list_params.py">params</a>) -> <a href="./src/hetzner/types/server.py">SyncServersPage[Server]</a></code>
- <code title="delete /servers/{id}">client.servers.<a href="./src/hetzner/resources/servers/servers.py">delete</a>(id) -> <a href="./src/hetzner/types/server_delete_response.py">ServerDeleteResponse</a></code>

## Actions

Types:

```python
from hetzner.types.servers import (
    ActionRetrieveResponse,
    ActionListResponse,
    ActionAddToPlacementGroupResponse,
    ActionAttachIsoResponse,
    ActionAttachToNetworkResponse,
    ActionChangeAliasIpsResponse,
    ActionChangeDnsPtrResponse,
    ActionChangeProtectionResponse,
    ActionChangeTypeResponse,
    ActionCreateImageResponse,
    ActionDetachFromNetworkResponse,
    ActionDetachIsoResponse,
    ActionDisableBackupResponse,
    ActionDisableRescueResponse,
    ActionEnableBackupResponse,
    ActionEnableRescueResponse,
    ActionPoweroffResponse,
    ActionPoweronResponse,
    ActionRebootResponse,
    ActionRebuildResponse,
    ActionRemoveFromPlacementGroupResponse,
    ActionRequestConsoleResponse,
    ActionResetResponse,
    ActionResetPasswordResponse,
    ActionShutdownResponse,
)
```

Methods:

- <code title="get /servers/{id}/actions/{action_id}">client.servers.actions.<a href="./src/hetzner/resources/servers/actions.py">retrieve</a>(id, action_id) -> <a href="./src/hetzner/types/servers/action_retrieve_response.py">ActionRetrieveResponse</a></code>
- <code title="get /servers/{id}/actions">client.servers.actions.<a href="./src/hetzner/resources/servers/actions.py">list</a>(id, \*\*<a href="src/hetzner/types/servers/action_list_params.py">params</a>) -> <a href="./src/hetzner/types/servers/action_list_response.py">ActionListResponse</a></code>
- <code title="post /servers/{id}/actions/add_to_placement_group">client.servers.actions.<a href="./src/hetzner/resources/servers/actions.py">add_to_placement_group</a>(id, \*\*<a href="src/hetzner/types/servers/action_add_to_placement_group_params.py">params</a>) -> <a href="./src/hetzner/types/servers/action_add_to_placement_group_response.py">ActionAddToPlacementGroupResponse</a></code>
- <code title="post /servers/{id}/actions/attach_iso">client.servers.actions.<a href="./src/hetzner/resources/servers/actions.py">attach_iso</a>(id, \*\*<a href="src/hetzner/types/servers/action_attach_iso_params.py">params</a>) -> <a href="./src/hetzner/types/servers/action_attach_iso_response.py">ActionAttachIsoResponse</a></code>
- <code title="post /servers/{id}/actions/attach_to_network">client.servers.actions.<a href="./src/hetzner/resources/servers/actions.py">attach_to_network</a>(id, \*\*<a href="src/hetzner/types/servers/action_attach_to_network_params.py">params</a>) -> <a href="./src/hetzner/types/servers/action_attach_to_network_response.py">ActionAttachToNetworkResponse</a></code>
- <code title="post /servers/{id}/actions/change_alias_ips">client.servers.actions.<a href="./src/hetzner/resources/servers/actions.py">change_alias_ips</a>(id, \*\*<a href="src/hetzner/types/servers/action_change_alias_ips_params.py">params</a>) -> <a href="./src/hetzner/types/servers/action_change_alias_ips_response.py">ActionChangeAliasIpsResponse</a></code>
- <code title="post /servers/{id}/actions/change_dns_ptr">client.servers.actions.<a href="./src/hetzner/resources/servers/actions.py">change_dns_ptr</a>(id, \*\*<a href="src/hetzner/types/servers/action_change_dns_ptr_params.py">params</a>) -> <a href="./src/hetzner/types/servers/action_change_dns_ptr_response.py">ActionChangeDnsPtrResponse</a></code>
- <code title="post /servers/{id}/actions/change_protection">client.servers.actions.<a href="./src/hetzner/resources/servers/actions.py">change_protection</a>(id, \*\*<a href="src/hetzner/types/servers/action_change_protection_params.py">params</a>) -> <a href="./src/hetzner/types/servers/action_change_protection_response.py">ActionChangeProtectionResponse</a></code>
- <code title="post /servers/{id}/actions/change_type">client.servers.actions.<a href="./src/hetzner/resources/servers/actions.py">change_type</a>(id, \*\*<a href="src/hetzner/types/servers/action_change_type_params.py">params</a>) -> <a href="./src/hetzner/types/servers/action_change_type_response.py">ActionChangeTypeResponse</a></code>
- <code title="post /servers/{id}/actions/create_image">client.servers.actions.<a href="./src/hetzner/resources/servers/actions.py">create_image</a>(id, \*\*<a href="src/hetzner/types/servers/action_create_image_params.py">params</a>) -> <a href="./src/hetzner/types/servers/action_create_image_response.py">ActionCreateImageResponse</a></code>
- <code title="post /servers/{id}/actions/detach_from_network">client.servers.actions.<a href="./src/hetzner/resources/servers/actions.py">detach_from_network</a>(id, \*\*<a href="src/hetzner/types/servers/action_detach_from_network_params.py">params</a>) -> <a href="./src/hetzner/types/servers/action_detach_from_network_response.py">ActionDetachFromNetworkResponse</a></code>
- <code title="post /servers/{id}/actions/detach_iso">client.servers.actions.<a href="./src/hetzner/resources/servers/actions.py">detach_iso</a>(id) -> <a href="./src/hetzner/types/servers/action_detach_iso_response.py">ActionDetachIsoResponse</a></code>
- <code title="post /servers/{id}/actions/disable_backup">client.servers.actions.<a href="./src/hetzner/resources/servers/actions.py">disable_backup</a>(id) -> <a href="./src/hetzner/types/servers/action_disable_backup_response.py">ActionDisableBackupResponse</a></code>
- <code title="post /servers/{id}/actions/disable_rescue">client.servers.actions.<a href="./src/hetzner/resources/servers/actions.py">disable_rescue</a>(id) -> <a href="./src/hetzner/types/servers/action_disable_rescue_response.py">ActionDisableRescueResponse</a></code>
- <code title="post /servers/{id}/actions/enable_backup">client.servers.actions.<a href="./src/hetzner/resources/servers/actions.py">enable_backup</a>(id) -> <a href="./src/hetzner/types/servers/action_enable_backup_response.py">ActionEnableBackupResponse</a></code>
- <code title="post /servers/{id}/actions/enable_rescue">client.servers.actions.<a href="./src/hetzner/resources/servers/actions.py">enable_rescue</a>(id, \*\*<a href="src/hetzner/types/servers/action_enable_rescue_params.py">params</a>) -> <a href="./src/hetzner/types/servers/action_enable_rescue_response.py">ActionEnableRescueResponse</a></code>
- <code title="post /servers/{id}/actions/poweroff">client.servers.actions.<a href="./src/hetzner/resources/servers/actions.py">poweroff</a>(id) -> <a href="./src/hetzner/types/servers/action_poweroff_response.py">ActionPoweroffResponse</a></code>
- <code title="post /servers/{id}/actions/poweron">client.servers.actions.<a href="./src/hetzner/resources/servers/actions.py">poweron</a>(id) -> <a href="./src/hetzner/types/servers/action_poweron_response.py">ActionPoweronResponse</a></code>
- <code title="post /servers/{id}/actions/reboot">client.servers.actions.<a href="./src/hetzner/resources/servers/actions.py">reboot</a>(id) -> <a href="./src/hetzner/types/servers/action_reboot_response.py">ActionRebootResponse</a></code>
- <code title="post /servers/{id}/actions/rebuild">client.servers.actions.<a href="./src/hetzner/resources/servers/actions.py">rebuild</a>(id, \*\*<a href="src/hetzner/types/servers/action_rebuild_params.py">params</a>) -> <a href="./src/hetzner/types/servers/action_rebuild_response.py">ActionRebuildResponse</a></code>
- <code title="post /servers/{id}/actions/remove_from_placement_group">client.servers.actions.<a href="./src/hetzner/resources/servers/actions.py">remove_from_placement_group</a>(id) -> <a href="./src/hetzner/types/servers/action_remove_from_placement_group_response.py">ActionRemoveFromPlacementGroupResponse</a></code>
- <code title="post /servers/{id}/actions/request_console">client.servers.actions.<a href="./src/hetzner/resources/servers/actions.py">request_console</a>(id) -> <a href="./src/hetzner/types/servers/action_request_console_response.py">ActionRequestConsoleResponse</a></code>
- <code title="post /servers/{id}/actions/reset">client.servers.actions.<a href="./src/hetzner/resources/servers/actions.py">reset</a>(id) -> <a href="./src/hetzner/types/servers/action_reset_response.py">ActionResetResponse</a></code>
- <code title="post /servers/{id}/actions/reset_password">client.servers.actions.<a href="./src/hetzner/resources/servers/actions.py">reset_password</a>(id) -> <a href="./src/hetzner/types/servers/action_reset_password_response.py">ActionResetPasswordResponse</a></code>
- <code title="post /servers/{id}/actions/shutdown">client.servers.actions.<a href="./src/hetzner/resources/servers/actions.py">shutdown</a>(id) -> <a href="./src/hetzner/types/servers/action_shutdown_response.py">ActionShutdownResponse</a></code>

## Metrics

Types:

```python
from hetzner.types.servers import MetricListResponse
```

Methods:

- <code title="get /servers/{id}/metrics">client.servers.metrics.<a href="./src/hetzner/resources/servers/metrics.py">list</a>(id, \*\*<a href="src/hetzner/types/servers/metric_list_params.py">params</a>) -> <a href="./src/hetzner/types/servers/metric_list_response.py">MetricListResponse</a></code>

# SshKeys

Types:

```python
from hetzner.types import (
    SshKeyCreateResponse,
    SshKeyRetrieveResponse,
    SshKeyUpdateResponse,
    SshKeyListResponse,
)
```

Methods:

- <code title="post /ssh_keys">client.ssh_keys.<a href="./src/hetzner/resources/ssh_keys.py">create</a>(\*\*<a href="src/hetzner/types/ssh_key_create_params.py">params</a>) -> <a href="./src/hetzner/types/ssh_key_create_response.py">SshKeyCreateResponse</a></code>
- <code title="get /ssh_keys/{id}">client.ssh_keys.<a href="./src/hetzner/resources/ssh_keys.py">retrieve</a>(id) -> <a href="./src/hetzner/types/ssh_key_retrieve_response.py">SshKeyRetrieveResponse</a></code>
- <code title="put /ssh_keys/{id}">client.ssh_keys.<a href="./src/hetzner/resources/ssh_keys.py">update</a>(id, \*\*<a href="src/hetzner/types/ssh_key_update_params.py">params</a>) -> <a href="./src/hetzner/types/ssh_key_update_response.py">SshKeyUpdateResponse</a></code>
- <code title="get /ssh_keys">client.ssh_keys.<a href="./src/hetzner/resources/ssh_keys.py">list</a>(\*\*<a href="src/hetzner/types/ssh_key_list_params.py">params</a>) -> <a href="./src/hetzner/types/ssh_key_list_response.py">SshKeyListResponse</a></code>
- <code title="delete /ssh_keys/{id}">client.ssh_keys.<a href="./src/hetzner/resources/ssh_keys.py">delete</a>(id) -> None</code>

# Volumes

Types:

```python
from hetzner.types import (
    VolumeCreateResponse,
    VolumeRetrieveResponse,
    VolumeUpdateResponse,
    VolumeListResponse,
)
```

Methods:

- <code title="post /volumes">client.volumes.<a href="./src/hetzner/resources/volumes/volumes.py">create</a>(\*\*<a href="src/hetzner/types/volume_create_params.py">params</a>) -> <a href="./src/hetzner/types/volume_create_response.py">VolumeCreateResponse</a></code>
- <code title="get /volumes/{id}">client.volumes.<a href="./src/hetzner/resources/volumes/volumes.py">retrieve</a>(id) -> <a href="./src/hetzner/types/volume_retrieve_response.py">VolumeRetrieveResponse</a></code>
- <code title="put /volumes/{id}">client.volumes.<a href="./src/hetzner/resources/volumes/volumes.py">update</a>(id, \*\*<a href="src/hetzner/types/volume_update_params.py">params</a>) -> <a href="./src/hetzner/types/volume_update_response.py">VolumeUpdateResponse</a></code>
- <code title="get /volumes">client.volumes.<a href="./src/hetzner/resources/volumes/volumes.py">list</a>(\*\*<a href="src/hetzner/types/volume_list_params.py">params</a>) -> <a href="./src/hetzner/types/volume_list_response.py">VolumeListResponse</a></code>
- <code title="delete /volumes/{id}">client.volumes.<a href="./src/hetzner/resources/volumes/volumes.py">delete</a>(id) -> None</code>

## Actions

Types:

```python
from hetzner.types.volumes import (
    ActionRetrieveResponse,
    ActionListResponse,
    ActionAttachResponse,
    ActionChangeProtectionResponse,
    ActionDetachResponse,
    ActionResizeResponse,
)
```

Methods:

- <code title="get /volumes/actions/{id}">client.volumes.actions.<a href="./src/hetzner/resources/volumes/actions.py">retrieve</a>(id) -> <a href="./src/hetzner/types/volumes/action_retrieve_response.py">ActionRetrieveResponse</a></code>
- <code title="get /volumes/{id}/actions">client.volumes.actions.<a href="./src/hetzner/resources/volumes/actions.py">list</a>(id, \*\*<a href="src/hetzner/types/volumes/action_list_params.py">params</a>) -> <a href="./src/hetzner/types/volumes/action_list_response.py">ActionListResponse</a></code>
- <code title="post /volumes/{id}/actions/attach">client.volumes.actions.<a href="./src/hetzner/resources/volumes/actions.py">attach</a>(id, \*\*<a href="src/hetzner/types/volumes/action_attach_params.py">params</a>) -> <a href="./src/hetzner/types/volumes/action_attach_response.py">ActionAttachResponse</a></code>
- <code title="post /volumes/{id}/actions/change_protection">client.volumes.actions.<a href="./src/hetzner/resources/volumes/actions.py">change_protection</a>(id, \*\*<a href="src/hetzner/types/volumes/action_change_protection_params.py">params</a>) -> <a href="./src/hetzner/types/volumes/action_change_protection_response.py">ActionChangeProtectionResponse</a></code>
- <code title="post /volumes/{id}/actions/detach">client.volumes.actions.<a href="./src/hetzner/resources/volumes/actions.py">detach</a>(id) -> <a href="./src/hetzner/types/volumes/action_detach_response.py">ActionDetachResponse</a></code>
- <code title="post /volumes/{id}/actions/resize">client.volumes.actions.<a href="./src/hetzner/resources/volumes/actions.py">resize</a>(id, \*\*<a href="src/hetzner/types/volumes/action_resize_params.py">params</a>) -> <a href="./src/hetzner/types/volumes/action_resize_response.py">ActionResizeResponse</a></code>
