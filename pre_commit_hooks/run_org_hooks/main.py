#!/usr/bin/env python
import os
import sys

HERE = os.path.dirname(os.path.realpath(__file__))


def main():
    cfg = os.path.join(HERE, 'orghooks.yaml')

    print(f'cfg: {cfg}')
    print(f'sys.argv[1]: {sys.argv[1]}')

    cmd = ['pre-commit', 'run', '--config', cfg, '--files'] + sys.argv[1:]
    os.execvp(cmd[0], cmd)


if __name__ == '__main__':
    exit(main())