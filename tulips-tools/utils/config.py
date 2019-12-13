import os

PATH = os.environ['HOME'] + "/.tulips"

def save_config(name, password):
    s = '{}\n{}\n'.format(name, password)

    with open(PATH, mode='w') as f:
        f.write(s)

    os.chmod(PATH, 0o700)

def load_config():
    with open(PATH) as f:
        l = f.readlines()
        name = l[0].rstrip()
        password = l[1].rstrip()

    return name, password

