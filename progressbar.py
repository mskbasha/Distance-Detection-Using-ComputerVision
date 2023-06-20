import time
from IPython.display import clear_output
from matplotlib import pyplot as plt
import math
class progressbar:
    def __init__(self,timegap):
        self.start_time = time.time()
        self.timegap=timegap
        self.time_ellapsed=0
        self.data=[]
        self.extraword=''
    def print(self,current,max,string='',clear=True,graph=False,error=0,graph_length=10):
        progress=round(100*current/max)
        if time.time()-self.start_time>self.timegap:
            self.start_time = time.time()
            self.time_ellapsed+=self.timegap
            self.extraword+='\n Time taken ='+str(self.time_ellapsed)+'sec'
            if clear:
                clear_output(wait=True)
            print('['+'-'*progress+'>'+'.'*(100-progress)+']','\n',string,flush=True)
            if graph:
                if len(self.data)>graph_length:
                    self.data.pop(0)
                    # print(self.data,graph_length,len(self.data))
                self.data.append([self.time_ellapsed,error])
                plt.plot([x[0] for x in self.data],[x[1] for x in self.data])
                plt.pause(0.01)
            return
        else:
            return