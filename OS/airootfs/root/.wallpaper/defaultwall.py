#!/bin/python

import os
import time

loop = True

# Loop until file is created by KDE Plasma
while loop:
  existence = os.path.exists("/root/.config/plasma-org.kde.plasma.desktop-appletsrc")
  if existence:
    # Pull file in and read lines to array 
    f = open("/root/.config/plasma-org.kde.plasma.desktop-appletsrc")
    lines=f.readlines()
    f.close()
    # Parse lines to find which has Image on it, replace line
    for i in range(len(lines)):
      if lines[i][0:5] == "Image":
        lines[i] = "Image=file:///root/.wallpaper/barn_01.jpg\n"
    # Write back to file
    f=open("/root/.config/plasma-org.kde.plasma.desktop-appletsrc", "w")
    f.writelines(lines)
    f.close()
    # End loop
    loop = False
  else:
    # Delay after each check to reduce load on system
    time.sleep(.25)
