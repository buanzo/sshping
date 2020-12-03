#!/usr/bin/env python3
# Author: Arturo 'Buanzo' Busleiman - October 2020
import argparse
import sys
from os.path import expanduser

from pythonping import ping
from sshconf import read_ssh_config

__version__ = '0.1.2'


class SSHPing:
    def __init__(self, target, count=None, verbose=False, timeout=10):
        config = read_ssh_config(expanduser("~/.ssh/config"))
        try:
            self.target = config.host(target)['hostname']
        except KeyError:
            self.target = target
        self.count = count
        self.verbose = verbose
        self.timeout = timeout

    def ping(self):
        try:
            if self.count is not None:  # FIX: I need to use **kwargs
                ping(self.target, timeout=self.timeout, verbose=self.verbose, count=self.count)
            else:
                ping(self.target, timeout=self.timeout, verbose=self.verbose)
        except PermissionError:
            print('Privileges required: setuid the script, or uso sudo. RAW capability required to send ping.')


def run():
    parser = argparse.ArgumentParser(description='''Simple command line tool that lets you ping hosts that are only defined in your ssh config''')
    parser.add_argument('target')
    args = parser.parse_args()
    # instantiation goes here
    sshping = SSHPing(target=sys.argv[1], verbose=True)
    sshping.ping()


if __name__ == '__main__':
    run()
