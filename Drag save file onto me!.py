import sys
import os
import numpy as np

np.seterr(all='ignore')  # stops overflow warning message from occuring

try:
    savefile = sys.argv[1]  # makes the file you drop on the script the save file in question
except IndexError:
    finished = input("No file dropped! Please drop the save file you want to update the checksum of\nPress enter to close")
    sys.exit()  # quits if file is not dropped on the script

filesize = os.path.getsize(savefile)

decfile = []

with open(savefile, 'r+b') as file:  # opens file as raw binary
    def ChecksumCount(start, stop, order, oldchecksumloc):
        checksum = 6031769
        file.seek(start)
        for a in range(0, stop):
            fileread = file.read(4)
            decfile.append(int.from_bytes(fileread, byteorder=order, signed=False))  # adds all the bytes in groups of 4 to the list
        for a in range(0, len(decfile) - 1):  # adds up all the groups of 4 bytes together
            checksum = np.uint32(decfile[a]) + np.uint32(checksum)
        oldchecksum = int.from_bytes(fileread, byteorder=order, signed=False)
        if checksum == oldchecksum:
            finished = input("New checksum already matches the existing one. Press enter to close")
            sys.exit()
        print("\nOld Checksum: " + str(oldchecksum))
        print("\nNew Checksum: " + str(checksum))
        file.seek(oldchecksumloc)
        file.write(int(checksum).to_bytes(4, byteorder=order))


    if filesize == 131072:
        print("Wii Save File Detected")
        ChecksumCount(60, 8084, "big", 32392)
    elif filesize == 32360:
        print("Xbox 360 Save File Detected")
        ChecksumCount(0, 8090, "big", 32356)
    elif filesize == 32336:
        print("Ps3 Save File Detected")
        ChecksumCount(0, 8084, "big", 32332)
    elif filesize == 40572:
        print("PC Save File Detected")
        ChecksumCount(8232, 8084, "little", 40564)
    else:
        finished = input("This is not a valid save file. Press enter to close")
        sys.exit()

finished = input("\nChecksum of the save file has been updated. Press enter to close")
sys.exit()