#!/usr/bin/python

from scapy.all import *
from scapy.layers import dhcp

IFACE = "eth0"
NETWORK = "192.168.1.0/24"
SERVER = "192.168.1.254"
DOMAIN = "localnet"

DHCP_DISCOVER = 1
DHCP_OFFER = 2
DHCP_REQUEST = 3
DHCP_DECLINE = 4
DHCP_ACK = 5
DHCP_NACK = 6
DHCP_RELEASE = 7
DHCP_INFORM = 8
DHCP_FORCE_RENEW = 9
DHCP_LEASE_QUERY = 10
DHCP_LEASE_UNASSIGNED = 11
DHCP_LEASE_UNKNOWN = 12
DHCP_LEASE_ACTIVE = 13


class BOOTP_am(dhcp.BOOTP_am):

    def parse_options(self, pool=None, network=NETWORK,
                      server=None, file=None, **kwargs):

        network_addr, mask = (network.split("/") + ["32"])[:2]
        mask = itom(int(mask))
        self.netmask = ltoa(mask)
        self.network = ltoa(atol(network_addr) & mask)
        self.broadcast = ltoa(atol(self.network) | (0xffffffff & ~ mask))

        self.server_id = server or SERVER

        self.leases = {}
        self.file = file + chr(0) * (128 - len(file))

        used_ips = [server, self.network, self.broadcast]
        if pool is None:
            pool = Net(network)
        elif isinstance(pool, str):
            pool = Net(pool)
        if isinstance(pool, Gen):
            pool = [k for k in pool if k not in used_ips]
            pool.reverse()
        if len(pool) == 1:
            pool, = pool
        self.pool = pool

    def make_reply(self, req):
        mac = req.src
        if isinstance(self.pool, list):
            if not mac in self.leases:
                self.leases[mac] = self.pool.pop()
            ip = self.leases[mac]
        else:
            ip = self.pool

        repb = req.getlayer(BOOTP).copy()
        repb.op = "BOOTREPLY"
        repb.yiaddr = ip
        repb.siaddr = self.server_id
        repb.ciaddr = '0.0.0.0'
        repb.giaddr = '0.0.0.0'
        if self.file is not None:
            repb.file = self.file
        del(repb.payload)

        rep = Ether(dst=mac) / IP(dst=ip) / \
            UDP(sport=req.dport, dport=req.sport) / repb
        return rep


class DHCP_am(BOOTP_am):

    function_name = "dhcpd"

    def parse_options(self, **kwargs):
        super(DHCP_am, self).parse_options(**kwargs)

        self.router = kwargs.get('router') or self.server_id
        self.name_server = kwargs.get('name_server') or self.server_id
        self.domain = kwargs.get('domain')
        self.lease_time = kwargs.get('lease_time')
        self.renewal_time = kwargs.get('renewal_time')
        ipxe_url = kwargs.get('ipxe_url', "")
        self.ipxe_url = ipxe_url + chr(0) * (128 - len(ipxe_url))

    def print_reply(self, req, reply):
        mac = req[Ether].src
        opts = {op[0]: op[1] for op in req[DHCP].options}
        msg_type = opts.get('message-type')
        requested_ip = opts.get("requested_addr") or req[BOOTP].ciaddr
        if msg_type == DHCP_DISCOVER:
            print("DHCPDISCOVER: mac=%s" % mac)
        elif msg_type == DHCP_REQUEST:
            print("DHCPREQUEST:  mac=%s, IP=%s" % (mac, requested_ip))
        else:
            print("DHCP:         mac=%s, type=%d" % (mac, msg_type))

        opts = {op[0]: op[1] for op in reply[DHCP].options}
        msg_type = opts.get('message-type')
        your_ip = reply[BOOTP].yiaddr
        if msg_type == DHCP_OFFER:
            print("DHCPOFFER:    mac=%s, IP=%s" % (mac, your_ip))
        elif msg_type == DHCP_ACK:
            print("DHCPACK:      mac=%s, IP=%s" % (mac, your_ip))
        elif msg_type == DHCP_NACK:
            print("DHCPNACK:     mac=%s, IP=%s" % (mac, your_ip))
        else:
            print("DHCP:         mac=%s, type=%d" % (mac, msg_type))

    def make_reply(self, req):
        resp = BOOTP_am.make_reply(self, req)
        if DHCP in req:
            if (77, "iPXE") in req[DHCP].options:
                resp[BOOTP].file = self.ipxe_url
            opts = {op[0]: op[1] for op in req[DHCP].options}
            if opts['message-type'] == DHCP_DISCOVER:
                msg_type = DHCP_OFFER
            elif opts['message-type'] == DHCP_REQUEST:
                mac = req[Ether].src
                req_addr = opts.get('requested_addr') or req[BOOTP].ciaddr
                if req_addr == self.leases.get(mac):
                    msg_type = DHCP_ACK
                else:
                    msg_type = DHCP_NACK
            else:
                msg_type = opts['message-type']
            dhcp_options = [("message-type", msg_type),
                            ("server_id", self.server_id),
                            ("domain", self.domain),
                            ("router", self.router),
                            ("name_server", self.name_server),
                            ("broadcast_address", self.broadcast),
                            ("subnet_mask", self.netmask),
                            ("renewal_time", self.renewal_time),
                            ("lease_time", self.lease_time),
                            "end"
                            ]
            resp /= DHCP(options=dhcp_options)
        return resp


dhcp_server = DHCP_am(iface='eth1',
                      server='192.168.10.254',
                      network='192.168.10.0/24',
                      name_server='192.168.0.254',
                      domain='example.com',
                      renewal_time=600,
                      lease_time=3600,
                      file='undionly.kpxe',
                      ipxe_url='http://192.168.10.254/ipxe/script/${uuid}')

dhcp_server()
