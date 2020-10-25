#!/usr/bin/env python3
# Author: Arturo 'Buanzo' Busleiman - October 2020
import sys
import argparse
from sshconf import read_ssh_config
from os.path import expanduser
from pythonping import ping
from pprint import pprint

__version__ = '0.1'

class SSHPing():
    def __init__(self, target=None, count=None, verbose=False, timeout=10):
        if target is None:
            return(ValueError('No target argument provided'))
        else:
            c = read_ssh_config(expanduser("~/.ssh/config"))
            try:
                self.target = c.host(target)['hostname']
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
    # argumentparsing goes here
    # instantiation goes here
    sshping = SSHPing(target=sys.argv[1], verbose=True)
    sshping.ping()
    
if __name__ == '__main__':
    run()
