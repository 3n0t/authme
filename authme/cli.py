# -*- coding: utf-8 -*-

__all__ = ['run']

from getpass import getpass
from argparse import ArgumentParser
from subprocess import Popen, PIPE

from .base import authme,  DEFAULT_TOKEN_HEAD, DEFAULT_TOKEN_LEN
from . import __name__, __version__


def run():
    try:
        parser = ArgumentParser(description='%s v%s' % (__name__, __version__))
        parser.add_argument('-d', '--domain', metavar='')
        parser.add_argument('-l', '--login', metavar='')
        parser.add_argument('-k', '--key', metavar='')
        parser.add_argument('--head', metavar='')
        parser.add_argument('--len', type=int, metavar='')
        parser.add_argument('-e', '--echo', action='store_true')
        args = parser.parse_args()
        domain = args.domain or raw_input('domain: ')
        login = args.login or raw_input('login: ')
        key = args.key or getpass('secret key: ')
        token_head = args.head or DEFAULT_TOKEN_HEAD
        token_len = args.len or DEFAULT_TOKEN_LEN
        token = authme(domain, login, key, token_head, token_len)
        if args.echo:
            print token
        else:
            try:
                Popen(['xclip', '-selection', 'clipboard'], stdin=PIPE
                ).communicate(token)
            except OSError:
                raise RuntimeError('xclip must be installed')
            else:
                print 'auth token [ %s*** ]  > clipboard' % token_head.strip()
    except AssertionError as e:
        print '[error] %s' % str(e)
    except KeyboardInterrupt:
        print
