import sys, re

class TeeLogger(object):
    def __init__(self, logfilename):
        self.terminal = sys.stdout
        self.log = open(logfilename, 'w')
        self.ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    def write(self, message):
        self.terminal.write(message)
        self.log.write(self.ansi_escape.sub('', message))
    def flush(self):
        self.terminal.flush()
        self.log.flush()

def startTeeLogging(filename):
    global sys
    sys.stdout = TeeLogger(filename)

def bg(text, col):
    return {
        'BLACK'    : '\033[40m',
        'RED'      : '\033[41m',
        'GREEN'    : '\033[42m',
        'YELLOW'   : '\033[43m',
        'BLUE'     : '\033[44m',
        'MAGENTA'  : '\033[45m',
        'CYAN'     : '\033[46m',
        'WHITE'    : '\033[47m'       
    }.get(col, '') + text + '\033[49m'

def fg(text, col):
    return {
        'BLACK'    : '\033[30m',
        'RED'      : '\033[31m',
        'GREEN'    : '\033[32m',
        'YELLOW'   : '\033[33m',
        'BLUE'     : '\033[34m',
        'MAGENTA'  : '\033[35m',
        'CYAN'     : '\033[36m',
        'WHITE'    : '\033[37m',
        'GREY'     : '\033[90m'
    }.get(col, '') + text + '\033[39m'
     