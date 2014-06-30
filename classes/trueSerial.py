#!/usr/bin/env python3

class TrueSerial():

    def __init__(self, prompt='Unknown'):
        self.prompt = prompt

    def send_command(self, command):
        print('='*20)
        print('{prompt}: {command}'.format(prompt=self.prompt, command=command))
        print('='*20)

if __name__ == '__main__':
    t = TrueSerial('TOTO')
    t.send_command('Salut')

