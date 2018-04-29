#!/bin/python3

import sys
from math import floor

if __name__ == "__main__":
    meal_cost = float(input().strip())
    tip_percent = int(input().strip())
    tax_percent = int(input().strip())

    tip=meal_cost * (tip_percent/100)
    tax=meal_cost * (tax_percent/100)
    totalCost=tip+tax+meal_cost
    #total=floor(totalCost)

    print ("The total meal cost is ", round(totalCost), "dollars.")
