#!/usr/bin/env python

import argparse
from pyghmi.ipmi.command import Command

try:
    from bergenholm.power import status
except:
    class status(object):
        ON = "on"
        OFF = "off"
        UNKNOWN = "unknown"


def main(host=None, port=None, user=None, password=None, command=None):

    c = Command(host, user, password, port=port)

    if command == "start":
        c.set_bootdev("network")
        c.set_power("on", wait=True)
    elif command == "stop":
        c.set_power("off", wait=True)
    elif command == "restart":
        c.set_power("reset", wait=True)
    elif command == "status":
        result = c.get_power()["powerstate"]
        if result == "on":
            return status.ON
        elif result == "off":
            return status.OFF
        else:
            return status.UNKNOWN
    else:
        raise exception("unknown command: %s" % command)


def power_on(**params):
    return main(host=params["ipmi_host"],
                user=params["ipmi_user"],
                password=params["ipmi_password"],
                command="start")


def power_off(**params):
    return main(host=params["ipmi_host"],
                user=params["ipmi_user"],
                password=params["ipmi_password"],
                command="stop")


def power_reset(**params):
    return main(host=params["ipmi_host"],
                user=params["ipmi_user"],
                password=params["ipmi_password"],
                command="restart")


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
