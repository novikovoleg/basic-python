import os
print('easy1')
def pathnew(name1):
    path = os.path.join(name1)
    try:
        os.makedirs(path)
        print('created' + name1)
    except FileExistsError:
        print('exists already')

if __name__ == '__main__':
    for i in range(1,10):
        pathnew('{}_{}'.format('dir', i))

def pathremove(name2):
    warning = input('{} {} {}'.format('r u sure', pathremove), 'y/n')
    if warning == 'y':
        os.removedirs(pathremove)
        print('deleted' + pathremove)
    elif warning == 'n':
        print('its safe')
    else:
        print('only y or n pls')

if __name__ == '__main__':
    for i in range(1, 10):
        pathnew('{}_{}'.format('dor', i))

print('easy2')
def dirconsistsof():
    consistsof = [os.listdir()]
    print(consistsof)

import shutil
print('easy3')
def copythat():
    shutil.copy(r'hw5.py', r'hw5_copy.py')

print('norm')
dirconsistsof()

