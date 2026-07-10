import os

with open('./random.bin','w') as f:
    f.write(os.urandom(10))