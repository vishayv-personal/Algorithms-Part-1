# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 16:22:52 2016

@author: vishay
"""

"""
Short example of creating a legend in matplotlib
"""
import math
import matplotlib.pyplot as plt

def legend_example():
    """
    Plot an example with two curves with legends
    """
    xvals = [1, 2, 3, 4, 5, 6, 7]
    yvals1 = [1, 2, 3, 4, 5, 6, 7]
    yvals2 = [1, 4, 9, 16, 25, 36, 49]
    yvals3 = [i*math.log(i) for i in range(1,8)]

    plt.plot(xvals, yvals1, '-b', label='linear')
    plt.plot(xvals, yvals2, '-r', label='quadratic')
    plt.plot(xvals, yvals3, '-g', label='nlogn')
    plt.legend(loc='upper left')
    plt.show()

legend_example()
