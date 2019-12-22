# 1 Overview

This is a Python program to manage configuration.

Python API is required to run this program.


# 2 Setup

* On the controller, create a sandbox.
```
mkdir sandbox
cd sandbox
wget https://raw.githubusercontent.com/tonyliu0592/contrail-toolbox/master/config/config
docker cp config_api_1:/usr/lib/python2.7/site-packages/vnc_api ./
docker cp config_api_1:/usr/lib/python2.7/site-packages/cfgm_common ./
```

* Update `admin.env`.

* Source `admin.env`.


# 3 Operation

# 3.1 Show

To list all resource types.
```
config show
```

To list all resource of specific type.
```
config show virtual-network
```

To show a specific resource whoes parent is the current project/tenant.
```
config show virtual-network red
```

To show a specific resource with FQ name.
```
config show virtual-network default-domain:admin:red
```


## 3.2  Create or update

To create or update resource.
```
config set --file <YAML file>
```
The resource will be created if it doesn't exist. Otherwise, it will be updated.

One resource file can have multiple resources.


## 3.3 Template

When creating or updating resource, the resource file can be built based on resource template. To show the template of specific type.
```
config show virtual-network --template
```

Note: The template has all attributes. When building the resoure file, only pick required atributes.


# 4 Example

## 4.1 Create virtual network

Create virtual network `net-a` and `net-b`.
```
- resource_type: virtual-network
  parent_type: project
  resource_fq_name:
  - default-domain
  - admin
  - net-a
  resource:
    display_name: net-a
    network_ipam_refs:
    - attr:
        ipam_subnets:
        - subnet:
            ip_prefix: 192.168.110.0
            ip_prefix_len: 24
      to:
      - default-domain
      - default-project
      - default-network-ipam

- resource_type: virtual-network
  parent_type: project
  resource_fq_name:
  - default-domain
  - admin
  - net-b
  resource:
    display_name: net-b
    network_ipam_refs:
    - attr:
        ipam_subnets:
        - subnet:
            ip_prefix: 192.168.120.0
            ip_prefix_len: 24
      to:
      - default-domain
      - default-project
      - default-network-ipam
```

## 4.2 Update virtual network

Add a subnet to `net-a`.
```
- resource_type: virtual-network
  parent_type: project
  resource_fq_name:
  - default-domain
  - admin
  - net-a
  resource:
    display_name: net-a
    network_ipam_refs:
    - attr:
        ipam_subnets:
        - subnet:
            ip_prefix: 192.168.110.0
            ip_prefix_len: 24
        - subnet:
            ip_prefix: 192.168.210.0
            ip_prefix_len: 24
      to:
      - default-domain
      - default-project
      - default-network-ipam
```

## 4.3 Create network policy

Create a network policy to connect `net-a` and `net-b`.
```
- resource_type: network-policy
  parent_type: project
  resource_fq_name:
  - default-domain
  - admin
  - net-a-net-b
  resource:
    display_name: string
    network_policy_entries:
      policy_rule:
      - action_list:
          simple_action: pass
        direction: <>
        protocol: any
        src_addresses:
        - virtual_network: default-domain:admin:net-b
        src_ports:
        - end_port: -1
          start_port: -1
        dst_addresses:
        - virtual_network: default-domain:admin:net-a
        dst_ports:
        - end_port: -1
          start_port: -1
```

## 4.4 Attach network policy

Update virtual network with policy.
```
- resource_type: virtual-network
  parent_type: project
  resource_fq_name:
  - default-domain
  - admin
  - net-a
  resource:
    display_name: net-a
    network_ipam_refs:
    - to:
      - default-domain
      - default-project
      - default-network-ipam
      attr:
        ipam_subnets:
        - subnet:
            ip_prefix: 192.168.110.0
            ip_prefix_len: 24
    network_policy_refs:
    - to:
      - default-domain
      - admin
      - net-a-net-b
      attr:
        sequence:
          major: 1
          minor: 0

- resource_type: virtual-network
  parent_type: project
  resource_fq_name:
  - default-domain
  - admin
  - net-b
  resource:
    display_name: net-b
    network_ipam_refs:
    - to:
      - default-domain
      - default-project
      - default-network-ipam
      attr:
        ipam_subnets:
        - subnet:
            ip_prefix: 192.168.120.0
            ip_prefix_len: 24
    network_policy_refs:
    - to:
      - default-domain
      - admin
      - net-a-net-b
      attr:
        sequence:
          major: 1
          minor: 0
```


## 4.5 Create service template

st-test.yaml
```
- resource_type: service-template
  parent_type: domain
  resource_fq_name:
  - default-domain
  - test-template
  resource:
    display_name: test-template
    service_template_properties:
      interface_type:
      - service_interface_type: management
      - service_interface_type: left
      - service_interface_type: right
      ordered_interfaces: true
      service_mode: in-network
      service_type: firewall
      service_virtualization_type: virtual-machine
      version: 2
```

