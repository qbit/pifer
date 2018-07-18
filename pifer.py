#!/usr/bin/env python

import asyncio
import pigpio
import time
import websockets

port = 8000
pi = pigpio.pi()

if not pi.connected:
    exit(0)

sensor = pi.spi_open(0, 1000000, 0)

@asyncio.coroutine
def read_temp(websocket, path):
    while True:
	# http://abyz.me.uk/rpi/pigpio/examples.html#Python_MAX6675_py
        c, d = pi.spi_read(sensor, 2)
        if c == 2:
            word = (d[0]<<8) | d[1]
            if (word & 0x8006) == 0: # Bits 15, 2, and 1 should be zero.
                t = (word >> 3)/4.0
                yield from websocket.send("{:.2f}".format(t))
                print(("{:.2f}".format(t)))
            else:
                yield from websocket.send("bad reading {:b}".format(word))
                print(("bad reading {:b}".format(word)))
        time.sleep(0.5)

start_server = websockets.serve(read_temp, '0.0.0.0', 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

pi.spi_close(sensor)

pi.stop()

