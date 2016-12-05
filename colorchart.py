'''
    Black      0;30       Dark Gray    1;30 
    Red        0;31       Bold Red     1;31 
    Green      0;32       Bold Green   1;32 
    Yellow     0;33       Bold Yellow  1;33 
    Blue       0;34       Bold Blue    1;34  
    Purple     0;35       Bold Purple  1;35 
    Cyan       0;36       Bold Cyan    1;36 
    Light Gray 0;37       White        1;37

##==========================================================================##

### Another color changer for text!
def print_format_table():
    """
    prints table of formatted text format options
    """
    for style in range(8):
        for fg in range(30,38):
            s1 = ''
            for bg in range(40,48):
                format = ';'.join([str(style), str(fg), str(bg)])
                s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
            print(s1)
        print('\n')

#print_format_table()

##==========================================================================##

#### Change coulours of text in Linux environment
def prRed(prt): print("\033[91m {}\033[00m" .format(prt))
def prGreen(prt): print("\033[92m {}\033[00m" .format(prt))
def prYellow(prt): print("\033[93m {}\033[00m" .format(prt))
def prLightPurple(prt): print("\033[94m {}\033[00m" .format(prt))
def prPurple(prt): print("\033[95m {}\033[00m" .format(prt))
def prCyan(prt): print("\033[96m {}\033[00m" .format(prt))
def prLightGray(prt): print("\033[97m {}\033[00m" .format(prt))
def prBlack(prt): print("\033[98m {}\033[00m" .format(prt))

#prGreen("Hello world")

##==========================================================================## 

import ctypes

# Constants from the Windows API
STD_OUTPUT_HANDLE = -11
FOREGROUND_RED    = 0x0004 # text color contains red.

def get_csbi_attributes(handle):
    # Based on IPython's winconsole.py, written by Alexander Belchenko
    import struct
    csbi = ctypes.create_string_buffer(22)
    res = ctypes.windll.kernel32.GetConsoleScreenBufferInfo(handle, csbi)
    assert res

    (bufx, bufy, curx, cury, wattr,
    left, top, right, bottom, maxx, maxy) = struct.unpack("hhhhHhhhhhh", csbi.raw)
    return wattr


handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
reset = get_csbi_attributes(handle)

ctypes.windll.kernel32.SetConsoleTextAttribute(handle, FOREGROUND_RED)
print ("Cherry on top")
ctypes.windll.kernel32.SetConsoleTextAttribute(handle, reset) 

##==========================================================================## 

class PrintInColor:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    LIGHT_PURPLE = '\033[94m'
    PURPLE = '\033[95m'
    END = '\033[0m'

    @classmethod
    def red(cls, s, **kwargs):
        print(cls.RED + s + cls.END, **kwargs)

    @classmethod
    def green(cls, s, **kwargs):
        print(cls.GREEN + s + cls.END, **kwargs)

    @classmethod
    def yellow(cls, s, **kwargs):
        print(cls.YELLOW + s + cls.END, **kwargs)

    @classmethod
    def lightPurple(cls, s, **kwargs):
        print(cls.LIGHT_PURPLE + s + cls.END, **kwargs)

    @classmethod
    def purple(cls, s, **kwargs):
        print(cls.PURPLE + s + cls.END, **kwargs)

PrintInColor.red('hello', end=' ')
PrintInColor.green('world') 

##==========================================================================## 

### This one shows some mad characters too!!
for i in range(255):
    print (i, chr(i))   



print (colors.draw("i'm yellow", bold=True, fg_yellow=True))   '''

# display text on a Windows console
# Windows XP with Python27 or Python32
from ctypes import windll
# needed for Python2/Python3 diff
try:
    input = raw_input
except:
    pass
STD_OUTPUT_HANDLE = -11
stdout_handle = windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
# look at the output and select the color you want
# for instance hex E is yellow on black
# hex 1E is yellow on blue
# hex 2E is yellow on green and so on
for color in range(0, 75):
     windll.kernel32.SetConsoleTextAttribute(stdout_handle, color)
     print("%X --> %s" % (color, "Have a fine day!"))
     input("Press Enter to go on ... ")

