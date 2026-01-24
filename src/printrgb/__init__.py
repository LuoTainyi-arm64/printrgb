from .printrgb import printrgb
import sys
__all__ = ["printrgb"]
__version__ = "1.1.10"

if __name__ =='__main__':
    printrgb("". join(map(str,sys.argv[1:])), rainbow = 1)
    printrgb(sys.stdin.read(),rainbow = 1)
