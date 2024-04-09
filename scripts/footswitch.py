#!/usr/bin/env python3

import hid
import threading
import time

import rclpy
from rclpy.node import Node

from std_msgs.msg import Bool

SHUTDOWN = False
STATE = False
VENDOR_ID = 1523 # VEC infinity pedal hid.enumerate()
PRODUCT_ID = 255 # VEC infinity pedal

def update_hid():
    global STATE
    global SHUTDOWN
    while not SHUTDOWN:
        # out = hid.Device(VENDOR_ID, PRODUCT_ID).read(64) # string, should be something like b'\x00\x00'
        try:
            out = int.from_bytes(hid.Device(VENDOR_ID, PRODUCT_ID).read(64), byteorder='little') # https://www.tutorialspoint.com/how-to-convert-bytes-to-int-in-python
        except:
            out = 0
        if out != 0:
            STATE = True
        else:
            STATE = False

        # shutdown
        if SHUTDOWN:
            break
        # print(out)
        time.sleep(0.01) # go fast so that events aren't missed



class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('simple_footswitch')
        self.publisher_ = self.create_publisher(Bool, 'footswitch/triggered', 10)
        timer_period = 0.1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = Bool()
        msg.data = STATE
        self.publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    # make the hid thread
    x = threading.Thread(target=update_hid)
    x.daemon = True
    x.start()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()

    SHUTDOWN = True
    # x.join()

if __name__ == '__main__':
    main()


