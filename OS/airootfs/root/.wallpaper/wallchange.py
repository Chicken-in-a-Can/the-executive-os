#!/usr/bin/env python3
import dbus
import os
from pathlib import Path
HOME = str(Path.home())
SCREEN_LOCK_CONFIG = HOME+"/.config/kscreenlockerrc"
def setwallpaper(filepath, plugin='org.kde.image'):
    jscript = """
    var allDesktops = desktops();
    print (allDesktops);
    for (i=0;i<allDesktops.length;i++) {
        d = allDesktops[i];
        d.wallpaperPlugin = "%s";
        d.currentConfigGroup = Array("Wallpaper", "%s", "General");
        d.writeConfig("Image", "file://%s")
    }
    """
    bus = dbus.SessionBus()
    plasma = dbus.Interface(bus.get_object(
        'org.kde.plasmashell', '/PlasmaShell'), dbus_interface='org.kde.PlasmaShell')
    plasma.evaluateScript(jscript % (plugin, plugin, filepath))

def set_lockscreen_wallpaper(filepath,plugin='org.kde.image'):
    if os.path.exists(SCREEN_LOCK_CONFIG):
        new_data=[]
        with open(SCREEN_LOCK_CONFIG, "r") as kscreenlockerrc:
            new_data = kscreenlockerrc.readlines()
            is_wallpaper_section=False
            for num,line in enumerate(new_data,1):
                if "[Greeter][Wallpaper]["+plugin+"][General]" in line:
                    is_wallpaper_section = True
                if "Image=" in line and is_wallpaper_section:
                    new_data[num-1] = "Image="+filepath+"\n"
                    break

        with open(SCREEN_LOCK_CONFIG, "w") as kscreenlockerrc:
            kscreenlockerrc.writelines(new_data)

setwallpaper("/root/.wallpaper/executive.jpg", plugin="org.kde.Plasma")
set_lockscreen_wallpaper("/root/.wallpaper/executive.jpg", plugin="org.kde.Plasma")
