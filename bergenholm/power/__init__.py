from bergenholm.power import dummy_driver
from bergenholm.power import vmware_driver
from bergenholm.power import ipmi_driver

DRIVERS = {
    "dummy": dummy_driver,
    "vmware": vmware_driver,
    "ipmi": ipmi_driver
}


def power_on(uuid, power_driver=None, **params):
    DRIVERS[power_driver].power_on(uuid, **params)


def power_off(uuid, power_driver=None, **params):
    DRIVERS[power_driver].power_off(uuid, **params)


def power_reset(uuid, power_driver=None, **params):
    DRIVERS[power_driver].power_reset(uuid, **params)


def power_status(uuid, power_driver=None, **params):
    return {"power": DRIVERS[power_driver].power_status(uuid, **params)}
