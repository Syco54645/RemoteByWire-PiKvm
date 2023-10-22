#
# Console Application Daemon to communicate with IrEmulator
# Copyright (C) 2023 Syco54645
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

#!/usr/bin/env python3
import serial
import time
import sys, getopt
import zmq
import signal

signal.signal(signal.SIGINT, signal.SIG_DFL); # allow ctrl-c to kill the app

ser = serial.Serial()
ser.baudrate = 9600
ser.timeout = 1

context = zmq.Context()
socket = context.socket(zmq.REP)

def interactiveMode():
    while True:
        value = input("Please enter 1-8: ")
        doSwitch(value)
        #line = ser.readline().decode('utf-8').rstrip()
        #print(line)

def daemonMode(port, serialPort):
    print(f"Daemon Started on tcp://*:%s. Waiting for command..." % port)
    print(f"Serial Port connected on %s. Ready to send command...\n" % serialPort)
    print("ctrl-c to exit\n")
    while True:
        message = socket.recv()
        print(">>> [%s]" % message)
        doSwitch(message)
        socket.send(b"done %s" % message)

def doSwitch(value):
    ser.reset_output_buffer()
    ser.reset_input_buffer()
    cmd = b"btn1\n"
    if isinstance(value, (bytes, bytearray)):
        cmd = value
    else:
        match value:
            case "1" | 1:
                cmd = b"btn1\n"
            case "2" | 2:
                cmd = b"btn2\n"
            case "3" | 3:
                cmd = b"btn3\n"
            case "4" | 4:
                cmd = b"btn4\n"
            case "5" | 5:
                cmd = b"btn5\n"
            case "6" | 6:
                cmd = b"btn6\n"
            case "7" | 7:
                cmd = b"btn7\n"
            case "8" | 8:
                cmd = b"btn8\n"
            case _:
                cmd = b"btn1\n"
    ser.write(cmd)
    line = ser.readline().decode('utf-8').rstrip()
    print(">>> [%s]" % line)

def main(argv):
    serialPort = 'COM3'
    port = "5555"
    mode = "daemon"
    opts, args = getopt.getopt(argv,"his:p:",["help","interactive","serial=","port="])

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print ('pyRemoteByWireDaemon.py -p <port> -s <number>\n')
            print ('-h, --help \t Shows this help screen.')
            print ('-s, --serial \t The serial port for daemon/arduino communication.')
            print ('-p, --port \t The web port for the daemon. Default is 5555.')
            print ('-i, --interactive \t Interactive mode bypasses the need of sendCmd. Good for debugging.')
            sys.exit()
        if opt in ("-s", "--serial"):
            serialPort = arg
        if opt in ("-p", "--port"):
            port = arg
        if opt in ("-i", "--interactive"):
            mode = "interactive"

    socket.bind(f"tcp://*:%s" % port)
    ser.port = serialPort
    ser.open()
    ser.reset_input_buffer()
    
    if mode == "interactive":
        interactiveMode()
    else:
        daemonMode(port, serialPort)

    ser.close()
    sys.exit()

if __name__ == '__main__':
    main(sys.argv[1:])