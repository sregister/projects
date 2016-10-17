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
import random


def main(argv):
    # a = [-1, 2, -3, 4, 5]

    # b = [31, -41, 59, 26, -53, 58, 97, -93, -23, 84]  # max is 187
    # max is 239

    # c = [
    #    22, -27, 38, -34, 49, 40, 13, -44, -13, 28, 46, 7, -26, 42, 29, 0, -6,
    #    35, 23, -37, 10, 12, -2, 18, -12, -49, -10, 37, -5, 17, 6, -11, -22,
    #    -17, -50, -40, 44, 14, -41, 19, -15, 45, -23, 48, -1, -39, -46, 15,
    #    3, -32, -29, -48, -19, 27, -33, -8, 11, 21, -43, 24, 5, 34, -36, -9,
    #    16, -31, -7, -24, -47, -14, -16, -18, 39, -30, 33, -45, -38, 41, -3,
    #    4, -25, 20, -35, 32, 26, 47, 2, -4, 8, 9, 31, -28, 36, 1, -21, 30,
    #    43, 25, -20, -42
    #    ]

#    test_dyna()
    test_enum()
    test_iter()

    return


def test_enum():
    time_enum(100)
    time_enum(200)
    time_enum(300)
    time_enum(400)
    time_enum(500)
    time_enum(600)
    time_enum(700)
    time_enum(800)
    time_enum(900)

    return


def test_iter():
    time_iter(100)
    time_iter(200)
    time_iter(300)
    time_iter(400)
    time_iter(500)
    time_iter(600)
    time_iter(700)
    time_iter(800)
    time_iter(900)
    time_iter(1000)
    time_iter(2000)
    time_iter(3000)
    time_iter(4000)
    time_iter(5000)
    time_iter(6000)
    time_iter(7000)
    time_iter(8000)
    time_iter(9000)

    return


def test_dyna():
    time_dyna(100)
    time_dyna(200)
    time_dyna(300)
    time_dyna(400)
    time_dyna(500)
    time_dyna(600)
    time_dyna(700)
    time_dyna(800)
    time_dyna(900)
    time_dyna(1000)
    time_dyna(2000)
    time_dyna(3000)
    time_dyna(4000)
    time_dyna(5000)
    time_dyna(6000)
    time_dyna(7000)
    time_dyna(8000)
    time_dyna(9000)

    return


# kadanes algorithm
# I got help from :
# http://www.ics.uci.edu/~goodrich/teach/cs161/notes/MaxSubarray.pdf


def time_enum(array_size):
    from timeit import Timer
    times = 0.0
    trial = 0.0
    for i in range(0, 10):
        array = [random.randint(-100, 100) for _ in range(array_size)]
        t = Timer(lambda: enumeration(array))
        trial = t.timeit(number=1)
        print trial
        times += float(trial)
    print "\nAlg 1: Enumeration"
    print "Array size: " + str(array_size)
    print "Avg of 10 trials in " + str(times / 10) + "seconds\n"


def time_iter(array_size):
    from timeit import Timer
    times = 0.0
    trial = 0.0
    for i in range(0, 10):
        array = [random.randint(-100, 100) for _ in range(array_size)]
        t = Timer(lambda: enumeration(array))
        trial = t.timeit(number=1)
        print trial
        times += float(trial)
    print "\nAlg 2: Better Enumeration"
    print "Array size: " + str(array_size)
    print "Avg of 10 trials in " + str(times / 10) + "seconds\n"


def time_dyna(array_size):
    from timeit import Timer
    times = 0.0
    trial = 0.0
    for i in range(0, 10):
        array = [random.randint(-100, 100) for _ in range(array_size)]
        t = Timer(lambda: dynamic(array))
        trial = t.timeit(number=1)
        print trial
        times += float(trial)
    print "\nAlg 3: Dynamic Programming"
    print "Array size" + str(array_size)
    print "Avg of 10 trials in " + str(times / 10) + "seconds\n"


def enumeration(array):
    maximum = 0
    for j in range(len(array)):
        for k in range(j, len(array)):
            summation = 0
            for i in range(j, k):
                summation = summation + array[i]
            if summation > maximum:
                # print "New maximum found"
                maximum = summation
                # print maximum

    print "Max subarray: " + str(maximum)
    return


def iteration(array):
    maximum = 0
    summation = 0
    for i in range(1, len(array)):
        summation = 0
        for j in range(i, len(array)):
            summation = summation + array[j]
            if summation > maximum:
                # print "New maximum found"
                maximum = summation
                # print maximum

    print "Max subarray: " + str(maximum)
    return


# kadanes algorithm
# I got help from :
# http://www.ics.uci.edu/~goodrich/teach/cs161/notes/MaxSubarray.pdf


def dynamic(array):
    summation = 0
    maximum = 0
    for t in array:
        summation = max(0, summation + t)
        maximum = max(maximum, summation)
    print "Max Subarray: " + str(maximum)
    return

if __name__ == '__main__':
    main(sys.argv[1:])
