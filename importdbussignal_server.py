#!/usr/bin/env python3

import dbus
import dbus.service

from gi.repository import GLib
import dbus.mainloop.glib
import random
INTERVAL = 2
import os

class SomeObject(dbus.service.Object):

    @dbus.service.signal(dbus_interface='org.example.demo.test',
                         signature='as')
    def ListAllFiles(self, i):
        pass
        #print("Inside integer_signal",i)
    @dbus.service.method("org.example.demo.test",
                         in_signature='s', out_signature='s')
    def DeleteFileGivenByClient(self, input_string):
        # os.chdir('/home/janki/Desktop/pythondbus')
        if os.path.exists(input_string):
            os.remove(input_string)
            send_to_client = "File Deleted"
        else:
            # file not found message
            print("File not found in the directory")
            send_to_client = "File Not Found"
        return send_to_client
    @dbus.service.method("org.example.demo.test",
                         in_signature= 'ays')   
    def UploadGivenFile(self, name, file_name):
        #print(name)
        #print(file_name)
        os.chdir('/home/janki/Desktop')
        if os.path.exists(file_name):
            print("file available")
        else:
            print("uploading file ....")
            converted_file = open(file_name, 'x')
            converted_file.write(name)
            converted_file.close()
        return

def send():
    path = "/home/janki/Desktop/pythondbus"
    dir_list = os.listdir(path)
    #print("Files and directories in '", path, "' :")
    #print(dir_list)
    object.ListAllFiles(dir_list)
    return True


if __name__ == '__main__':
    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
    bus = dbus.SessionBus()
    name = dbus.service.BusName("org.example.demo.test", bus)
    object = SomeObject(bus, '/org/example/demo/test')
    GLib.timeout_add_seconds(interval=INTERVAL, function=send)
    mainloop = GLib.MainLoop()
    print("Running example service.")
    mainloop.run()