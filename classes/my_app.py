#!/usr/bin/env python3

import commands
import fakeSerial
import trueSerial

s = fakeSerial.FakeSerial('Ultimate Fake')
t = trueSerial.TrueSerial('Great Truth')
mc = commands.MyCommands(s)

mc.send('First command')
s.prompt = 'Fake Pro'
mc.send('Second command')
mc.serial = t
mc.send('Third command')

