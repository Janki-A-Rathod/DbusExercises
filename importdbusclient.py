#!/usr/bin/env python3

import dbus
from gi.repository import GLib
mainloop = GLib.MainLoop()
INTERVAL=2
def main():
    bus = dbus.SessionBus()
    remote_object = bus.get_object("org.example.demo.test",
                                       "/org/example/demo/test")
    print("Sending Method Call: server_no_args")
    reply = remote_object.server_no_args()
    return True

if __name__ == '__main__':
    print("Running client....")
    GLib.timeout_add_seconds(interval=INTERVAL, 
                             function=main)
    mainloop.run()