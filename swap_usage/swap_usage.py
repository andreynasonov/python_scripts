#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

import psutil

otstup = "%s %5s    %s %-35s    %s %-5s"

def collect_pids():
    pids = []
    for p in psutil.pids():
        pids.append(p)
    return pids

def proc_info(arg):
    result = []
    proc_info = []
    proc = psutil.Process(pid=arg).memory_maps(grouped=False)
    if proc:
        for s in proc:
            theSum = 0
            result.append(s.swap)
            for n in result:
                theSum = theSum + n
        if theSum > 0:
            proc_info.extend([psutil.Process(pid=arg).pid, psutil.Process(pid=arg).name(), theSum])
    return proc_info
    
def sort_swap_usage():
    result = []
    for p in collect_pids():
        if proc_info(p):
            result.extend([proc_info(p)])
    return sorted(result, key=lambda x: x[2])
    
for s in sort_swap_usage():
    print(otstup % ("Pid:", s[0], "Process name:", s[1], "Swap usage:", str(s[2] / 1024 ) + ' K'))
