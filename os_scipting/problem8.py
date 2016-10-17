#!/usr/bin/python

# Created By : Scott Register
# Email: registsc@onid.orst.edu
# File Name : problem9.py
# Creation Date : Sun 05 Oct 2014 05:29:22 PM PDT
# Last Modified :
# Purpose :
# This script used subprocess to open the unix
# program cal. It takes up to 3 arguments. They are
# not checked in any way, they are passed to the
# cal program so than if there is any error the error
# from cal should be provided to the user.



import subprocess
import shlex
import sys

def main():

    command = 'cal'
    # debug
    # if len(sys.argv) == 1:
    #     command = 'cal'


    # this nested if
    if len(sys.argv) >= 2:
        command = command + ' ' + str(sys.argv[1])
        if len(sys.argv) >= 3:
            command = command + ' ' +str(sys.argv[2])
            if len(sys.argv) >= 4:
                command = command + ' ' + str(sys.argv[3])
            else: pass
        else: pass
    else: pass

    #print command




    command_sequence = shlex.split(command)
    ls = subprocess.Popen(command_sequence, stdout=subprocess.PIPE)
    ls_out = ls.stdout.readlines()

    for line in ls_out:
        print line,

# When you start a Python script, the Python file you identify on the command line
# to Python contains a global name called __name__.  The value of that variable is
# '__main__'.

if __name__ == '__main__':
    main()
