import opc
import time
from patterns import *
from math import *

fc = opc.Client("127.0.0.1:7890")

def show():
    initTime = time.time()
    while(time.time() < initTime + 60):
        chase(fc)

    initTime = time.time()
    while(time.time() < initTime + 120):
        stack(fc)

    initTime = time.time()
    while(time.time() < initTime + 180):
        twinkle(fc)

    initTime = time.time()
    while(time.time() < initTime + 120):
        bacon_static(fc)
        time.sleep(1)
        bacon_static_inverse(fc)
        time.sleep(1)

if fc.can_connect():
    print "Connected"
else:
    print "Not Connected"

initTime = time.time()
while(time.time() < initTime + 30):
    colorwheel(fc)

while(True):
    show()
