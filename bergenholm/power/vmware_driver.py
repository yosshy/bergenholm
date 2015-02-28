#!/usr/bin/env python
#
# Copyright (c) 2015 A.Yoshiyama <akirayoshiyama@gmail.com>
#
# From VMware vSphere Python SDK
# Copyright (c) 2008-2013 VMware, Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
"""

import argparse
import time

from pyVim import connect
from pyVmomi import vim, vmodl

try:
    from bergenholm.power import status
except:
    class status(object):
        ON = "on"
        OFF = "off"
        UNKNOWN = "unknown"


def find_vm(virtual_machine, uuid, depth=1):
    """
    find a virtual machine with specified BIOS UUID.
    """
    maxdepth = 10

    if hasattr(virtual_machine, 'childEntity'):
        if depth > maxdepth:
            return
        for c in virtual_machine.childEntity:
            find_vm(c, uuid, depth + 1)
        return

    if virtual_machine.summary.config.uuid == uuid:
        return virtual_machine


def main(host=None, port=None, user=None, password=None, uuid=None,
         command=None):

    service = None
    try:
        service = connect.SmartConnect(host=host, port=port,
                                       user=user, pwd=password)

        content = service.RetrieveContent()

        for child in content.rootFolder.childEntity:
            if not hasattr(child, 'vmFolder'):
                continue

            for virtual_machine in child.vmFolder.childEntity:
                VM = find_vm(virtual_machine, uuid, 10)
                if VM:
                    break
            else:
                continue

            if command == "start":
                spec = vim.vm.ConfigSpec()
                spec.extraConfig = [vim.option.OptionValue(
                    key='bios.bootDeviceClasses',
                    value='allow:net')]
                VM.ReconfigVM_Task(spec)

                time.sleep(2)
                VM.PowerOnVM_Task()
            elif command == "stop":
                VM.PowerOffVM_Task()
            elif command == "restart":
                VM.ResetVM_Task()
            elif command == "detail":
                import pprint
                return pprint.pformat(VM.config)
            elif command == "status":
                if VM.runtime.powerState == "poweredOn":
                    return status.ON
                elif VM.runtime.powerState == "poweredOff":
                    return status.OFF
                else:
                    return status.UNKNOWN

    except vmodl.MethodFault as error:
        print "Caught vmodl fault : " + error.msg
        return -1
    finally:
        connect.Disconnect(service)

    return 0


def power_on(uuid, **params):
    return main(host=params["vmware_host"],
                port=params.get("vmware_port", 443),
                user=params["vmware_user"],
                password=params["vmware_password"],
                uuid=uuid,
                command="start")


def power_off(uuid, **params):
    return main(host=params["vmware_host"],
                port=params.get("vmware_port", 443),
                user=params["vmware_user"],
                password=params["vmware_password"],
                uuid=uuid,
                command="stop")


def power_reset(uuid, **params):
    return main(host=params["vmware_host"],
                port=params.get("vmware_port", 443),
                user=params["vmware_user"],
                password=params["vmware_password"],
                uuid=uuid,
                command="restart")


def power_status(uuid, **params):
    return main(host=params["vmware_host"],
                port=params.get("vmware_port", 443),
                user=params["vmware_user"],
                password=params["vmware_password"],
                uuid=uuid,
                command="status")


# Start program
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Power control for VMware ESXi')
    parser.add_argument('uuid', metavar='UUID',
                        help='System (BIOS) UUID of VM')
    parser.add_argument('command', metavar='COMMAND',
                        help='subcommand (start/stop/reboot/status)')
    parser.add_argument('--host', dest='host',
                        default="127.0.0.1",
                        help='IP address of VMware ESXi')
    parser.add_argument('--port', dest='port',
                        default=443, type=int,
                        help='Port of VMware ESXi')
    parser.add_argument('--user', dest='user',
                        default="Admin",
                        help='User account of VMware ESXi')
    parser.add_argument('--password', dest='password',
                        default="",
                        help='User password of VMware ESXi')

    args = parser.parse_args()
    print(main(**args.__dict__))
