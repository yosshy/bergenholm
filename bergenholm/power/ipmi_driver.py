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

    def __init__(host, port, user, password):
        self.host = host
        self.port = str(port)
        self.user = user
        self.password = password

    def run(*args):
        cmdline = ["ipmitool",
                   "-H", self.host,
                   "-p", self.port,
                   "-U", self.user,
                   "-P", self.password,
                   "chassis"]
        return subprocess.check_output(cmdline + args)


def main(host=None, port=623, user=None, password=None, command=None):

    ipmitool = IPMItool(host, port, user, password)

    if command == "start":
        ipmitool.run("bootdev", "pxe")
        ipmitool.run("power", "on")
    elif command == "stop":
        ipmitool.run("power", "off")
    elif command == "restart":
        ipmitool.run("power", "reset")
    elif command == "status":
        out = ipmitool.run("power", "status")
        if out.strip().endswith("On"):
            return status.ON
        elif out.strip().endswith("Off"):
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

    args = parser.parse_args()
    print(main(**args.__dict__))
