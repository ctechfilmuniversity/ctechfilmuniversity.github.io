import sys;

from os import walk


print(sys.version)


f = []
for (dirpath, dirnames, filenames) in walk("__content/"):
    print(filenames)
    f.extend(filenames)
    break