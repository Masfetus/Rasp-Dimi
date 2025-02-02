from os import system
import platform
import pprint

import psutil

result_dict = { 
    "sys": {},
    "cpu": {},
    "memory": {},
    "disk": {}
}


def retrieveSystemInfo():
    uname = platform.uname()
    result_dict["sys"] = uname._asdict()

def retrieveCPUInfo():
    cpufreq = psutil.cpu_freq()
    result_dict["cpu"] = cpufreq._asdict()
    result_dict["cpu"]["physical_cpu"] = psutil.cpu_count(logical=False)
    result_dict["cpu"]["logical_cpu"] = psutil.cpu_count(logical=True)
    result_dict["cpu"]["usage"] = psutil.cpu_percent()

def retrieveMemoryInfo():
    svmem = psutil.virtual_memory()
    swap = psutil.swap_memory()
    result_dict["memory"]["virtual"] = svmem._asdict()
    result_dict["memory"]["swap"] = swap._asdict()

def retrieveDiskInfo():
    partitions = psutil.disk_partitions()
    for partition in partitions:
        usage = psutil.disk_usage(partition.mountpoint)
        result_dict["disk"][partition.mountpoint] = usage._asdict()

retrieveSystemInfo()
retrieveCPUInfo()
retrieveMemoryInfo()
retrieveDiskInfo()

pprint.pprint(result_dict)