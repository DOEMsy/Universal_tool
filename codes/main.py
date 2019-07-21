import os
import numpy
import time

import Pkg_Waining
import Pkg_test
import Pkg_TranstoZh
import Pkg_Clt

Ip = {'test':Pkg_test,
    'trs':Pkg_TranstoZh,
    'clt':Pkg_Clt
    }

def Pause(str="",stime=0):
    if str!="":
        print(str)
    if stime==0:
        os.system("pause>nul")
    else:
        time.sleep(stime)



if __name__ == "__main__":
    while True:
        inp = input("-$:").split(' ',1)
        if inp[0] in Ip:
            Tp = Ip[inp[0]]
        else:
            Tp = Pkg_Waining
        Tp.begin(inp)
        
