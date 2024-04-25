#!/usr/bin/env python3
"""
Author:  Iain
Purpose: Say hello
"""

import argparse


def get_args():
    """ Get passed args """
    parser = argparse.ArgumentParser(description='Say hello')
    parser.add_argument('-n', '--name', metavar='name',
                        default='World', help='Name to greet')
    return parser.parse_args()


def main():
    """ Execute program """
    args = get_args()
    print('Hello, ' + args.name + '!')


if __name__ == '__main__':
    main()