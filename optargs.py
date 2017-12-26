import sys

"""Supply defaults for sys.argv variables, falling back to them if there is no CLI input."""
def parse(*default_args):
    return sys.argv[1:len(default_args)+1] + list(default_args[len(sys.argv)-1:])
