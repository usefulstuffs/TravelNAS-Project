# The TravelNAS Project
Create a Portable NAS with a Raspberry Pi 4

## 1. Hardware
You need the following:
- Raspberry Pi 4 (model B 4GB RAM is used here)
- Wi-Fi dongle
- MicroSD with at least 16 GB
- Internet connection

## 2. Getting started
1. Download the [Raspberry Pi Imager](https://www.raspberrypi.com/software/)
2. Install and open it
3. Select your Raspberry Pi model
4. Use "Raspberry Pi OS Lite (64 bits)" as the operating system
5. Now select your MicroSD and hit the button to start writing the image
6. You may want to customize the settings for the operating system, like enabling SSH and creating an account, setting up the keyboard layout, etc
7. Wait for it to write and when asked for, remove the MicroSD from your PC and put it in the Raspi
8. Turn on Raspberry Pi by plugging it in
9. Log in with your credentials
10. Connect to the internet via ethernet or USB WI-FI DONGLE (IMPORTANT!! Internal Wi-Fi is going to be used as hotspot!!)

## 3. Setting up Wi-Fi hotspot
Follow [this guide](https://www.raspberrypi.com/tutorials/host-a-hotel-wifi-hotspot/). For the app.py file, use the one in this repository.

## 4. Setting up the NAS Software
As NAS Software, I used [CasaOS](https://casaos.io). You can install it with a command:
```bash
curl -fsSL https://get.casaos.io | sudo bash
```
After this, connect your PC or phone to the Wi-Fi hotspot created by your raspberry. Visit then its IP (in my case 10.42.0.1) and set up CasaOS. Visit 10.42.0.1:4000 to set-up wifi (you may want to add a shortcut to CasaOS's home to that).

## 5. Turn off Raspberry Pi lights (OPTIONAL)
Raspberry Pi lights may be annoying. If you are in that case, you can easly turn them off by editing one file.

1. Type ``sudo nano /boot/firmware/config.txt``
2. Append this code at the end of the file:
```
dtparam=pwr_led_activelow=off
dtparam=act_led_trigger=none
dtparam=act_led_activelow=off
dtparam=eth_led0=14
dtparam=eth_led1=14
```
3. Reboot the Raspberry Pi

More info at [this link](https://raspberrytips.com/disable-leds-on-raspberry-pi/)

## Credits
- Raspberry Pi Foundation: article for hotspot
- CasaOS: NAS software used in this project
- Raspberry Tips: turning off leds

##### Copyright (C) 2024 Useful Stuffs
