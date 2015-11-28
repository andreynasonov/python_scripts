#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

import psutil

otstup = "%s %5s    %s %-35s    %s %-5s"

def collect_pids():
    pids = []
    for p in psutil.pids():
        pids.append(p)
    return pids

def calc_swap(arg):
    result = []
    proc = psutil.Process(pid=arg).memory_maps(grouped=False)
    if proc:
        for s in proc:
            theSum = 0
            result.append(s.swap)
            for n in result:
                theSum = theSum + n
        if theSum > 0:
            print(otstup % ("Pid:", psutil.Process(pid=arg).pid, "Process name:", psutil.Process(pid=arg).name(), "Swap usage:", str(theSum / 1024) + 'K'))

for i in collect_pids():
    calc_swap(i)
