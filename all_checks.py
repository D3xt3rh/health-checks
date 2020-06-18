import shutil
import sys
import os
def check_reboot():

    #Rerturns True if the computer has apending reboot.
    return os.path.exists("/run/reboot-required")#/run/reboot-required

def check_disk_full(disk, min_gb, min_percent):
    #Retrun if there is enough space on the disk,otherwise false.
    du = shutil.disk_usage(disk)
    #calculate the prcentage of free space
    percent_free = 100*du.free/du.total
    #calculate how many free gigabytes
    gigabytes_free = du.free/2**30
    if percent_free < min_percent or gigabytes_free < min_gb:
        return True
    return False
    
def main():
    if check_reboot():
        print("Pending Reboot.")
        sys.exit(1)
    if check_disk_full(disk="/",min_gb=2, min_percent=10):
        print("DISK FULL.")
        sys.exit(1)

        print("Everything OK.")
        sys.exit(0)
    main() 
