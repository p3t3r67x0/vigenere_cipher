# vigenere.py


Simple programm to encrypt or decrypt a vigenere cipher text.


```
usage: vigenere.py [-h] [-d, --decrypt] [-e, --encrypt] -k, --key KEY
                   [-i, --in [INPUT]] [-o, --out [OUTPUT]]

Encrypt or decrypt a vigenere cipher text

optional arguments:
  -h, --help          show this help message and exit
  -d, --decrypt       set flag to decrypt given cipher text
  -e, --encrypt       set flag to encrypt given plain text
  -k, --key KEY       set key as argument, this is required
  -i, --in [INPUT]    string from stdin or from file
  -o, --out [OUTPUT]  result defaults to stdout or specify a file

And that's how you'd run this prgramm. You have multiple choices running this programm,
wether you like to read from STDIN or from FILE and wether you like to write to STDOUT
or to FILE. Here I will show you a few examples, how to proper use this programm. When
you want to decrypt a cipher text you can run the following example:

This will encrypt and write the cipher text to STDOUT and read the plain text from FILE.
./vigenere.py -e -k <key> -o - -i <infile>

This will decrypt and write the cipher text to FILE and read the plain text from FILE.
./vigenere.py -d -k <key> -o <outfile> -i <infile>

This will encrypt and write the cipher text to STDOUT and read the plain text from STDIN.
echo '<intext>' | ./vigenere.py -d -k <key> -o - -i -
```
