#!/usr/bin/env python

import re
import sys
import argparse

from argparse import RawTextHelpFormatter


def encrypt(text, key):
    universe = [c for c in (chr(i) for i in range(32, 127))]
    universe_length = len(universe)
    plain_text = text.read().strip()
    key_length = len(key)
    cipher_text = []
    key_text = key

    for i, l in enumerate(plain_text):
        if l not in universe:
            cipher_text.append(l)
        else:
            text_index = universe.index(l)
            k = key_text[i % key_length]
            key_index = universe.index(k)
            code = universe[(text_index + key_index) % universe_length]
            cipher_text.append(code)

    for i in re.finditer('\n', plain_text):
        cipher_text[i.start()] = '\n'

    return ''.join(cipher_text)


def decrypt(text, key):
    universe = [c for c in (chr(i) for i in range(32, 127))]
    universe_length = len(universe)
    plain_text = text.read().strip()
    key_length = len(key)
    cipher_text = []
    key_text = key

    for i, l in enumerate(plain_text):
        if l not in universe:
            cipher_text.append(l)
        else:
            text_index = universe.index(l)
            k = key_text[i % key_length]
            key_index = universe.index(k)
            code = universe[(text_index - key_index) % universe_length]
            cipher_text.append(code)

    for i in re.finditer('\n', plain_text):
        cipher_text[i.start()] = '\n'

    return ''.join(cipher_text)


def main():
    parser = argparse.ArgumentParser(formatter_class=RawTextHelpFormatter,
                                     description='Encrypt or decrypt a vigenere cipher text',
                                     epilog='''
And that's how you'd run this prgramm. You have multiple choices running this programm,
wether you like to read from STDIN or from FILE and wether you like to write to STDOUT
or to FILE. Here I will show you a few examples, how to proper use this programm. When
you want to decrypt a cipher text you can run the following example:

This will decrypt and write the cipher text to STDOUT and read the plain text from STDIN.
echo '<intext>' | ./vigenere.py -d -k <key> -o - -i -

This will encrypt and write the cipher text to STDOUT and read the plain text from FILE.
./vigenere.py -e -k <key> -o - -i <infile>

This will decrypt and write the cipher text to FILE and read the plain text from FILE.
./vigenere.py -d -k <key> -o <outfile> -i <infile>
                                     ''')

    parser.add_argument('-d, --decrypt', dest='decrypt', action='store_true',
                        help='set flag to decrypt given cipher text')
    parser.add_argument('-e, --encrypt', dest='encrypt', action='store_true',
                        help='set flag to encrypt given plain text')
    parser.add_argument('-k, --key', required=True, dest='key',
                        help='set key as argument, this is required')
    parser.add_argument('-i, --in', metavar='INPUT', nargs='?', dest='input', type=argparse.FileType('r'),
                        default=sys.stdin, help='string from stdin or from file')
    parser.add_argument('-o, --out',  metavar='OUTPUT', nargs='?', dest='output', type=argparse.FileType('w'),
                        default=sys.stdout, help='result defaults to stdout or specify a file')

    args = parser.parse_args()

    if args.encrypt:
        value = encrypt(args.input, args.key)
        args.output.write(value)
    elif args.decrypt:
        value = decrypt(args.input, args.key)
        args.output.write(value)


if __name__ == '__main__':
    main()
