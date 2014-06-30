#!/usr/bin/env python3

class FakeSerial():

    def __init__(self, prompt='Unknown'):
        self.prompt = prompt

    def send_command(self, command):
        print('{prompt}: {command}'.format(prompt=self.prompt, command=command))

if __name__ == '__main__':
    fake = FakeSerial('TOTO')
    fake.send_command('Salut')

