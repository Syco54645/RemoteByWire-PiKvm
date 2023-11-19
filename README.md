


# RemoteByWire-PiKvm
This project allows the control of an AIMOS 8 Port KVM via the PiKvm system. This was accomplished by replacing the IR receiver with an Arduino. In theory, this should work for other multi-port KVMs with an IR remote.

## Why Bother?
PiKVM is a fantastic project, the only issue is that it is single port only. This can be worked around by plugging in a multi-port KVM. There are a few plug and play options available but they were cost prohibitive. The AIMOS KVM will work but has a few shortcomings. First, it must be controlled by hotkeys. While this is not horrible, to use this method of control you must plug the USB into the keyboard port of the KVM. Doing this will break the USB mass storage emulation. To be fair, there is a workaround for the mass storage issue but it requires a second Raspberry Pi. This system allows direct control of the AIMOS KVM with a simple terminal script.

### Usage
This project consists of three parts.

 - [IrEmulator.ino](https://github.com/Syco54645/RemoteByWire-PiKvm/blob/main/IrEmulator/IrEmulator.ino) - Arduino software to perform the switching of inputs on the AIMOS KVM.
 - [pyRemoteByWireDaemon.py](https://github.com/Syco54645/RemoteByWire-PiKvm/blob/main/pyRemoteByWireDaemon.py "pyRemoteByWireDaemon.py") - Python script that connects to the Arduino via serial. It waits for a command to be sent to it from the [sendCmd.py](https://github.com/Syco54645/RemoteByWire-PiKvm/blob/main/sendCmd.py "sendCmd.py") script
 - [sendCmd.py](https://github.com/Syco54645/RemoteByWire-PiKvm/blob/main/sendCmd.py "sendCmd.py") - Python script to send commands to [pyRemoteByWireDaemon.py](https://github.com/Syco54645/RemoteByWire-PiKvm/blob/main/pyRemoteByWireDaemon.py "pyRemoteByWireDaemon.py")

#### [IrEmulator.ino](https://github.com/Syco54645/RemoteByWire-PiKvm/blob/main/IrEmulator/IrEmulator.ino)
Flash this to your Arduino. Theroritically this file could be modified to send different signals and work for other KVMs.

#### [pyRemoteByWireDaemon.py](https://github.com/Syco54645/RemoteByWire-PiKvm/blob/main/pyRemoteByWireDaemon.py "pyRemoteByWireDaemon.py")
`python pyRemoteByWireDaemon.py -s <USB SERIAL> -p 5555`

#### [sendCmd.py](https://github.com/Syco54645/RemoteByWire-PiKvm/blob/main/sendCmd.py "sendCmd.py")
`python sendCmd.py -p 5555 -s <KVM PORT NUMBER> `

### Skills
Basic soldering skills are a must. The most dangerous part is removing the IR receiver. the rest should just be simple soldering.

### BOM
 - PiKVM
 - Aimos 8 port KVM
 - Arduino Nano
 - Logic Level Converter

### Building
This project is relatively simple to build
 1. Disassemble the AIMOS KVM and remove the IR receiver

### Circuit
Below is a diagram of the circuit. The purple and black output wires connect to the AIMOS board, the purple goes where the output of the IR receiver was and the black goes to ground.
![RemoteByWire-PiKvm Circuit](https://raw.githubusercontent.com/Syco54645/RemoteByWire-PiKvm/main/RemoteByWire-PiKvm_bb.png)

### Pi Setup
 - rw
 - pacman -S python-pip
 - pacman -S python-pyzmq
 - ls /dev/serial/by-id/

### /etc/kvmd/override.yaml
```
    kvmd:
        ...
        gpio:
            drivers:
                btn1:
                    type: cmd
                    cmd: [/usr/bin/python, /usr/local/bin/sendCmd.py, -s, 1]
                btn2:
                    type: cmd
                    cmd: [/usr/bin/python, /usr/local/bin/sendCmd.py, -s, 2]
                btn3:
                    type: cmd
                    cmd: [/usr/bin/python, /usr/local/bin/sendCmd.py, -s, 3]
                btn4:
                    type: cmd
                    cmd: [/usr/bin/python, /usr/local/bin/sendCmd.py, -s, 4]
                btn5:
                    type: cmd
                    cmd: [/usr/bin/python, /usr/local/bin/sendCmd.py, -s, 5]
                btn6:
                    type: cmd
                    cmd: [/usr/bin/python, /usr/local/bin/sendCmd.py, -s, 6]
                btn7:
                    type: cmd
                    cmd: [/usr/bin/python, /usr/local/bin/sendCmd.py, -s, 7]
                btn8:
                    type: cmd
                    cmd: [/usr/bin/python, /usr/local/bin/sendCmd.py, -s, 8]
            scheme:
                btn1_button:
                    driver: btn1
                    pin: 0
                    mode: output
                    switch: false
                btn2_button:
                    driver: btn2
                    pin: 0
                    mode: output
                    switch: false
                btn3_button:
                    driver: btn3
                    pin: 0
                    mode: output
                    switch: false
                btn4_button:
                    driver: btn4
                    pin: 0
                    mode: output
                    switch: false
                btn5_button:
                    driver: btn5
                    pin: 0
                    mode: output
                    switch: false
                btn6_button:
                    driver: btn6
                    pin: 0
                    mode: output
                    switch: false
                btn7_button:
                    driver: btn7
                    pin: 0
                    mode: output
                    switch: false
                btn8_button:
                    driver: btn8
                    pin: 0
                    mode: output
                    switch: false
            view:
                header:
                    title: KVM Control
                table:
                     - ["btn1_button|Port 1"]
                     - ["btn2_button|Port 2"]
                     - ["btn3_button|Port 3"]
                     - ["btn4_button|Port 4"]
                     - ["btn5_button|Port 5"]
                     - ["btn6_button|Port 6"]
                     - ["btn7_button|Port 7"]
                     - ["btn8_button|Port 8"]
```
