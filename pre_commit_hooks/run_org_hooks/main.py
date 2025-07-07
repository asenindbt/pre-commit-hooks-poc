#!/usr/bin/env python
import os
import sys

HERE = os.path.dirname(os.path.realpath(__file__))


def main():
    cmd = ['pre-commit', 'run', '--files'] + sys.argv[1:]
    os.execvp(cmd[0], cmd)


if __name__ == '__main__':
    exit(main())