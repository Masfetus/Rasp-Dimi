from os import system

CPUINFO_PATH = "/proc/cpuinfo"
MODELINFO_PATH = "/sys/firmware/devicetree/base/model"

def getRaspModel():
    result = ""
    try:
        f = open(MODELINFO_PATH,'r')
        for line in f:
            result = line
        f.close()
    except:
        result = "ERROR-RETRIEVING-MODEL"
    return result
    
print(getRaspModel())