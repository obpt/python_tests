#!/usr/bin/env python3

class MyCommands:

    def __init__(self, serial):
        self.serial = serial

    def send(self, cmd):
        self.serial.send_command(cmd)

if __name__ == '__main__':
    import fakeSerial

    s = fakeSerial.FakeSerial()

    mc = MyCommands(s)

    mc.send('Salut')

