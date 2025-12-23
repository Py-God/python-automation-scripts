#! python3
# give the user a chance to press CTRL-C to cancel an action, such as deleting files.
import time, send2trash, os

print('''Ready to delete contents of headerRemoved folder
type 'y' to continue, n to terminate, ctrl+c to terminate after starting''')
ans = input().lower()
try:
    if ans == 'y':
        for files in os.listdir('headerRemoved'):
            print('deleting ' + files)
            send2trash.send2trash(os.path.join('headerRemoved', files))
            time.sleep(1)
        print('Done')
    else:
        exit()
except KeyboardInterrupt:
    print('canceled')