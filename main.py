import netaddr

class network:
    def __init__(self, ip, cidr=None):
        self.IP = netaddr.IPNetwork(ip)
        self.Network = self.IP.network
        if cidr is None:
            cidr = self.IP.prefixlen 
        else: self.IP.prefixlen = cidr

        self.ip_list = list(self.IP)
        self.SIZE = len(self.ip_list)
        self.NAME = f"NETWORK_{self.Network}/{cidr}"
        self.Broadcast = self.IP.broadcast
        self.Netmask = self.IP.netmask


    def name(self):
        return self.NAME
    def size(self):
        return self.SIZE
    def broadcast(self):
        return self.Broadcast
    def all(self):
        return self.NAME, self.SIZE, self.Netmask, self.Broadcast
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
    net1 = network('192.168.0.0/24')
    print(net1.all())

    host1 = Host(22, '192.168.0.2', "lol")
    print(host1.name())