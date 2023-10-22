#!/usr/bin/env python3
import serial
import time
import sys, getopt

#ser = serial.Serial('COM3', 9600, timeout=1)
ser = serial.Serial()
ser.baudrate = 9600
ser.timeout = 1
#ser.reset_input_buffer()

def interactiveMode():
    while True:
        value = input("Please enter 1-8: ")
        doSwitch(value)
        line = ser.readline().decode('utf-8').rstrip()
        print(line)

def manualMode(switchNum):
    doSwitch(switchNum)

def doSwitch(value):
    ser.reset_output_buffer()
    ser.reset_input_buffer()
    cmd = b"btn6\n"
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
            print ("do this")
            cmd = b"btn7\n"
        case "8":
            print ("blarg")
            cmd = b"btn8\n"
        case _:
            cmd = b"btn6\n"
    ser.write(cmd)

def main(argv):
    port = 'COM3'
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

    ser.port = port
    ser.open()
    ser.reset_input_buffer()
    if switchNum:
        time.sleep(2) # 2 second sleep because the arduino resets
        doSwitch(switchNum)
    else:
        #print ('interactive')
        interactiveMode()
    
    print ('port is ', port)
    print ('switch is ', switchNum)
    

    ser.close()
    sys.exit()

if __name__ == '__main__':
    main(sys.argv[1:])


