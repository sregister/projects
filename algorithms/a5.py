#!/usr/bin/python 

# Created By : Scott Register
# Oregon State University
# College of Engineering - School of EECS
# Email: registsc@onid.orst.edu
# File Name : a5.py
# Creation Date : Mon 12 Jan 2015 07:15:43 PM PST
# Last Modified : Tue 13 Jan 2015 05:01:35 AM PST
# Purpose : reading data weather data from csv
# and running it through an LP Solver

import sys
import math
import pulp
import csv

def main(argv):
    points = []
    with open('1000days.csv', 'rb') as csvfile:
        read = csv.reader(csvfile, delimiter=';', quotechar='|')
        for row in read:
            #print 'day: ' + str(row[8]) + ' avg: ' + str(row[7])
            points.append([float(row[8]), float(row[7])])

    #print points
    a = math.pi
    print a

    prob = pulp.LpProblem("min abs dev", pulp.LpMinimize)
    x0 = pulp.LpVariable("x0")
    x1 = pulp.LpVariable("x1")
    x2 = pulp.LpVariable("x2")
    x3 = pulp.LpVariable("x3")
    x4 = pulp.LpVariable("x4")
    x5 = pulp.LpVariable("x5")
    tvar = pulp.LpVariable("tvar")
    prob += tvar
    return

if __name__ == '__main__':
    main(sys.argv[1:])
