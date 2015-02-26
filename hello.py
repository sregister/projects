#!/usr/bin/python

# Created By : Scott Register
# File Name : problem6.py
# Creation Date :
# Last Modified :
# Purpose :


# import modules used here -- sys is a very standard one
#import sys
import os
import getopt
import sys
import getpass


def main(argv):
    # Command line args are in sys.argv[1], sys.argv[2] ..
    # sys.argv[0] is the script name itself and can be ignored
    try:
        opts, args = getopt.getopt(sys.argv[1:], 't:c:', ['term=', 'class='])
    except getopt.GetoptError:
        getopt.usage()
        #print error message
        print "Couldn't parse arguments"
        sys.exit(2)
    #print opts #for debugging
    t_arg = opts[0][1]
    c_arg = opts[1][1]

    print "\n"
    print "Parsed arguments: " + t_arg + "\t" + c_arg
    print "\n"

    l = ['assignments', 'examples', 'exams', 'lecture_note', 'submissions']
    for i in l:
        pwd = os.getcwd() + '/'
        #print pwd

        new_dir = pwd + i
        print "Making " + new_dir

        if not os.path.exists(new_dir):
            os.makedirs(new_dir)
        else:
            print "this path already exists"
            print "\n"
        continue
    print "\n"


    ### Sym-link 1
    #/usr/local/classes/eecs/<term>/<class>/README linked to
    #<pwd>/README

    readme = "/usr/local/classes/eecs/"+ t_arg  + "/" + c_arg + "/README"
    print "Attempting to make link: " + readme

    if not os.path.exists(readme):
        print "Trouble finding that directory"
        sys.exit(2)
    else:
        pass

    sym_1 = os.getcwd() + '/README'
    print "with sym_1 dest: " + sym_1
    if os.path.exists(sym_1):
        print "the directory: " + sym_1 + "is already in use"
        sys.exit(2)
    else:
        os.symlink(readme, sym_1)
        print "\n" + "created the symbolic link"

    print "\n"
    ### Sym-link 2
    #/usr/local/classes/eecs/<term>/<class>/src linked to
    #/home/<user_name>/src_class


    src = "/usr/local/classes/eecs/"+ t_arg  + "/" + c_arg + "/src/"

    print "Attempting to make link: " + src

    if not os.path.exists(src):
        print "Trouble finding that directory"
        sys.exit(2)
    else:
        pass

    user_name = getpass.getuser()
    home_dir = "/home/" + user_name + "/"
    sym_2 = home_dir + 'src_class'
    print "with sym_2 dest: " + sym_2

    if os.path.exists(sym_2):
        print "the directory: " + sym_2 + "is already in use"
        sys.exit(2)

    else:
        os.symlink(src, sym_2)
        print "\n" + "created the symbolic link"


# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    main(sys.argv[1:])

