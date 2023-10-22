#
# Console Application to communicate with pyRemoteByWireDaemon
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
import time
import sys, getopt
import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)

def interactiveMode():
    while True:
        value = input("Please enter 1-8: ")
        doSwitch(value)
        #line = ser.readline().decode('utf-8').rstrip()
        #print(line)

def doSwitch(value):
    cmd = b"btn6\n"
    print (type(value))
    match value:
        case "1":
            cmd = b"btn1\n"
        case "2":
            cmd = b"btn2\n"
        case "3":
            cmd = b"btn3\n"
        case "4":
            cmd = b"btn4\n"
        case "5":
            cmd = b"btn5\n"
        case "6":
            cmd = b"btn6\n"
        case "7":
            cmd = b"btn7\n"
        case "8":
            cmd = b"btn8\n"
        case _:
            cmd = b"btn6\n"

    socket.send(cmd)
    message = socket.recv()
    print("Received reply [ %s ]" % (message))

def main(argv):
    port = '5555'
    switchNum = ''
    opts, args = getopt.getopt(argv,"his:p:",["interactive","switch","port"])

    for opt, arg in opts:
        if opt == '-h':
            print ('test.py -p <port> -s <number>')
            sys.exit()
        if opt in ("-p", "--port"):
            port = arg
        if opt in ("-s", "--switch"):
            mode = "switch"
            switchNum = arg

    socket.connect("tcp://localhost:5555")

    if switchNum:
        doSwitch(switchNum.replace("btn", ""))
    else:
        #print ('interactive')
        interactiveMode()
    
    print ('port is ', port)
    print ('switch is ', switchNum)

    sys.exit()

if __name__ == '__main__':
    main(sys.argv[1:])


