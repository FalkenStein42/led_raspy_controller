import serial, struct
import time as t
from datetime import datetime
LED=50
s = serial.Serial('COM3', 57600)
MIN_TIME = 0.18

##### DEFAULT COLORS #####

red = [255,0,0]
blue = [0,255,0]
green = [0,0,255]
purple = [255,255,0]
uwu = [255,127,0]

##########################

def create_package(data):
    package = b''
    for item in data:
        package += struct.pack('B',item)
    return package


def send(data):
    s.write(create_package(data))

def color(ca):
    send(ca*LED)

def move(ti=1):
    #assert ti>MIN_TIME
    j=LED-1
    send([0,0,0]*LED)
    for i in range(0,LED):
        send([0,0,0]*i+[255-4*i,4*i,0]+[0,0,0]*(j-i))
        t.sleep(ti)
        
def alternate(ca,cb,ti=.5):
    assert ti>MIN_TIME
    send((ca*int(LED/2))+(cb*int(LED/2)))
    t.sleep(ti)
    send((cb*int(LED/2))+(ca*int(LED/2)))
    t.sleep(ti)

def alternate_2(ca,cb,ti=.5):
    assert ti>MIN_TIME
    send((ca+cb)*int(LED/2))
    t.sleep(ti)
    send((cb+ca)*int(LED/2))
    t.sleep(ti)

def change(ca,cb,ti=.4):
    assert ti>MIN_TIME
    color(ca)
    t.sleep(ti)
    color(cb)
    t.sleep(ti)

def off():
    color([0,0,0])

def alarm(atime,checktime=5):
    #assert type(atime) is datetime
    while True:
        if int(datetime.now().timestamp()) in range(int(atime.timestamp())-checktime*2,int(atime.timestamp())+checktime*2):
            while True:
                change([255,255,255],[0,0,0],ti=1.25)
        else:
            t.sleep(checktime-.25)


################## EXECUTION ##############3

color(purple)


