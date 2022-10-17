# cscOS
Arch-based distro. Senior year project  
Had the idea to create a distro that I could use for persistent storage for code so I could just keep a flash drive on me and in case
anything happened and I couldn't use my laptop, I could still code and keep my code across sessions. So the installer script will install cscOS as well as
create an `ext4` partition as the third partition on the drive, and it'll get mounted automatically on start. The 3rd partition is persistent across reboots. Based on the releng profile, built with archiso. I've also set up a [wiki](https://github.com/Chicken-in-a-Can/cscOS/wiki) for any cscOS-specific things, as well as a bit of info on what I'm doing, and how to do some of it if you want.  
Official Operating System of the [MHS Comp-Sci Club](https://secure.payk12.com/school/martinhs/787/3155/item/213063).

## Current features
 - Persistent partition mounted to `/root/persistent`
 - Custom configuration files for:
   - Neovim
   - Neofetch
 - Multiple programming languages & compilers installed:
   - GCC
   - JDK
   - Go
   - Python
   - NodeJS
 - Relatively easy to use with KDE, Firefox, Konsole, SDDM, and other additional software
 - Single arg support on build script to allow for last-minute package additions
 
## Build & install
 1. Run `./build`
   - You'll be prompted for sudo password. **Don't** run script with sudo or as root
 2. Run `./install`
   - You'll be prompted for sudo password. **Don't** run script with sudo or as root
 3. Boot to drive on laptop/desktop
 4. Multiple arg support for build script
 5. Arg support for install script
 6. Checks for install script to prevent potential bricking
 
## Build & installation dependencies
Most of these come pre-installed
 - `archiso`
 - `git`
 - `python >= 3.10`
 - `grep`
 - `dd`
 - `lsblk`
 - `sed`
 - **Arch Linux**
 
## Current to-do
 - Make it change wallpaper from default KDE to default cscOS not just when you open terminal
 - Occasionally /dev/sdc is mounted for live USB instead of /dev/sdc1, so mounting script fails
   - > sdc can be exchanged for any device, I just already have 2 drives in my laptop
   - Reboot to fix for now
   - I haven't seen this in a while though
 - Make it look good in general
 - Other minor appearance improvements
   - Probably custom Firefox appearance, not just that though
 - Any issues submitted
   - I'll find something to fix probably anyways

## Releases
Github doesn't let me put a release over 2GB, and KDE and Firefox are big, so use the build script I created  
Just run: `./build`  
Don't run with `sudo` or `doas`  
To install on a flash drive, run `./install`  
It may take a bit of time to build, ranging between 2 hours and just a few minutes depending on the PC.  

## Screenshots
Current cscOS desktop & terminal. It's kinda rough  
  
![cscOS-liveUSB](https://raw.githubusercontent.com/chicken-in-a-can/cscOS/master/Media/cscOS_001.png)
![cscOS-liveUSB](https://raw.githubusercontent.com/chicken-in-a-can/cscOS/master/Media/cscOS_002.png)
