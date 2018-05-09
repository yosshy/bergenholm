#!/usr/bin/env python

import argparse
import subprocess
import sys


try:
    from bergenholm.power import status
except:
    class status(object):
        ON = "on"
        OFF = "off"
        UNKNOWN = "unknown"


class IPMItool(object):

    def __init__(self, host, port, user, password, interface):
        self.cmdline = ["ipmitool",
                        "-H", host,
                        "-p", str(port),
                        "-U", user,
                        "-P", password,
                        "-I", interface,
                        "chassis"]

    def run(self, *args):
        return subprocess.check_output(self.cmdline + list(args))


def main(host=None, port=623, user=None, password=None, command=None,
         interface='lanplus'):

    ipmitool = IPMItool(host, port, user, password, interface)

    if command == "start":
        ipmitool.run("bootdev", "pxe")
        ipmitool.run("power", "on")
    elif command == "stop":
        ipmitool.run("power", "off")
    elif command == "restart":
        ipmitool.run("power", "reset")
    elif command == "status":
        out = ipmitool.run("power", "status")
        if out.strip().lower().endswith("on"):
            return status.ON
        elif out.strip().lower().endswith("off"):
            return status.OFF
        else:
            return status.UNKNOWN
    else:
        raise Exception("unknown command: %s" % command)


def power_on(**params):
    return main(host=params["ipmi_host"],
                user=params["ipmi_user"],
                password=params["ipmi_password"],
                command="on")


def power_off(**params):
    return main(host=params["ipmi_host"],
                user=params["ipmi_user"],
                password=params["ipmi_password"],
                command="off")


def power_reset(**params):
    return main(host=params["ipmi_host"],
                user=params["ipmi_user"],
                password=params["ipmi_password"],
                command="reset")


def power_status(**params):
    return main(host=params["ipmi_host"],
                user=params["ipmi_user"],
                password=params["ipmi_password"],
                command="status")


# Start program
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Power control for IPMI')
    parser.add_argument('command', metavar='COMMAND',
                        help='subcommand (start/stop/reboot/status)')
    parser.add_argument('--host', dest='host',
                        default="127.0.0.1",
                        help='IP address of IPMI LAN I/F')
    parser.add_argument('--port', dest='port',
                        default=623,
                        help='Port of IPMI LAN I/F')
    parser.add_argument('--user', dest='user',
                        default="Admin",
                        help='User account of IPMI LAN I/F')
    parser.add_argument('--password', dest='password',
                        default="",
                        help='User password of IPMI LAN I/F')
    parser.add_argument('--interface', dest='interface',
                        default="lanplus",
                        help='Type of IPMI LAN I/F')

    args = parser.parse_args()
    print(main(**args.__dict__))
