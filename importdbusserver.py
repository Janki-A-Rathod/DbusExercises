#!/usr/bin/env python3

import dbus
import dbus.service

from gi.repository import GLib
import dbus.mainloop.glib
#loop = GLib.MainLoop()
message_count = 0

class SomeObject(dbus.service.Object):
    @dbus.service.method("org.example.demo.test",
                         in_signature='', out_signature='')
    def server_no_args(self):
        "No arguments over the dbus. Server produces a message on the console."
        global message_count
        print("This is message {}".format(message_count))
        message_count +=1
        return
        
if __name__ == '__main__':
    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
    bus = dbus.SessionBus()
    name = dbus.service.BusName("org.example.demo.test", bus)
    object = SomeObject(bus, '/org/example/demo/test')
    mainloop = GLib.MainLoop()
    print("Running example service.")
    mainloop.run()
