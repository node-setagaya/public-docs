#!/usr/bin/env python
# -*- coding:utf-8 -*-

import click

@click.group()
def main():
    pass

@main.command('sum')
@click.argument('integers', type=int, nargs=-1, required=True)
def sum_calc(integers):
    click.echo(sum(integers))

if __name__ == '__main__':
    main()
