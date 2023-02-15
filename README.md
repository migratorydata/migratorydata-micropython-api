# MigratoryData MicroPython Client API

## Installing MicroPython on Pico W board

Download the latest MicroPython firmware (a <code>UF2</code> file) from [micropython](https://micropython.org/download/rp2-pico-w/). Use a USB to micro-USB cable to connect the Pico board to your computer. Hold down the BOOTSEL button of the Pico board while plugging the board into USB. An USB mass storage device will appear into the file explorer of your computer. Drag and drop the <code>UF2</code> MicroPython firmware file you downloaded into the USB mass storage device. Your Pico board will reboot and will start running the MicroPython firmware. More details about the installation can be found on [raspberrypi.com](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html).


## Programming the board with Thonny IDE

To write programs you can use Thonny IDE. Follow the instruction form [Thonny website](https://thonny.org/) on how to install the IDE on your OS. After the installation is completed, connect the Pico board to your computer and start the Thonny IDE. From the down right corner select the communicate port named `Micropython (Raspberry PI Pico)`.

Go to View menu and click on Files option to see your computer file system and Pico board file system.

## Wireless network configuration

Create a `config.py` file on the Pico board. To create the file, right click on Raspberry Pi Pico window from the left of the Thonny IDE and click on `New file`.

Set the name of the file `config.py` and copy the code bellow into the newly created file. Edit the file by providing your country code, as well as the network name (SSID) and password of your wireless network.

```python
country = "RO"
ssid = "ssid"
password = "password"
```

## Install MigratoryData MicroPython library

One way to install the MigratoryData MicroPython library is by using the `mip` package manager provided by the MicroPython firmware.

The `mip` package manager needs an Internet connection. Therefore, provided that you created the `config.py` file as detailed above, connect the Pico board to the Internet by copying and pasting the following code into Thonny shell window:

```bash
import network, rp2, config
rp2.country(config.country)
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(config.ssid, config.password)
while not wlan.isconnected() and wlan.status() >= 0: time.sleep(1)
print(wlan.ifconfig())
```

Finally, to install the MigratoryData MicroPython library, copy and paste the following code into Thonny shell window:

```bash
import mip  
mip.install("github:migratorydata/migratorydata-micropython-api/package.json")
```

This will install the MigratoryData MicroPython library into the folder `lib/migratorydata`.

Getting started tutorial can be found [here](https://migratorydata.com/docs/client-api/micropython/getting_started/) and the documentation for the API [here](https://migratorydata.com/docs/client-api/micropython/).