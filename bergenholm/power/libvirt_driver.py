#!/usr/bin/env python

import argparse
import libvirt

try:
    from bergenholm.power import status
except:
    class status(object):
        ON = "on"
        OFF = "off"
        UNKNOWN = "unknown"


def main(url=None, uuid=None, command=None):

    c = libvirt.open(url)
    vm = c.lookupByUUIDString(uuid)

    if command == "start":
        vm.create()
    elif command == "stop":
        vm.destroy()
    elif command == "restart":
        vm.destroy()
        vm.create()
    elif command == "status":
        power_state = vm.state()[0]
        if power_state == libvirt.VIR_DOMAIN_RUNNING:
            return status.ON
        elif power_state == libvirt.VIR_DOMAIN_SHUTOFF:
            return status.OFF
        else:
            return status.UNKNOWN
    else:
        raise exception("unknown command: %s" % command)


def power_on(**params):
    return main(url=params["libvirt_url"],
                uuid=params["uuid"],
                command="start")


def power_off(**params):
    return main(url=params["libvirt_url"],
                uuid=params["uuid"],
                command="stop")


def power_reset(**params):
    return main(url=params["libvirt_url"],
                uuid=params["uuid"],
                command="reset")


def power_status(**params):
    return main(url=params["libvirt_url"],
                uuid=params["uuid"],
                command="status")


# Start program
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Power control for Libvirt')
    parser.add_argument('uuid', metavar='UUID',
                        help='UUID of VM')
    parser.add_argument('command', metavar='COMMAND',
                        help='subcommand (start/stop/reboot/status)')
    parser.add_argument('--url', dest='url',
                        default="qemu:///system",
                        help='IP address of Libvirtd')

    args = parser.parse_args()
    print(main(**args.__dict__))
