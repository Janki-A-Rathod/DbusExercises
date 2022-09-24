#!/usr/bin/env python3

#from ast import arg
import signal
import dbus.mainloop.glib
from gi.repository import GLib
import dbus
from dbus.mainloop.glib import DBusGMainLoop
DBusGMainLoop(set_as_default=True)
INTERVAL = 2
bus = dbus.SessionBus()
mainloop = GLib.MainLoop()
import threading
import os
x = []
import threading as th
S = th.Timer(0, None)

def handler(signum, frame):
    print("Ctrl-c was pressed")
    os._exit(1)

def uploadfileintoServer():
    #print(os.getcwd())
    arg = (input("Which file you want to upload: "))
    os.chdir(os.getcwd())
    if os.path.exists(arg):
        # print(os.path)
        print("File Exist......")
        try:
            with open(arg, "rb") as f:
                getbyte = f.read()
                reply = remote_object.UploadGivenFile(getbyte, arg)
        except:
            print("It is not file")
    else:
        print("File Not Exist")
    return True

def cb_signal_emission(arg):
    "Callback on emitting signal, a random integer, from server. "
    #random_number = args[4][0]
    #print("Client received : {}".format(arg))
    def sctn():
        print("Server is OFF\n")
        os._exit(1)

    global S
    S.cancel()
    S = th.Timer(3.0, sctn)
    S.start()
    global x
    x = arg

def deletefile():
    arg = (input("Which file you want to delete: "))
    reply = remote_object.DeleteFileGivenByClient(arg)
    print("Sended From Server_:{}".format(reply))
    return True

def GetListofFiles():
    global x
    print(x)

def menu():
    print("File Transfer System")
    while (1):
        print(
            "1.Delete File\n2.Upload File\n3.File Info\n4.Download File\n5.List All Files")
        try:
            option = int(input('Enter your choice: '))
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
            continue

        if option == 1:
            print(f"Handle option \'Option 1\'")
            deletefile()
        elif option == 2:
            print('Handle option \'Option 2\'')
            uploadfileintoServer()
        elif option == 3:
            print('Handle option \'Option 3\'')
            #Getfileinfofromserver()
        elif option == 4:
            print('Handle option \'Option 4\'')
            # DownloadfileGivenByServer()
        elif option == 5:
            print('Handle option \'Option 5\'')
            GetListofFiles()
        else:
            print("\nChoose right option")


if __name__ == "__main__":
    print("Running client....")
    signal.signal(signal.SIGINT, handler)
    signal.signal(signal.SIGABRT, handler)
    bus = dbus.SessionBus()
    remote_object = bus.get_object("org.example.demo.test",
                                   "/org/example/demo/test")
    remote_object.connect_to_signal(
        "ListAllFiles", handler_function=cb_signal_emission, dbus_interface="org.example.demo.test")
    t1 = threading.Thread(target=menu)
    t1.start()
    mainloop.run()
