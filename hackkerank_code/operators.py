#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function accepts following parameters:
#  1. DOUBLE meal_cost
#  2. INTEGER tip_percent
#  3. INTEGER tax_percent
#

def solve(meal_cost, tip_percent, tax_percent):
    # Write your code here
    tax_percent_decimal = tax_percent/100
    tax_amount = tax_percent_decimal*meal_cost
    # print ("Tax amount")
    # print (math.ceil(tax_amount)) 
    tip_percent_decimal = tip_percent/100
    tip_amount = tip_percent_decimal * meal_cost
    # print ("Tip amount")
    # print (math.ceil(tip_amount))
    print (round(tax_amount + tip_amount + meal_cost))
    

if __name__ == '__main__':
    meal_cost = float(input().strip())

    tip_percent = int(input().strip())

    tax_percent = int(input().strip())

    solve(meal_cost, tip_percent, tax_percent)