from bergenholm.power import dummy_driver
from bergenholm.power import vmware_driver
from bergenholm.power import ipmi_driver

DRIVERS = {
    "dummy": dummy_driver,
    "vmware": vmware_driver,
    "ipmi": ipmi_driver
}


def power_on(power_driver=None, **params):
    DRIVERS[power_driver].power_on(**params)


def power_off(power_driver=None, **params):
    DRIVERS[power_driver].power_off(**params)


def power_reset(power_driver=None, **params):
    DRIVERS[power_driver].power_reset(**params)


def power_status(power_driver=None, **params):
    return {"power": DRIVERS[power_driver].power_status(**params)}
