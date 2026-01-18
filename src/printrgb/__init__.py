"""Rainbow terminal printer."""

from .printrgb import printrgb, get_color_default  # 把核心函数/类导出来
import sys
__all__ = ["printrgb", "get_color_default"]
__version__ = "1.1.1"

if __name__ =='__main__':
    printrgb("". join(map(str,sys.argv[1:])), rainbow = 1)
    printrgb(sys.stdin.read(),rainbow = 1)
