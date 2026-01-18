
import sys
from . import printrgb

def main() -> None:
    arg_txt = " ".join(sys.argv[1:])
    if arg_txt:
        printrgb(arg_txt, rainbow = True)
    if not sys.stdin.isatty():
        printrgb(sys.stdin.read(), rainbow = True)

if __name__ == "__main__":
    main()