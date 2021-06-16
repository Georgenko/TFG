#encoding:utf-8

from hebra import Hebra



class PoolHebras:
    def __init__(self,num_hebras,monitor):
        self.num_hebras=num_hebras
        self.monitor=monitor
        
        hebras=[Hebra(i,monitor) for i in range(num_hebras)]
        [t.start() for t in hebras]