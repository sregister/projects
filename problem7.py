#!/usr/bin/python

# Created By : Scott Register
# Email: registsc@onid.orst.edu
# File Name : problem7.py
# Creation Date : Sun 05 Oct 2014 05:29:16 PM PDT
# Last Modified :
# Purpose : This script takes two command line args
# the first being a url and the second being a file name
# the script opens the url using urllib2 and then saves
# the response to the file name



import sys
import getopt
import urllib2

def get_file(source, dest):
    pass

    print "Parsed URL:" + source
    print "Parsed destination: " + dest

    try:
        response = urllib2.urlopen(str(source))
    except urllib2.URLError:
        print "ERROR: Couldn't open that URL"
        print "exiting"
        sys.exit(2)

    html = response.read()
    fo = open(str(dest), "wb")
    fo.write(html)
    print "Saved url response to file: " + dest + " in present working directory"


def main(argv):
    try:
        opts, args = getopt.getopt(sys.argv[1:], ['source=', 'dest='])
    except getopt.GetoptError:
        getopt.usage()
        #print error message
        print "Couldn't parse arguments"
        sys.exit(2)


    # print args
    url = args[0]
    dest = args[1]

    get_file(url, dest)


    # Standard boilerplate to call the main() function to begin
    # the program.
if __name__ == '__main__':
    main(sys.argv[1:])

