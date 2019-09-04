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
The module file for ios_interfaces
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "network",
}


DOCUMENTATION = """
---
module: ios_interfaces
version_added: 2.9
short_description: Manages interface attributes of Cisco IOS network devices
description: This module manages the interface attributes of Cisco IOS network devices.
author: Sumit Jaiswal (@justjais)
notes:
- Tested against Cisco IOSv Version 15.2 on VIRL
- This module works with connection C(network_cli).
  See L(IOS Platform Options,../network/user_guide/platform_ios.html).
options:
  config:
    description: A dictionary of interface options
    type: list
    suboptions:
      name:
        description:
        - Full name of interface, e.g. GigabitEthernet0/2, loopback999.
        type: str
        required: True
      description:
        description:
        - Interface description.
        type: str
      enabled:
        description:
        - Administrative state of the interface.
        - Set the value to C(true) to administratively enable the interface or C(false) to disable it.
        type: bool
        default: True
      speed:
        description:
        - Interface link speed. Applicable for Ethernet interfaces only.
        type: str
      mtu:
        description:
        - MTU for a specific interface. Applicable for Ethernet interfaces only.
        - Refer to vendor documentation for valid values.
        type: int
      duplex:
        description:
        - Interface link status. Applicable for Ethernet interfaces only, either in half duplex,
          full duplex or in automatic state which negotiates the duplex automatically.
        type: str
        choices: ['full', 'half', 'auto']
  state:
    choices:
    - merged
    - replaced
    - overridden
    - deleted
    default: merged
    description:
    - The state of the configuration after module completion
    type: str
"""

EXAMPLES = """
---

# Using merged

# Before state:
# -------------
#
# vios#show running-config | section ^interface
# interface GigabitEthernet0/1
#  description Configured by Ansible
#  no ip address
#  duplex auto
#  speed auto
# interface GigabitEthernet0/2
#  description This is test
#  no ip address
#  duplex auto
#  speed 1000
# interface GigabitEthernet0/3
#  no ip address
#  duplex auto
#  speed auto

- name: Merge provided configuration with device configuration
  ios_interfaces:
    config:
      - name: GigabitEthernet0/2
        description: 'Configured and Merged by Ansible Network'
        enabled: True
      - name: GigabitEthernet0/3
        description: 'Configured and Merged by Ansible Network'
        mtu: 2800
        enabled: False
        speed: 100
        duplex: full
    state: merged

# After state:
# ------------
#
# vios#show running-config | section ^interface
# interface GigabitEthernet0/1
#  description Configured by Ansible
#  no ip address
#  duplex auto
#  speed auto
# interface GigabitEthernet0/2
#  description Configured and Merged by Ansible Network
#  no ip address
#  duplex auto
#  speed 1000
# interface GigabitEthernet0/3
#  description Configured and Merged by Ansible Network
#  mtu 2800
#  no ip address
#  shutdown
#  duplex full
#  speed 100

# Using replaced

# Before state:
# -------------
#
# vios#show running-config | section ^interface
# interface GigabitEthernet0/1
#  no ip address
#  duplex auto
#  speed auto
# interface GigabitEthernet0/2
#  description Configured by Ansible Network
#  no ip address
#  duplex auto
#  speed 1000
# interface GigabitEthernet0/3
#  mtu 2000
#  no ip address
#  shutdown
#  duplex full
#  speed 100

- name: Replaces device configuration of listed interfaces with provided configuration
  ios_interfaces:
    config:
      - name: GigabitEthernet0/3
        description: 'Configured and Replaced by Ansible Network'
        enabled: False
        duplex: auto
        mtu: 2500
        speed: 1000
    state: replaced

# After state:
# -------------
#
# vios#show running-config | section ^interface
# interface GigabitEthernet0/1
#  no ip address
#  duplex auto
#  speed auto
# interface GigabitEthernet0/2
#  description Configured by Ansible Network
#  no ip address
#  duplex auto
#  speed 1000
# interface GigabitEthernet0/3
#  description Configured and Replaced by Ansible Network
#  mtu 2500
#  no ip address
#  shutdown
#  duplex full
#  speed 1000

# Using overridden

# Before state:
# -------------
#
# vios#show running-config | section ^interface#
# interface GigabitEthernet0/1
#  description Configured by Ansible
#  no ip address
#  duplex auto
#  speed auto
# interface GigabitEthernet0/2
#  description This is test
#  no ip address
#  duplex auto
#  speed 1000
# interface GigabitEthernet0/3
#  description Configured by Ansible
#  mtu 2800
#  no ip address
#  shutdown
#  duplex full
#  speed 100

- name: Override device configuration of all interfaces with provided configuration
  ios_interfaces:
    config:
      - name: GigabitEthernet0/2
        description: 'Configured and Overridden by Ansible Network'
        speed: 1000
      - name: GigabitEthernet0/3
        description: 'Configured and Overridden by Ansible Network'
        enabled: False
        duplex: full
        mtu: 2000
    state: overridden

# After state:
# -------------
#
# vios#show running-config | section ^interface
# interface GigabitEthernet0/1
#  no ip address
#  duplex auto
#  speed auto
# interface GigabitEthernet0/2
#  description Configured and Overridden by Ansible Network
#  no ip address
#  duplex auto
#  speed 1000
# interface GigabitEthernet0/3
#  description Configured and Overridden by Ansible Network
#  mtu 2000
#  no ip address
#  shutdown
#  duplex full
#  speed 100

# Using Deleted

# Before state:
# -------------
#
# vios#show running-config | section ^interface
# interface GigabitEthernet0/1
#  no ip address
#  duplex auto
#  speed auto
# interface GigabitEthernet0/2
#  description Configured by Ansible Network
#  no ip address
#  duplex auto
#  speed 1000
# interface GigabitEthernet0/3
#  description Configured by Ansible Network
#  mtu 2500
#  no ip address
#  shutdown
#  duplex full
#  speed 1000

- name: "Delete module attributes of given interfaces (Note: This won't delete the interface itself)"
  ios_interfaces:
    config:
      - name: GigabitEthernet0/2
    state: deleted

# After state:
# -------------
#
# vios#show running-config | section ^interface
# interface GigabitEthernet0/1
#  no ip address
#  duplex auto
#  speed auto
# interface GigabitEthernet0/2
#  no ip address
#  duplex auto
#  speed auto
# interface GigabitEthernet0/3
#  description Configured by Ansible Network
#  mtu 2500
#  no ip address
#  shutdown
#  duplex full
#  speed 1000

# Using Deleted without any config passed
#"(NOTE: This will delete all of configured resource module attributes from each configured interface)"

# Before state:
# -------------
#
# vios#show running-config | section ^interface
# interface GigabitEthernet0/1
#  no ip address
#  duplex auto
#  speed auto
# interface GigabitEthernet0/2
#  description Configured by Ansible Network
#  no ip address
#  duplex auto
#  speed 1000
# interface GigabitEthernet0/3
#  description Configured by Ansible Network
#  mtu 2500
#  no ip address
#  shutdown
#  duplex full
#  speed 1000

- name: "Delete module attributes of all interfaces (Note: This won't delete the interface itself)"
  ios_interfaces:
    state: deleted

# After state:
# -------------
#
# vios#show running-config | section ^interface
# interface GigabitEthernet0/1
#  no ip address
#  duplex auto
#  speed auto
# interface GigabitEthernet0/2
#  no ip address
#  duplex auto
#  speed auto
# interface GigabitEthernet0/3
#  no ip address
#  duplex auto
#  speed auto

"""

RETURN = """
before:
  description: The configuration as structured data prior to module invocation.
  returned: always
  type: list
  sample: The configuration returned will alwys be in the same format of the paramters above.
after:
  description: The configuration as structured data after module completion.
  returned: when changed
  type: list
  sample: The configuration returned will alwys be in the same format of the paramters above.
commands:
  description: The set of commands pushed to the remote device
  returned: always
  type: list
  sample: ['interface GigabitEthernet 0/1', 'description This is test', 'speed 100']
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.ios.plugins.module_utils.network.ios.argspec.interfaces.interfaces import (
    InterfacesArgs,
)
from ansible_collections.cisco.ios.plugins.module_utils.network.ios.config.interfaces.interfaces import (
    Interfaces,
)


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(
        argument_spec=InterfacesArgs.argument_spec, supports_check_mode=True
    )

    result = Interfaces(module).execute_module()
    module.exit_json(**result)


if __name__ == "__main__":
    main()
