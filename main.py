import netaddr

class network:
    def __init__(self, ip, cidr):
        self.IP = netaddr.IPNetwork(ip)
        self.CIDR = self.IP.prefixlen = cidr
        self.ip_list = list(self.IP)
        self.SIZE = len(self.ip_list)
        self.NAME = f"NETWORK_{ip}/{cidr}"
        # ip = IPNetwork('192.0.2.0/24')

        # ip.ip
        # IPAddress('192.0.2.0')

        # ip.network, ip.broadcast
        # (IPAddress('192.0.2.0'), IPAddress('192.0.2.255'))

        # ip.netmask, ip.hostmask
        # (IPAddress('255.255.255.0'), IPAddress('0.0.0.255'))

        # ip.size
        # 256

    def name(self):
        return self.NAME
    def size(self):
        return self.SIZE

class Host:
    def __init__(self, num, ip, dev=None): 
        self.IP = netaddr.IPAddress(ip)
        self.MAC = netaddr.EUI('00-1B-77-49-54-FD')
        if dev is None:
            dev = "HOST"
        self.NAME = dev + str(num)

    def name(self):
        return self.NAME

if __name__ == "__main__":
    net1 = network('192.168.0.0', 24)
    print(net1.size())

    host1 = Host(22, '192.168.0.2', "lol")
    print(host1.name())