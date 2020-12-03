#!/usr/bin/env python3
# Author: Arturo 'Buanzo' Busleiman - October 2020
import argparse
from os.path import expanduser

from pythonping import ping
from sshconf import read_ssh_config

__version__ = '0.1.2'


class SSHPing:
    def __init__(self, target, count=4, verbose=False, timeout=10):
        assert target is not None
        config = read_ssh_config(expanduser('~/.ssh/config'))
        try:
            self.target = config.host(target)['hostname']
        except KeyError:
            self.target = target
        self.count = count
        self.verbose = verbose
        self.timeout = timeout

    def ping(self):
        return ping(self.target, timeout=self.timeout, verbose=self.verbose, count=self.count)


def run():
    parser = argparse.ArgumentParser(description="""Simple command line tool that lets you ping hosts that are only defined in your ssh config""")
    parser.add_argument('target', metavar="HOST", help="Name of host to ping")
    parser.add_argument('-c', '--count', default=4, type=int, help="How many times to attempt the ping, 4 by default")
    parser.add_argument('-v', '--verbose', action='store_true', help="Be verbose")
    parsed = parser.parse_args()

    sshping = SSHPing(target=parsed.target, count=parsed.count, verbose=parsed.verbose)
    try:
        sshping.ping()
    except PermissionError:
        print("Privileges required: setuid the script, or use sudo. RAW capability required to send ping.")


if __name__ == '__main__':
    run()
