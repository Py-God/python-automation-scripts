#! python3
# a simple timesheet app that records when you type a person’s name and uses the current time to clock them in or out.
import time

print('A simple time sheet app.')
register = {}
try:
    while True:
        name = input('Type in a name:\n')
        if name not in register.keys():
            now = time.time()
            register.setdefault(name, now)
            print(name + ': clocked in.')
        else:
            print( name + ': clocked out.', 'timespent: ' + str(round(time.time() - register[name])) + 's')
            register.pop(name)
except KeyboardInterrupt:
    print('done')
    exit()