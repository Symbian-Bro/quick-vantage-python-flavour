import os
import sys
import glob
import time
def root_checker_boy():
    if os.getuid() != 0:
        print("Requesting root privileges...")
        # Do sudo :)
        os.execvp('sudo', ['sudo', sys.executable] + sys.argv)
        sys.exit(1)

root_checker_boy()