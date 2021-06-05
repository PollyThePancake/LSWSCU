# LSWSCU

The LSWSCU (Lego Star Wars Save Checksum Updater) is a tool used for updating the checksums in save files that the games use to validate the file, incase it has been modified or corrupted.  

## What is a checksum?
A checksum is a small bit of data derived from some other data, as a means of verifying the datas integrity. In this case, it is a 4 byte wide value that is the unsigned sum of every 4 bytes in the save file starting from a certain offset up until the existing checksum, and any overflow that happens is kept. In some save files the calculation is salted at the beginning, meaning that the count starts at a value other than 0

## What can I use it on?

At the moment, there is only support for the following formats

### LEGO Star Wars: The Complete Sage
- PC
- PS3
- Xbox 360
- Wii

### LEGO Star Wars II: The Original Trilogy
- PC
- PS3 (Backwards compatability & emulation)
- PS2
- PS2 13/6/2006 Print Preview
- PSP
- Xbox 360
- Xbox
- GameCube

### LEGO Star Wars: The Video Game 
- PC
- PS3 (Backwards compatability & emulation)
- PS2
- PS2 10/1/2005 Print Preview
- Xbox
- GameCube

## How to use?
Simply drag your save onto the "Drag save file onto me!" python script (python required) or .exe file. This will generate a new checksum for the save file, which will pass the checksum check that the game will perform when loading a save file, allowing you to use it. ALWAYS MAKE BACKUPS OF YOUR SAVE FILES. I AM NOT RESPONSIBLE FOR WHAT HAPPENS TO THEM

## Finding your save files?
Documentation Pending
