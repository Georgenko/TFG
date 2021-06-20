#encoding:utf-8

from proceso import Proceso



class PoolProcesos:
    def __init__(self,num_procesos,monitor):
        self.num_procesos=num_procesos
        self.monitor=monitor        
        
        procesos=[Proceso(i,monitor) for i in range(num_procesos)]
        [p.start() for p in procesos]