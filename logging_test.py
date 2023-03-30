from time import sleep

from pytoolkit.logging import startTeeLogging, bg, fg
from pytoolkit.datetime_h import ts as timestamp_func
def ts():
    return fg(timestamp_func(), 'GREY')

print('HELLO, NOT LOGGED TO FILE')

startTeeLogging('test_log_file.log')

print(f"{ts()} | HELLO, LOGGED TO FILE")
print(f"{ts()} | OOOOH! | {fg('WARNING', 'YELLOW')} ")
print(f"{ts()} | UH OH! | {bg('CRITICAL', 'RED')} ")

