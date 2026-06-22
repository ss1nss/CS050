# let's try using cowsay with the saying.py library

import sys

from sayings import hello # from the library, I'm importing just one of the functions (hello)

if len(sys.argv) == 2:
    hello(sys.argv[1])
