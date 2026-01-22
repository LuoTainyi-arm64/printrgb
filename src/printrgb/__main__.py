
import sys
from . import printrgb

version = "1.1.6"

def main() -> None:
    argv = sys.argv
    ask  = ''
    if argv:
        if len(argv) == 2:
            if argv[1] in ['-h','--help']:
                ask = 'Argvs of Using printrgb\nprintrgb(*values: object,\nforeground_color: list | tuple | None = None,\nbackground_color: list | tuple | None = None,\nsep: str = " ",\nrainbow: bool = False,\nangle_mode : Literal[\'inner\',\'init\',\'random\'] = \'random\',\nend: str = "\\n",\nfile : object | None = None,\nget_color : types.FunctionType | None = None,\nflush: Literal[False] = False\nswap_fbc: bool = False'
            elif argv[1] in ['-v','--version']:
                ask = f'printrgb {version} by LuoTainyi-arm64'
        printrgb(ask, rainbow = True)
    if not sys.stdin.isatty():
        printrgb(sys.stdin.read(), rainbow = True)

if __name__ == "__main__":
    main()
