import os
for iter in range(0, 15):
    if os.path.exists('./lab{0:02d}'.format(iter)):
        print('./lab{0:02d} already exits'.format(iter))
        continue
    else:
        os.system('wget https://inst.eecs.berkeley.edu/~cs61a/su20/lab/lab{0:02d}/lab{0:02d}.zip'.format(iter))
        os.system('unzip lab{0:02d}.zip'.format(iter))
        os.system('rm -rf lab{0:02d}.zip'.format(iter))
