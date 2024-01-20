import netaddr 

class host:
    def __init__(self, num, ip, dev): 
        self.IP = netaddr.IPAddress(ip)
        self.MAC = netaddr.EUI('00-1B-77-49-54-FD')
        if self.dev is not None:
            self.dev = dev 
        else: self.dev = "HOST"
        # self.NAME = self.dev + str(num)

    def name(self):
        return self.NAME

    host1 = host(22,'192.168.0.2','router')
    print (host1.name())
