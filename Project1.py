class Resource:
    def __init__(self, name, manufacturer, total, allocated):
        self._name = name
        self._manufacturer = manufacturer
        self._total = total  #inchqan ka inventory um
        self._allocated = allocated #inchqanna ogtaogrcvel

    @property
    def name(self):
        return self._name
    
    @property
    def manufacturer(self):
        return self._manufacturer

    @property
    def total(self):
        return self._total

    @property
    def allocated(self):
        return self._allocated
    
    @property
    def category(self):
        return self.__class__.__name__.lower()


    def __str__(self):
        return self.name
    
    def __repr__(self):
        return f"Resource: name={self._name}, manufacturer={self._manufacturer}, total={self._total}, allocated={self._allocated}"

    def claim(self, n):
        if self._total - self._allocated >= n:
            self._allocated += n 
        else:
            raise ValueError("Value error")
        
    def freeup(self, n):
        if self._allocated >=n:
            self._allocated -=n
        else:
            raise ValueError("Value error")
        
    def died(self, n):
        if self._total >= n:
            self._total -= n
            self._allocated -= n
        else:
            raise ValueError("Value error")
        
    def purchased(self, n):
        self._total +=n

    
class CPU(Resource):
    def __init__(self, name, manufacturer, total, allocated, cores):
        super().__init__(name, manufacturer, total, allocated)
        self._cores = cores

    @property
    def cores(self):
        return self._cores
    
    def __repr__(self):
        return f"{super().__repr__()}, cores={self._cores}"


class Storage(Resource):
    def __init__(self, name, manufacturer, total, allocated, capacity_GB):
        super().__init__(name, manufacturer, total, allocated)
        self._capacity_GB = capacity_GB

    @property
    def capacity_GB(self):
        return self._capacity_GB

    def __repr__(self):
        return f"{super().__repr__()}, capacity_GB={self._capacity_GB}"
    

class HDD(Storage):
    def __init__(self, name, manufacturer, total, allocated, capacity_GB, size, rpm):
        super().__init__(name, manufacturer, total, allocated, capacity_GB)
        self._size = size
        self._rpm = rpm

    @property
    def size(self):
        return self._size

    @property
    def rpm(self):
        return self._rpm

    def __repr__(self):
        return f"{super().__repr__()}, size={self._size}, rpm={self._rpm}"



class SSD(Storage):
    def __init__(self, name, manufacturer, total, allocated, capacity_GB, interface, socket, power_watts):
        super().__init__(name, manufacturer, total, allocated, capacity_GB)
        self._interface = interface
        self._socket = socket
        self._power_watts = power_watts

    @property
    def interface(self):
        return self._interface
    
    @property
    def socket(self):
        return self._socket
    
    @property
    def power_watts(self):
        return self._power_watts

    def __repr__(self):
        return f"{super().__repr__()}, interface={self._interface}"



cpu = CPU("Intel Core i9-9900K", "Intel", 10, 5, 6)
cpu.claim(2)
cpu.purchased(3)


hdd = HDD("Seagate Barracuda", "Seagate", 20, 8, 2000, "3.5\"", 7200)
hdd.claim(5)
hdd.freeup(3)
hdd.died(2)

ssd = SSD("Samsung 970 EVO", "Samsung", 15, 2, 500, "PCIe NMVe 3.0 x4", 1, 3000 )
ssd.claim(2)
ssd.freeup(1)
ssd.purchased(1)
