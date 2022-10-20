#!/usr/bin/env bash
# shellcheck disable=SC2034

iso_name="BossOS"
iso_label="BossOS_$(date +%Y%m)"
iso_publisher="Chicken in a Can <https://github.com/Chicken-in-a-Can/the-executive-os>"
iso_application="BossOS Live USB"
iso_version="$(date +%Y.%m.%d)"
install_dir="arch"
buildmodes=('iso')
bootmodes=('bios.syslinux.mbr' 'bios.syslinux.eltorito'
           'uefi-ia32.grub.esp' 'uefi-x64.grub.esp'
           'uefi-ia32.grub.eltorito' 'uefi-x64.grub.eltorito')
arch="x86_64"
pacman_conf="pacman.conf"
airootfs_image_type="squashfs"
airootfs_image_tool_options=('-comp' 'xz' '-Xbcj' 'x86' '-b' '1M' '-Xdict-size' '1M')
file_permissions=(
  ["/etc/shadow"]="0:0:400"
  ["/root"]="0:0:750"
  ["/root/.automated_script.sh"]="0:0:755"
  ["/usr/local/bin/choose-mirror"]="0:0:755"
  ["/usr/local/bin/Installation_guide"]="0:0:755"
  ["/usr/local/bin/livecd-sound"]="0:0:755"
  ["/root/.setup"]="0:0:755"
  ["/root/Desktop/konsole.desktop"]="0:0:755"
  ["/root/.wallpaper/defaultwall.py"]="0:0:755"
  ["/root/.wallpaper/wallchange.py"]="0:0:755"
  ["/root/.wallpaper/wallwait.sh"]="0:0:755"
)
