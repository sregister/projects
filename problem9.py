
#!/usr/bin/python

# Created By : Scott Register
# Email: registsc@onid.orst.edu
# File Name : problem9.py
# Creation Date : Sun 05 Oct 2014 05:29:22 PM PDT
# Last Modified :
# Purpose : This program takes a list
# of numbers and finds the largest product
# of 5 consecutive integers



import sys


def main(argv):
    b = (
    '53697817977846174064955149290862569321978468622482'
    '05886116467109405077541002256983155200055935729725'
    '24219022671055626321111109370544217506941658960408'
    '12540698747158523863050715693290963295227443043557'
    '66896648950445244523161731856403098711121722383113'
    '62229893423380308135336276614282806444486645238749'
    '30358907296290491560440772390713810515859307960866'
    '70172427121883998797908792274921901699720888093776'
    '71636269561882670428252483600823257530420752963450'
    '73167176531330624919225119674426574742355349194934'
    '83972241375657056057490261407972968652414535100474'
    '96983520312774506326239578318016984801869478851843'
    '82166370484403199890008895243450658541227588666881'
    '16427171479924442928230863465674813919123162824586'
    '62229893423380308135336276614282806444486645238749'
    '30358907296290491560440772390713810515859307960866'
    '70172427121883998797908792274921901699720888093776'
    '71636269561882670428252483600823257530420752963450'
    '73167176531330624919225119674426574742355349194934'
    '83972241375657056057490261407972968652414535100474'
    '96983520312774506326239578318016984801869478851843'
    '82166370484403199890008895243450658541227588666881'
    '16427171479924442928230863465674813919123162824586'
    '17866458359124566529476545682848912883142607690042'
    '65727333001053367881220235421809751254540594752243'
    '17866458359124566529476545682848912883142607690042'
    '65727333001053367881220235421809751254540594752243'
    '52584907711670556013604839586446706324415722155397'
    '07198403850962455444362981230987879927244284909188'
    '84580156166097919133875499200524063689912560717606'
    '85861560789112949495459501737958331952853208805511'
    '53697817977846174064955149290862569321978468622482'
    '05886116467109405077541002256983155200055935729725'
    '24219022671055626321111109370544217506941658960408'
    '12540698747158523863050715693290963295227443043557'
    '66896648950445244523161731856403098711121722383113'
    '52584907711670556013604839586446706324415722155397'
    '07198403850962455444362981230987879927244284909188'
    '84580156166097919133875499200524063689912560717606'
    '85861560789112949495459501737958331952853208805511'
    )

    current_prod = 0
    max_prod = 0

    for i in range(len(b)):
        if i <= len(b) - 5:
            current_prod = int(b[i]) * int(b[i+1]) * int(b[i+2]) * int(b[i+3]) * int(b[i+4])
            print "Factors: " + b[i] + b[i+1] + b[i+2] + b[i+3] + b[i+4] + " = " + str(current_prod)
            if current_prod > max_prod:
                max_prod = current_prod
                print "New max product found: " + str(max_prod)
        else:
            break

    print "\n---------"
    print "the max product found was: " + str(max_prod)

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    main(sys.argv[1:])

