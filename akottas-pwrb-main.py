##**************************************************##
## Filename:     akottas-pwrb-main.py
## Author:       Apostolos Kottas 
## Date:         May 18th 2013 (Start)
## Date:         June 1st 2013 (Fin)
## ===========================================
## Description:
## ------------
##   Reading Powerball numbers from a .csv file and
##   performing some statistical analysis on them
##**************************************************##

# "modules" to include // or actually "extensions" because they're written in C

from sys import argv

import csv
import numpy as np
import scipy as sp
import matplotlib as mpl
import matplotlib.pyplot as plt

pb_nums_raw_csv = open('winnums-text-import.csv', 'r')


b_white_range = range(1, 59)  ## White ball (min, max) = (1, 59)
b_red_range = range(1, 35)    ## Red ball (min, max) = (1, 35)


# (nˆX)(eˆ−n)/X!
# Probability of (X wins) = (nˆX)(eˆ−n)/X!, 
# where n = 0.1298 average winning tickets per drawing, 
# X = possible number of winning tickets per drawing,





# b_white_min = 1
# b_white_max = 59
# b_red_min = 1
# ball_red_max = 35

# b_white_rng = range(b_white_min, b_white_max)
# b_red_rng = range(b_red_min, b_red_max)





#import web
#import urllib

# u = urllib.urlopen('http://www.powerball.com/powerball/pb_nbr_history.asp?startDate=5%2F13%2F2009&endDate=5%2F29%2F2013')
# PowerbNums = u.read()

# u = read("winnumbs-text.txt")





# ## This first function takes TWO arguments - and is a lot like our previous scripts with argv
# def print_two(*args):
# 	arg1, arg2 = args
# 	print "arg1: %r, arg2: %r" % (arg1, arg2)

# ## The previous *args is actually pointless (??) - so we can actually do the following
# def print_two_again(arg1, arg2):
# 	print "arg1: %r, arg2 %r" % (arg1, arg2)

# ## This function takes ONE argument
# def print_one(arg1):
# 	print "arg1: %r" % arg1

# ## This function takes NO arguments
# def print_none():
# 	print "I got nothin'!"


# print_two("Apost","Tolis")
# print_two_again("Apost-again","Tolis_again")
# print_one("first!")
# print_none()
