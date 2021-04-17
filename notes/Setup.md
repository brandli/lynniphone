# Setup
## Setup Raspberry Pi
* Follow [these steps](https://blog.jongallant.com/2017/11/raspberrypi-setup/) for Raspberry setup
  * Ignore hardware instructions
  * Use Raspbian with desktop and recommended software
  * Turn on VNC Server: Preferences -> Raspberry Pi Configuration -> Interfaces
  * Set the display resolution which is used when no screen is connected: 
    sudo raspi-config

## Dependencies (preliminary)
    sudo apt-get install espeak
    sudo apt-get install mplayer
    sudo apt-get install sox
    sudo apt-get install amsynth

## Configuration
    git clone https://github.com/brandli/lynniphone
    sudo cp lynniphone/config/boot/config.txt /boot/
    sudo cp lynniphone/config/etc/lynniphone.service /etc/systemd/system/lynniphone.service
    sudo chmod +x lynniphone/src/init/init.sh
    sudo systemctl daemon-reload
    sudo systemctl enable lynniphone
    cp lynniphone/config/home/.bashrc ./
    reboot
