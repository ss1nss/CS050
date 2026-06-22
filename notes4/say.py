# DO NOT NAME YOUR FILE THE SAME AS WHAT YOU ARE IMPORTING

# packages, are third party libraries you can use with Python
# ASCII Art is a package, for example; these types of packages can be utilized on a cloud/ downloaded, etc
# pypi.org allows you to download all sorts of these packages

# cowsay, is a package that allows people to have a cow speak word for you LOL
# pip = package manager; so you can run: pip [package]

import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.trex("hello, " + sys.argv[1]) # concatenating text with name listed in 1 /// you can switch .cow to .trex to change the image :3
