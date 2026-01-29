
import sys
from . import printrgb

version = "1.2.2"

def main() -> None:
    argv = sys.argv
    ask  = ''
    if argv:
        if len(argv) == 2:
            if argv[1] in ['-h','--help']:
                ask = '''Argvs of Using printrgb
                printrgb(*values: object,
                foreground_color: list | tuple | None = None,
                background_color: list | tuple | None = None,
                sep: str = " ",
                rainbow: bool = False,
                angle_mode : Literal[\'inner\',\'init\',\'random\'] = \'random\',
                end: str = "\\n",
                file : object | None = None,
                get_color : types.FunctionType | None = None,
                flush: Literal[False] = False
                swap_fbc: bool = False,
                allow_rainbow_blank: bool = False(Using it when swap_fbc))'''
            elif argv[1] in ['-v','--version']:
                ask = f'printrgb {version} by LuoTianyi-arm64'
        printrgb(ask, rainbow = True)
    if not sys.stdin.isatty():
        printrgb(sys.stdin.buffer.read().decode('utf-8'), rainbow = True)

if __name__ == "__main__":
    main()
