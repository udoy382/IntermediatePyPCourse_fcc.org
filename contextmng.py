# with open('note.txt', 'w') as file:
#     file.write('some todoo...')


# file = open('note.text', 'w')
# try:
#     file.write('some todoo...')
# finally:
#     file.close()

#--------------------------------------

# from threading import Lock
# lock = Lock()

# lock.acquire()

# #...
# lock.release()

# with lock:

#----------------------------------------
'''
class ManagedFile:
    def __init__(self, filename):
        print('init')
        self.filename = filename

    def __enter__(self):
        print('enter')
        self.file = open(self.filename, 'w')
        return self.file


    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.file:
            self.file.close()
        if exc_type is not None:
            print('exception has ben handled')
            # print('exc', exc_type, exc_value)
            print('exit')
            return True

with ManagedFile('notes.txt') as file:
    print('do some stuff...')
    file.write('some todoo...')
    file.somemethod
print('continuing')
'''

from contextlib import contextmanager

@contextmanager
def open_managed_file(filename):
    f = open(filename, 'w')
    try:
        yield f
    finally:
        f.close()

with open_managed_file('notes.txt') as f:
    f.write('some todoo...')