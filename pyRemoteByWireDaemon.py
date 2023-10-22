#!/usr/bin/env python3
import serial
import time
import sys, getopt
import zmq

ser = serial.Serial()
ser.baudrate = 9600
ser.timeout = 1

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

def interactiveMode():
    while True:
        value = input("Please enter 1-8: ")
        doSwitch(value)
        #line = ser.readline().decode('utf-8').rstrip()
        #print(line)

def daemonMode():
    print("Daemon Started. Waiting for command...")
    while True:
        message = socket.recv()
        print("Received: %s" % message)
        #time.sleep(2)
        doSwitch(message)
        socket.send(b"done %s" % message)

def doSwitch(value):
    ser.reset_output_buffer()
    ser.reset_input_buffer()
    print (type(value))
    print ("value is %s" % value)
    print (type("1"))
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
    print(line)

def main(argv):
    port = 'COM3'
    mode = "daemon"
    opts, args = getopt.getopt(argv,"hip:",["interactive","port"])

    for opt, arg in opts:
        if opt == '-h':
            print ('test.py -p <port> -s <number>')
            sys.exit()
        if opt in ("-p", "--port"):
            port = arg
        if opt in ("-i", "--interactive"):
            mode = "interactive"
       
    ser.port = port
    ser.open()
    ser.reset_input_buffer()
    
    if mode == "interactive":
        interactiveMode()
    else:
        daemonMode()

    ser.close()
    sys.exit()

if __name__ == '__main__':
    main(sys.argv[1:])