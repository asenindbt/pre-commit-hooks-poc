#!/usr/bin/env python
import os
import sys

HERE = os.path.dirname(os.path.realpath(__file__))


def main():
    # cfg = os.path.join(HERE, 'orghooks.yaml')

    # cmd = ['pre-commit', 'run']
    # cmd = ['pre-commit', 'run', '--config', cfg, '--files'] + sys.argv[1:]
    # os.execvp(cmd[0], cmd)
    os.system('pre-commit run')


if __name__ == '__main__':
    exit(main())