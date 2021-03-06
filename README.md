# py-serial-test
Tx/Rx test tool for transmitting signal from system under test serial port to modem continuously.

## Environment
Language: Python 3.7

### Supported operating system
* Ubuntu 18.04
* Manjaro 18.04
* windows server 2012R2
* windows server 2016

## Compilation
`gcc` and `make` is needed if `pip install patchelf-wrapper` occurs error

## Installation
### Use the package manager pip to install pyserial.

`sudo pip install -r Requirement.txt`

### Use the Linux package manager software to install tkinter.

**Debian**  `sudo apt-get install python3-tk`

**Arch** `sudo pacman -S tk`

## Execution
### Text mode
    sudo python main.py

### GUI mode
    sudo python mainui.py

## Image
### Text mode
![](./images/text_sel.png)

![](./images/text_test.png)

![](./images/text_result.png)
### GUI mode
![](./images/start.png)
![](./images/select.png)
![](./images/failed.png)
![](./images/pass.png)
