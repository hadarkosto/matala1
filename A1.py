# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 19:56:47 2023

@author: kosto
"""

#x1= input ("Enter number: ")
#x2= input ("Enter number: ")
#x3= input ("Enter number: ")
#list=[x1,x2,x3]
def my_func(x1, x2, x3):
    if type(x1) is not float or type(x2) is not float or type(x3) is not float:
        return ("Error: parameters should be float","None")
        
    if (x1+x2+x3)==0:
        return ("Not a number: denominator equals zero")
    
    return float(((x1+x2+x3)*(x2+x3)*x3)/(x1+x2+x3))
        
print(my_func(1.0,1.0,-2.0))