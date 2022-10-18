#!/bin/python

import os
import time
loop = True

# Loop until file is created by KDE Plasma
while loop:
  existence = os.path.exists("/root/.config/plasma-org.kde.plasma.desktop-appletsrc")
  if existence:
      os.system("/root/.wallpaper/changewall.py")
      loop = False
  time.sleep(.25)
