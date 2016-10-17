#!/usr/bin/python

# Created By : Scott Register
# Oregon State University
# College of Engineering - School of EECS
# Email: registsc@onid.orst.edu
# File Name : a1.py
# Creation Date : Mon 12 Jan 2015 07:15:43 PM PST
# Last Modified : Tue 13 Jan 2015 05:01:35 AM PST
# Purpose :
# This program provides 3 algorithms for
# solving the maximum subarray problem.
#
# Sources:
# Glencora Borradaile "Crash course in theoretical comp sci"
# https://web.engr.oregonstate.edu/~glencora/wiki/uploads/max-subarray.pdf
#
# Goodrich "A case study of algorithm Analysis"
# http://www.ics.uci.edu/~goodrich/teach/cs161/notes/MaxSubarray.pdf


import sys
# import random


class locker:
    '''This is a locker object'''
    closest_key = 0


def main(argv):

    enum_test()

    return


def enum_test():
    keys = ['5', '3', '1', '6', '4']
    balls = ['12', '0', '5', '8', '3', '1']
    enum(keys, balls, 15)
    print "Answer should be 11\n"

    keys = ['1', '2']
    balls = ['0', '3']
    enum(keys, balls, 5)
    print "Answer should be 4\n"

    keys = ['11', '52', '31', '17', '10', '47', '16', '62', '6', '53',
            '19', '3', '5', '7', '13', '55']
    balls = ['65', '31', '38', '15', '7', '39', '18', '51', '52', '11',
             '20', '50', '21', '18']
    enum(keys, balls, 80)
    print "Answer should be 25\n"

    return


# This function contains my first algorithm for
# solving the locker problem


def enum(keys, balls, n):
    opened = []
    set = []
    for p in range(n):
        set.append(locker())

    shortest = 10000
    for b in balls:
        # print "finding nearest key for ball " + str(b)
        shortest = 10000
        for k in keys:
            distance = abs(int(b) - int(k))
            # print "Distance from ball in " + str(b) + " to key in " + str(k) + " is " \
            #      + str(distance) + "\n"
            if distance < shortest:
                shortest = distance
                set[int(b)].closest_key = int(k)
                # print "NEW SHORTEST FOUND for ball " + str(b)
                # print "\tit is now: " + str(shortest) + " using key " \
                #     + str(k) + "\n"

    # for p in range(n):
        # print "set[" + str(p) + "]: " + str(set[p].closest_key)

    for b in balls:
        # print "value of b " + str(b)
        k = set[int(b)].closest_key

        print "ball " + str(b) + " key is : " + str(k)
        if b > k:
                # print "There is a ball(s) to the LEFT of key " + str(k) \
                #     + "ball at: " + str(b)
                distance = int(k) - int(b)
                # print "Distance from key in " + str(k) + " to ball in " + str(b) \
                #      + " is " + str(distance)
                for open_locker in range(int(b), int(k)+1):
                    if open_locker not in opened:
                        opened.append(open_locker)
                print opened

        if b >= k:
                # print "There is a ball(s) to the RIGHT of key " + str(k) \
                #      + "ball at: " + str(b)
                distance = int(b) - int(k)
                # print "Distance from key in " + str(k) + " to ball in " + str(b) \
                #       + " is " + str(distance)
                for open_locker in range(int(k), int(b)+1):
                    if open_locker not in opened:
                        opened.append(open_locker)
    print "\n\tLockers Opened: (unsorted)\n"
    print opened
    print "Sum:" + str(len(opened))

    return

if __name__ == '__main__':
    main(sys.argv[1:])
