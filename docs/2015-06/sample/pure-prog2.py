#!/usr/bin/env python
# -*- coding:utf-8 -*-

import argparse

def sum_command(args):
    print(sum(args.integer))

def main():

    parser = argparse.ArgumentParser(description='Process some integers.')
    subparsers = parser.add_subparsers()

    '''
    for `sum` command
    -----------------------------------
    '''

    sum_parser = subparsers.add_parser('sum')
    sum_parser.add_argument('integer', metavar='N', type=int, nargs='+', 
            help='an integer for the accumulator'
            )
    sum_parser.set_defaults(func=sum_command)


    args = parser.parse_args()
    try:
        args.func(args)
    except AttributeError:
        parser.print_help()


if __name__ == '__main__':
    main()
