#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the resource
#   module builder playbook.
#
# Do not edit this file manually.
#
# Changes to this file will be over written
#   by the resource module builder.
#
# Changes should be made in the model used to
#   generate this file or in the resource module
#   builder template.
#
#############################################

"""
The module file for ios_vlans
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type


ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "network",
}

DOCUMENTATION = """
module: ios_vlans
version_added: 2.9
short_description: Manage VLANs on Cisco IOS devices.
description: This module provides declarative management of VLANs on Cisco IOS network devices.
author: Sumit Jaiswal (@justjais)
notes:
  - Tested against Cisco IOSv Version 15.2 on VIRL
  - This module works with connection C(network_cli).
    See L(IOS Platform Options,../network/user_guide/platform_ios.html).
options:
  config:
    description: A dictionary of VLANs options
    type: list
    elements: dict
    suboptions:
      name:
        description:
        - Ascii name of the VLAN.
        - NOTE, I(name) should not be named/appended with I(default) as it is reserved for device default vlans.
        type: str
      vlan_id:
        description:
        - ID of the VLAN. Range 1-4094
        type: int
        required: True
      mtu:
        description:
        - VLAN Maximum Transmission Unit.
        - Refer to vendor documentation for valid values.
        type: int
      state:
        description:
        - Operational state of the VLAN
        type: str
        choices:
        - active
        - suspend
      remote_span:
        description:
        - Configure as Remote SPAN VLAN
        type: bool
      shutdown:
        description:
        - Shutdown VLAN switching.
        type: str
        choices:
        - enabled
        - disabled
  state:
    description:
    - The state of the configuration after module completion
    type: str
    choices:
    - merged
    - replaced
    - overridden
    - deleted
    default: merged
"""
EXAMPLES = """
---
# Using merged

# Before state:
# -------------
#
# vios#show vlan
# VLAN Name                             Status    Ports
# ---- -------------------------------- --------- -------------------------------
# 1    default                          active    Gi0/1, Gi0/2
# 1002 fddi-default                     act/unsup
# 1003 token-ring-default               act/unsup
# 1004 fddinet-default                  act/unsup
# 1005 trnet-default                    act/unsup
#
# VLAN Type  SAID       MTU   Parent RingNo BridgeNo Stp  BrdgMode Trans1 Trans2
# ---- ----- ---------- ----- ------ ------ -------- ---- -------- ------ ------
# 1    enet  100001     1500  -      -      -        -    -        0      0
# 1002 fddi  101002     1500  -      -      -        -    -        0      0
# 1003 tr    101003     1500  -      -      -        -    -        0      0
# 1004 fdnet 101004     1500  -      -      -        ieee -        0      0
# 1005 trnet 101005     1500  -      -      -        ibm  -        0      0

- name: Merge provided configuration with device configuration
  ios_vlans:
    config:
      - name: Vlan_10
        vlan_id: 10
        state: active
        shutdown: disabled
        remote_span: 10
      - name: Vlan_20
        vlan_id: 20
        mtu: 610
        state: active
        shutdown: enabled
      - name: Vlan_30
        vlan_id: 30
        state: suspend
        shutdown: enabled
    state: merged

# After state:
# ------------
#
# vios#show vlan
# VLAN Name                             Status    Ports
# ---- -------------------------------- --------- -------------------------------
# 1    default                          active    Gi0/1, Gi0/2
# 10   vlan_10                          active
# 20   vlan_20                          act/lshut
# 30   vlan_30                          sus/lshut
# 1002 fddi-default                     act/unsup
# 1003 token-ring-default               act/unsup
# 1004 fddinet-default                  act/unsup
# 1005 trnet-default                    act/unsup
#
# VLAN Type  SAID       MTU   Parent RingNo BridgeNo Stp  BrdgMode Trans1 Trans2
# ---- ----- ---------- ----- ------ ------ -------- ---- -------- ------ ------
# 1    enet  100001     1500  -      -      -        -    -        0      0
# 10   enet  100010     1500  -      -      -        -    -        0      0
# 20   enet  100020     610   -      -      -        -    -        0      0
# 30   enet  100030     1500  -      -      -        -    -        0      0
# 1002 fddi  101002     1500  -      -      -        -    -        0      0
# 1003 tr    101003     1500  -      -      -        -    -        0      0
# 1004 fdnet 101004     1500  -      -      -        ieee -        0      0
# 1005 trnet 101005     1500  -      -      -        ibm  -        0      0
#
# Remote SPAN VLANs
# ------------------------------------------------------------------------------
# 10

# Using overridden

# Before state:
# -------------
#
# vios#show vlan
# VLAN Name                             Status    Ports
# ---- -------------------------------- --------- -------------------------------
# 1    default                          active    Gi0/1, Gi0/2
# 10   vlan_10                          active
# 20   vlan_20                          act/lshut
# 30   vlan_30                          sus/lshut
# 1002 fddi-default                     act/unsup
# 1003 token-ring-default               act/unsup
# 1004 fddinet-default                  act/unsup
# 1005 trnet-default                    act/unsup
#
# VLAN Type  SAID       MTU   Parent RingNo BridgeNo Stp  BrdgMode Trans1 Trans2
# ---- ----- ---------- ----- ------ ------ -------- ---- -------- ------ ------
# 1    enet  100001     1500  -      -      -        -    -        0      0
# 10   enet  100010     1500  -      -      -        -    -        0      0
# 20   enet  100020     610   -      -      -        -    -        0      0
# 30   enet  100030     1500  -      -      -        -    -        0      0
# 1002 fddi  101002     1500  -      -      -        -    -        0      0
# 1003 tr    101003     1500  -      -      -        -    -        0      0
# 1004 fdnet 101004     1500  -      -      -        ieee -        0      0
# 1005 trnet 101005     1500  -      -      -        ibm  -        0      0
#
# Remote SPAN VLANs
# ------------------------------------------------------------------------------
# 10

- name: Override device configuration of all VLANs with provided configuration
  ios_vlans:
    config:
      - name: Vlan_10
        vlan_id: 10
        mtu: 1000
    state: overridden

# After state:
# ------------
#
# vios#show vlan
# VLAN Name                             Status    Ports
# ---- -------------------------------- --------- -------------------------------
# 10   Vlan_10                          active
#
# VLAN Type  SAID       MTU   Parent RingNo BridgeNo Stp  BrdgMode Trans1 Trans2
# ---- ----- ---------- ----- ------ ------ -------- ---- -------- ------ ------
# 10   enet  100010     1000  -      -      -        -    -        0      0

# Using replaced

# Before state:
# -------------
#
# vios#show vlan
# VLAN Name                             Status    Ports
# ---- -------------------------------- --------- -------------------------------
# 1    default                          active    Gi0/1, Gi0/2
# 10   vlan_10                          active
# 20   vlan_20                          act/lshut
# 30   vlan_30                          sus/lshut
# 1002 fddi-default                     act/unsup
# 1003 token-ring-default               act/unsup
# 1004 fddinet-default                  act/unsup
# 1005 trnet-default                    act/unsup
#
# VLAN Type  SAID       MTU   Parent RingNo BridgeNo Stp  BrdgMode Trans1 Trans2
# ---- ----- ---------- ----- ------ ------ -------- ---- -------- ------ ------
# 1    enet  100001     1500  -      -      -        -    -        0      0
# 10   enet  100010     1500  -      -      -        -    -        0      0
# 20   enet  100020     610   -      -      -        -    -        0      0
# 30   enet  100030     1500  -      -      -        -    -        0      0
# 1002 fddi  101002     1500  -      -      -        -    -        0      0
# 1003 tr    101003     1500  -      -      -        -    -        0      0
# 1004 fdnet 101004     1500  -      -      -        ieee -        0      0
# 1005 trnet 101005     1500  -      -      -        ibm  -        0      0
#
# Remote SPAN VLANs
# ------------------------------------------------------------------------------
# 10

- name: Replaces device configuration of listed VLANs with provided configuration
  ios_vlans:
    config:
      - vlan_id: 20
        name: Test_VLAN20
        mtu: 700
        shutdown: disabled
      - vlan_id: 30
        name: Test_VLAN30
        mtu: 1000
    state: replaced

# After state:
# ------------
#
# vios#show vlan
# VLAN Name                             Status    Ports
# ---- -------------------------------- --------- -------------------------------
# 1    default                          active    Gi0/1, Gi0/2
# 10   vlan_10                          active
# 20   Test_VLAN20                      active
# 30   Test_VLAN30                      sus/lshut
# 1002 fddi-default                     act/unsup
# 1003 token-ring-default               act/unsup
# 1004 fddinet-default                  act/unsup
# 1005 trnet-default                    act/unsup
#
# VLAN Type  SAID       MTU   Parent RingNo BridgeNo Stp  BrdgMode Trans1 Trans2
# ---- ----- ---------- ----- ------ ------ -------- ---- -------- ------ ------
# 1    enet  100001     1500  -      -      -        -    -        0      0
# 10   enet  100010     1500  -      -      -        -    -        0      0
# 20   enet  100020     700   -      -      -        -    -        0      0
# 30   enet  100030     1000  -      -      -        -    -        0      0
# 1002 fddi  101002     1500  -      -      -        -    -        0      0
# 1003 tr    101003     1500  -      -      -        -    -        0      0
# 1004 fdnet 101004     1500  -      -      -        ieee -        0      0
# 1005 trnet 101005     1500  -      -      -        ibm  -        0      0
#
# Remote SPAN VLANs
# ------------------------------------------------------------------------------
# 10

# Using deleted

# Before state:
# -------------
#
# vios#show vlan
# VLAN Name                             Status    Ports
# ---- -------------------------------- --------- -------------------------------
# 1    default                          active    Gi0/1, Gi0/2
# 10   vlan_10                          active
# 20   vlan_20                          act/lshut
# 30   vlan_30                          sus/lshut
# 1002 fddi-default                     act/unsup
# 1003 token-ring-default               act/unsup
# 1004 fddinet-default                  act/unsup
# 1005 trnet-default                    act/unsup
#
# VLAN Type  SAID       MTU   Parent RingNo BridgeNo Stp  BrdgMode Trans1 Trans2
# ---- ----- ---------- ----- ------ ------ -------- ---- -------- ------ ------
# 1    enet  100001     1500  -      -      -        -    -        0      0
# 10   enet  100010     1500  -      -      -        -    -        0      0
# 20   enet  100020     610   -      -      -        -    -        0      0
# 30   enet  100030     1500  -      -      -        -    -        0      0
# 1002 fddi  101002     1500  -      -      -        -    -        0      0
# 1003 tr    101003     1500  -      -      -        -    -        0      0
# 1004 fdnet 101004     1500  -      -      -        ieee -        0      0
# 1005 trnet 101005     1500  -      -      -        ibm  -        0      0
#
# Remote SPAN VLANs
# ------------------------------------------------------------------------------
# 10

- name: Delete attributes of given VLANs
  ios_vlans:
    config:
      - vlan_id: 10
      - vlan_id: 20
    state: deleted

# After state:
# -------------
#
# vios#show vlan
# VLAN Name                             Status    Ports
# ---- -------------------------------- --------- -------------------------------
# 1    default                          active    Gi0/1, Gi0/2
# 30   vlan_30                          sus/lshut
# 1002 fddi-default                     act/unsup
# 1003 token-ring-default               act/unsup
# 1004 fddinet-default                  act/unsup
# 1005 trnet-default                    act/unsup
#
# VLAN Type  SAID       MTU   Parent RingNo BridgeNo Stp  BrdgMode Trans1 Trans2
# ---- ----- ---------- ----- ------ ------ -------- ---- -------- ------ ------
# 1    enet  100001     1500  -      -      -        -    -        0      0
# 30   enet  100030     1500  -      -      -        -    -        0      0
# 1002 fddi  101002     1500  -      -      -        -    -        0      0
# 1003 tr    101003     1500  -      -      -        -    -        0      0
# 1004 fdnet 101004     1500  -      -      -        ieee -        0      0
# 1005 trnet 101005     1500  -      -      -        ibm  -        0      0

# Using Deleted without any config passed
#"(NOTE: This will delete all of configured vlans attributes)"

# Before state:
# -------------
#
# vios#show vlan
# VLAN Name                             Status    Ports
# ---- -------------------------------- --------- -------------------------------
# 1    default                          active    Gi0/1, Gi0/2
# 10   vlan_10                          active
# 20   vlan_20                          act/lshut
# 30   vlan_30                          sus/lshut
# 1002 fddi-default                     act/unsup
# 1003 token-ring-default               act/unsup
# 1004 fddinet-default                  act/unsup
# 1005 trnet-default                    act/unsup
#
# VLAN Type  SAID       MTU   Parent RingNo BridgeNo Stp  BrdgMode Trans1 Trans2
# ---- ----- ---------- ----- ------ ------ -------- ---- -------- ------ ------
# 1    enet  100001     1500  -      -      -        -    -        0      0
# 10   enet  100010     1500  -      -      -        -    -        0      0
# 20   enet  100020     610   -      -      -        -    -        0      0
# 30   enet  100030     1500  -      -      -        -    -        0      0
# 1002 fddi  101002     1500  -      -      -        -    -        0      0
# 1003 tr    101003     1500  -      -      -        -    -        0      0
# 1004 fdnet 101004     1500  -      -      -        ieee -        0      0
# 1005 trnet 101005     1500  -      -      -        ibm  -        0      0
#
# Remote SPAN VLANs
# ------------------------------------------------------------------------------
# 10

- name: Delete attributes of ALL VLANs
  ios_vlans:
    state: deleted

# After state:
# -------------
#
# vios#show vlan
# VLAN Name                             Status    Ports
# ---- -------------------------------- --------- -------------------------------
# 1    default                          active    Gi0/1, Gi0/2
# 1002 fddi-default                     act/unsup
# 1003 token-ring-default               act/unsup
# 1004 fddinet-default                  act/unsup
# 1005 trnet-default                    act/unsup
#
# VLAN Type  SAID       MTU   Parent RingNo BridgeNo Stp  BrdgMode Trans1 Trans2
# ---- ----- ---------- ----- ------ ------ -------- ---- -------- ------ ------
# 1    enet  100001     1500  -      -      -        -    -        0      0
# 1002 fddi  101002     1500  -      -      -        -    -        0      0
# 1003 tr    101003     1500  -      -      -        -    -        0      0
# 1004 fdnet 101004     1500  -      -      -        ieee -        0      0
# 1005 trnet 101005     1500  -      -      -        ibm  -        0      0

"""
RETURN = """
before:
  description: The configuration as structured data prior to module invocation.
  returned: always
  type: list
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
after:
  description: The configuration as structured data after module completion.
  returned: when changed
  type: list
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
commands:
  description: The set of commands pushed to the remote device.
  returned: always
  type: list
  sample: ['vlan 20', 'name vlan_20', 'mtu 600', 'remote-span']
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.ios.plugins.module_utils.network.ios.argspec.vlans.vlans import (
    VlansArgs,
)
from ansible_collections.cisco.ios.plugins.module_utils.network.ios.config.vlans.vlans import (
    Vlans,
)


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(
        argument_spec=VlansArgs.argument_spec, supports_check_mode=True
    )

    result = Vlans(module).execute_module()
    module.exit_json(**result)


if __name__ == "__main__":
    main()
