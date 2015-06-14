#!/usr/bin/env python
# -*- coding:utf-8 -*-

import click

@click.command()
@click.argument('integers', type=int, nargs=-1, required=True)
@click.option('--sum/--no-sum', 'is_sum', default=False)
def main(integers, is_sum):
    if is_sum:
        click.echo(sum(integers))

if __name__ == '__main__':
    main()
