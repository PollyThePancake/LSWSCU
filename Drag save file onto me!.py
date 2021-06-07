import sys
import os
import math as m
import numpy as np

np.seterr(all='ignore')

try:
    savefile = sys.argv[1]
except IndexError:
    finished = input("No file dropped! Please drop the save file you want to update the checksum of\nPress enter to close")
    sys.exit()

filesize = os.path.getsize(savefile)

decfile = []

with open(savefile, 'r+b') as file:
    def ChecksumCount(start, end, order, salt):
        checksum = salt
        file.seek(start)
        for a in range(0, m.trunc((end - start) / 4)):
            fileread = file.read(4)
            checksum = np.uint32(int.from_bytes(fileread, byteorder=order, signed=False)) + np.uint32(checksum)
        oldchecksum = int.from_bytes(file.read(4), byteorder=order, signed=False)
        if checksum == oldchecksum:
            finished = input("New checksum already matches the existing one. Press enter to close")
            sys.exit()
        print("\nOld Checksum: " + str(oldchecksum))
        print("\nNew Checksum: " + str(checksum))
        file.seek(end)
        file.write(int(checksum).to_bytes(4, byteorder=order))


    # TCS
    if filesize == 40572:
        print("TCS PC Save File Detected")
        ChecksumCount(8232, 40564, "little", 6031769)
    elif filesize == 32336:
        print("TCS Ps3 Save File Detected")
        ChecksumCount(0, 32332, "big", 6031769)
    elif filesize == 32360:
        print("TCS Xbox 360 Save File Detected")
        ChecksumCount(0, 32356, "big", 6031769)
    elif filesize == 131072:
        print("TCS Wii Save File Detected")
        ChecksumCount(60, 32392, "big", 6031769)

    # LSW2
    elif filesize == 79252:
        print("LSW2 Ps2 (Ps3 Format) Save File Detected")
        ChecksumCount(76272, 77276, "little", 0)
    elif filesize == 960:
        print("LSW2 Ps2 Print Preview Save File Detected")
        ChecksumCount(0, 956, "little", 0)
    elif filesize == 1008:
        print("LSW2 PC/Ps2/Xbox 360 File Detected")
        version = input("Enter 1 for PC/Ps2 Save or 2 for Xbox 360 Save.\nIf you select the wrong one, just run it again and choose the correct one: ")
        if version == "1":
            ChecksumCount(0, 1004, "little", 0)
        elif version == "2":
            ChecksumCount(0, 1004, "big", 0)
        else:
            finished = input("Invalid choice. Press enter to close")
            sys.exit()
    elif filesize == 1032:
        print("LSW2 Xbox Save File Detected")
        ChecksumCount(4, 1008, "little", 0)
    elif filesize == 8528:
        print("LSW2 GC Save File Detected")
        ChecksumCount(1996, 3000, "big", 0)
    elif filesize == 8256:
        print("LSW2 GC Save File Detected")
        ChecksumCount(1724, 2728, "big", 0)
    elif filesize == 1040:
        print("LSW2 PSP Save File Detected")
        ChecksumCount(4, 1036, "little", 0)

    # LSW1
    elif filesize == 532:
        print("LSW1 PC/Ps2/Ps2 Preview Save File Detected")
        ChecksumCount(0, 528, "little", 0)
    elif filesize == 58550:
        print("LSW1 Ps2 Save FIle Detected")
        ChecksumCount(58014, 58542, "little", 0)
    elif filesize == 24640:
        print("LSW1 GC Save FIle Detected")
        ChecksumCount(8852, 9380, "big", 0)
    elif filesize == 24912:
        print("LSW1 GC Save FIle Detected")
        ChecksumCount(1952, 2480, "big", 0)
    elif filesize == 57620:
        print("LSW1 Ps2 (Ps3 Format) Save File Detected")
        ChecksumCount(57088, 57616, "little", 0)

    # INVALID
    else:
        finished = input("This is not a valid save file. Press enter to close")
        sys.exit()

finished = input("\nChecksum of the save file has been updated. Press enter to close")
sys.exit()
