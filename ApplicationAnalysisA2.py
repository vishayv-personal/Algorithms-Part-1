"""
Provided code for Application portion of Module 2
"""

# general imports
import urllib2
import random
import time
import math
from collections import deque

# CodeSkulptor import
#import simpleplot
#import codeskulptor
#codeskulptor.set_timeout(300)

# Desktop imports
import matplotlib.pyplot as plt


############################################
# Provided code



GRAPH0 = {0:set([1]),1:set([0, 2]),2:set([1, 3]),3:set([2])}

GRAPH1 = {0: set([1, 2, 3, 4]),
          1: set([0, 2, 3, 4]),
          2: set([0, 1, 3, 4]),
          3: set([0, 1, 2, 4]),
          4: set([0, 1, 2, 3])}

GRAPH2 = {1: set([2, 4, 6, 8]),
          2: set([1, 3, 5, 7]),
          3: set([2, 4, 6, 8]),
          4: set([1, 3, 5, 7]),
          5: set([2, 4, 6, 8]),
          6: set([1, 3, 5, 7]),
          7: set([2, 4, 6, 8]),
          8: set([1, 3, 5, 7])}

GRAPH3 = {0: set([]),
          1: set([2]),
          2: set([1]),
          3: set([4]),
          4: set([3])}

GRAPH4 = {0: set([1, 2, 3, 4]),
          1: set([0]),
          2: set([0]),
          3: set([0]),
          4: set([0]),
          5: set([6, 7]),
          6: set([5]),
          7: set([5])}

GRAPH5 = {"dog": set(["cat"]),
          "cat": set(["dog"]),
          "monkey": set(["banana"]),
          "banana": set(["monkey", "ape"]),
          "ape": set(["banana"])}

GRAPH6 = {1: set([2, 5]),
          2: set([1, 7]),
          3: set([4, 6, 9]),
          4: set([3, 6, 9]),
          5: set([1, 7]),
          6: set([3, 4, 9]),
          7: set([2, 5]),
          9: set([3, 4, 6])}

GRAPH7 = {0: set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 
                  27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]), 
          1: set([0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 
                  27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]), 
          2: set([0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 
                  27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]), 
          3: set([0, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 
                  27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]), 
          4: set([0, 1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 
                  27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]), 
          5: set([0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 
                  27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]), 
          6: set([0, 1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 
                  27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]), 
          7: set([0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 
                  27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]), 
          8: set([0, 1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 
                  27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]), 
          9: set([0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 
                  27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]), 
          10: set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 
                   27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]), 
          11: set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 
                   27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]), 
          12: set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 
                   27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]), 
          13: set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 
                   27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]), 
          14: set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 
                   27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]), 
          15: set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 
                   27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]), 
          16: set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 
                   27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]), 
          17: set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 21, 22, 23, 24, 25, 26, 
                   27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]), 
          18: set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 19, 20, 21, 22, 23, 24, 25, 26, 
                   27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]), 
          19: set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21, 22, 23, 24, 25, 26, 
                   27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]), 
          20: set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 22, 23, 24, 25, 26, 
                   27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]), 
          21: set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 22, 23, 24, 25, 26, 
                   27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]), 
          22: set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 25, 26, 
                   27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]), 
          23: set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 
                   27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]), 
          24: set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 
                   27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]), 
          25: set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 26, 
                   27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]), 
          26: set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 
                   27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]), 
          27: set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 
                   26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]), 
          28: set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 
                   26, 27, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]), 
          29: set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 
                   26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]), 
          30: set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 
                   26, 27, 28, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]), 
          31: set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 
                   26, 27, 28, 29, 30, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]), 
          32: set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 
                   26, 27, 28, 29, 30, 31, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]), 
          33: set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 
                   26, 27, 28, 29, 30, 31, 32, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]), 
          34: set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 
                   26, 27, 28, 29, 30, 31, 32, 33, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]), 
          35: set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 
                   26, 27, 28, 29, 30, 31, 32, 33, 34, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]), 
          36: set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 
                   26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]), 
          37: set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 
                   26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]), 
          38: set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 
                   26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]), 
          39: set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 
                   26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]), 
          40: set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 
                   26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 41, 42, 43, 44, 45, 46, 47, 48, 49]), 
          41: set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 
                   26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 42, 43, 44, 45, 46, 47, 48, 49]), 
          42: set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 
                   26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45, 46, 47, 48, 49]), 
          43: set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 
                   26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 44, 45, 46, 47, 48, 49]), 
          44: set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 
                   26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 45, 46, 47, 48, 49]), 
          45: set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 
                   26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 46, 47, 48, 49]), 
          46: set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 
                   26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 47, 48, 49]), 
          47: set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 
                   26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 48, 49]), 
          48: set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 
                   26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 49]), 
          49: set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 
                   26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48])}

GRAPH8 = {0: set([]), 
          1: set([]), 
          2: set([]), 
          3: set([]), 
          4: set([]), 
          5: set([]), 
          6: set([]), 
          7: set([]), 
          8: set([]), 
          9: set([]), 
          10: set([]), 
          11: set([]), 
          12: set([]), 
          13: set([]), 
          14: set([]), 
          15: set([]), 
          16: set([]), 
          17: set([]), 
          18: set([]), 
          19: set([]), 
          20: set([]), 
          21: set([]), 
          22: set([]), 
          23: set([]), 
          24: set([]), 
          25: set([]), 
          26: set([]), 
          27: set([]), 
          28: set([]), 
          29: set([]), 
          30: set([]), 
          31: set([]), 
          32: set([]), 
          33: set([]), 
          34: set([]), 
          35: set([]), 
          36: set([]), 
          37: set([]), 
          38: set([]), 
          39: set([]), 
          40: set([]), 
          41: set([]), 
          42: set([]), 
          43: set([]), 
          44: set([]), 
          45: set([]), 
          46: set([]), 
          47: set([]), 
          48: set([]), 
          49: set([])}


GRAPH9 = {0: set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]),
          1: set([0, 3, 4, 7, 8, 9, 10]),
          2: set([0, 5, 6, 11, 12, 13, 14]),
          3: set([0, 1, 7, 8]),
          4: set([0, 1, 9, 10]),
          5: set([0, 2, 11, 12]),
          6: set([0, 2, 13, 14]),
          7: set([0, 1, 3]),
          8: set([0, 1, 3]),
          9: set([0, 1, 4]),
          10: set([0, 1, 4]),
          11: set([0, 2, 5]),
          12: set([0, 2, 5]),
          13: set([0, 2, 6]),
          14: set([0, 2, 6])}

GRAPH10 = {0: set([1, 2]),
           1: set([0]),
           2: set([0, 3, 4]),
           3: set([2]),
           4: set([2, 5, 6,]),
           5: set([4]),
           6: set([4, 7, 8]),
           7: set([6]),
           8: set([6, 9 , 10]),
           9: set([8]),
           10: set([8, 11, 12]),
           11: set([10]),
           12: set([10,13, 14]),
           13: set([12]),
           14: set([12, 15, 16]),
           15: set([14]),
           16: set([14, 17, 18]),
           17: set([16]),
           18: set([16, 19, 20]),
           19: set([18]),
           20: set([18])}


def copy_graph(graph):
    """
    Make a copy of a graph
    """
    new_graph = {}
    for node in graph:
        new_graph[node] = set(graph[node])
    return new_graph

def delete_node(ugraph, node):
    """
    Delete a node from an undirected graph
    """
    neighbors = ugraph[node]
    ugraph.pop(node)
    for neighbor in neighbors:
        ugraph[neighbor].remove(node)
    
def targeted_order(ugraph):
    """
    Compute a targeted attack order consisting
    of nodes of maximal degree
    
    Returns:
    A list of nodes
    """
    # copy the graph
    new_graph = copy_graph(ugraph)
    
    order = []    
    while len(new_graph) > 0:
        max_degree = -1
        for node in new_graph:
            if len(new_graph[node]) > max_degree:
                max_degree = len(new_graph[node])
                max_degree_node = node
        
        neighbors = new_graph[max_degree_node]
        new_graph.pop(max_degree_node)
        for neighbor in neighbors:
            new_graph[neighbor].remove(max_degree_node)

        order.append(max_degree_node)
    return order

def fast_targeted_order(graph2):
    
    # init 
    graph = copy_graph(graph2)
    attack_order = []
    degree_set = dict()
    num_nodes = len(graph)
    # degree distribution can range from 0 to n-1. init this range to n
    for dummy_var in range(num_nodes): # o(n)
        degree_set[dummy_var] = set()
        #print dummy_var
    #count = 0    
    for node in graph.keys():
        node_degree = len(graph[node])
        degree_set[node_degree].add(node)
        #count +=1 
    #print "graph",graph
    #print degree_set
    
    #count=0
    # traverse from degree n-1 to 0 and create targeted order
    for degree in xrange(num_nodes-1,-1,-1):  #o(n)
        
        while len(degree_set[degree]) > 0:
            #print degree
            # arbitarily choose any element/node and remove it from set
            edge_node = degree_set[degree].pop()  # o(1) 
            for neighbor_node in graph[edge_node]:
                degree_neighbor = len(graph[neighbor_node])
                degree_set[degree_neighbor].remove(neighbor_node)
                if(degree_neighbor-1 >= 0):
                    degree_set[degree_neighbor-1].add(neighbor_node)
            attack_order.append(edge_node)
            #count +=1 
            delete_node(graph, edge_node)
    #print "len",len(graph.keys())
    #print degree_set
    #print "count",count
    return attack_order
##MY HELPER METHODS 

def bfs_visited(ugraph, start_node):

    """
    akes the undirected graph ugraph and the node start_node and 
    returns the set consisting of all nodes that are visited by 
    a breadth-first search that starts at start_node.
    """

    #initialize
    visited_set = set([start_node])
    bfs_queue = deque()
    bfs_queue.append(start_node)

    # till queue is not empty pop
    while len(bfs_queue) != 0:
        g_node = bfs_queue.popleft()
        
        # avoid of infinite loop by checking neighbor has not already been visited
        for neighbor_node in ugraph[g_node]:
            if(neighbor_node not in visited_set):
                bfs_queue.append(neighbor_node)
                visited_set.add(neighbor_node)
    return visited_set


#print bfs_visited(GRAPH0,0)
#print bfs_visited(GRAPH1,0)
#print bfs_visited(GRAPH2,1)
#print bfs_visited(GRAPH3,0)
#print bfs_visited(GRAPH4,0)
#print bfs_visited(GRAPH5,"dog")
#print bfs_visited(GRAPH5,"monkey")
#print bfs_visited(GRAPH6,1)
#rint bfs_visited(GRAPH7,0)
#print bfs_visited(GRAPH8,0)
#print bfs_visited(GRAPH9,0)
#print bfs_visited(GRAPH10,0)

def cc_visited(ugraph) :
    """
    takes the undirected graph ugraph and returns a list of sets, 
    where each set consists of all the nodes (and nothing else) in a connected component, 
    and there is exactly one set in the list for each connected component in ugraph and nothing else.

    """
    # init set list and remain list 
    cc_list = []
    remain_set = set(ugraph.keys())

    while len(remain_set) !=0:

        # take one node from remain, randomly choose one.
        start_node = random.sample(remain_set,1)[0]  # o(n) 
        bfs_set = bfs_visited(ugraph, start_node)
        cc_list.append(bfs_set)   # o(num elements)
        remain_set = remain_set.symmetric_difference(bfs_set)  #o(numelements s * t)
        
    return cc_list

#print cc_visited(GRAPH5)
#print cc_visited(GRAPH0)
#print cc_visited(GRAPH1)
#print cc_visited(GRAPH2)
#print cc_visited(GRAPH3)
#print cc_visited(GRAPH4)
#print cc_visited(GRAPH5)
#print cc_visited(GRAPH5)
#print cc_visited(GRAPH6)
#print cc_visited(GRAPH7)
#print cc_visited(GRAPH8)
#print cc_visited(GRAPH9)
#print cc_visited(GRAPH10)

def largest_cc_size(ugraph):
    
    """
    Takes the undirected graph ugraph 
    and returns the size (an integer) 
    of the largest connected component in ugraph.
    """

    cc_max = 0
    #cc_max_set = None
    cc_list = cc_visited(ugraph)
    for cc_set in cc_list:

        len_set = len(cc_set)
        if(len_set > cc_max):
            cc_max = len_set
            #cc_max_set = cc_set
    return cc_max

print largest_cc_size(GRAPH5)

def compute_resilience(ugraph, attack_order):

    """
    For each node in attack_order, 
    the function removes the given node and 
    its edges from the graph and then computes 
    the size of the largest connected component 
    for the resulting graph.
    The function should return a list whose 
    k+1th entry is the size of the largest 
    connected component in the graph after the 
    removal of the first k nodes in attack_order. 
    """

    out_list = []
    largest_size = largest_cc_size(ugraph)
    out_list.append(largest_size)

    for attack_node in attack_order:

        attack_node_neighbors = ugraph[attack_node]

        for node in attack_node_neighbors:
            ugraph[node].remove(attack_node)

        del ugraph[attack_node]
        out_list.append(largest_cc_size(ugraph))
    return out_list

print compute_resilience(GRAPH5, ["ape", "monkey"])

def make_ER_graph(num_nodes, p_threshold):
    """
    creates a complete graph with num_nodes number of vertices
    input = number of nodes 
    output = a complete graph with input number of nodes
    """
    graph = dict()
    for node in range(num_nodes):
        graph[node] = set()
    
    for node in range(num_nodes):
        #print node
        edge_set = set()
        for edge_node in range(num_nodes):
            if(node != edge_node):
                p = random.random()
                if(p < p_threshold):
                    edge_set.add(edge_node)
                    graph[edge_node].add(node)
                    #print node,edge_node, edge_set
        graph[node].update(edge_set)   
    return graph


"""
Provided code for application portion of module 2

Helper class for implementing efficient version
of UPA algorithm
"""

import random

class UPATrial:
    """
    Simple class to encapsulate optimizated trials for the UPA algorithm
    
    Maintains a list of node numbers with multiple instance of each number.
    The number of instances of each node number are
    in the same proportion as the desired probabilities
    
    Uses random.choice() to select a node number from this list for each trial.
    """

    def __init__(self, num_nodes):
        """
        Initialize a UPATrial object corresponding to a 
        complete graph with num_nodes nodes
        
        Note the initial list of node numbers has num_nodes copies of
        each node number
        """
        self._num_nodes = num_nodes
        self._node_numbers = [node for node in range(num_nodes) for dummy_idx in range(num_nodes)]


    def run_trial(self, num_nodes):
        """
        Conduct num_nodes trials using by applying random.choice()
        to the list of node numbers
        
        Updates the list of node numbers so that each node number
        appears in correct ratio
        
        Returns:
        Set of nodes
        """
        
        # compute the neighbors for the newly-created node
        new_node_neighbors = set()
        for _ in range(num_nodes):
            new_node_neighbors.add(random.choice(self._node_numbers))
        
        # update the list of node numbers so that each node number 
        # appears in the correct ratio
        self._node_numbers.append(self._num_nodes)
        for dummy_idx in range(len(new_node_neighbors)):
            self._node_numbers.append(self._num_nodes)
        self._node_numbers.extend(list(new_node_neighbors))
        
        #update the number of nodes
        self._num_nodes += 1
        return new_node_neighbors
    
def make_complete_graph(num_nodes):
        
    """
    creates a complete graph with num_nodes number of vertices
    input = number of nodes 
    output = a complete graph with input number of nodes
    """
    graph = dict()
    edge_set = set()
    for node in range(num_nodes):
        edge_set = set()
        for edge_node in range(num_nodes):
            if(node != edge_node):
                edge_set.add(edge_node)
        graph[node] = edge_set.copy()
    return graph

def upa(n,m):

    graph = make_complete_graph(m)
    up_inst = UPATrial(m)
    #print m,graph.values
    for dummy_var in range(m,n):
        new_node_neighbors = up_inst.run_trial(m)
        for new_node in new_node_neighbors:
            if( new_node not in graph):
                graph[new_node] = set()
            graph[new_node].add(dummy_var)
        graph[dummy_var] = new_node_neighbors
    return graph

def random_order(graph):
    
    node_list = graph.keys()
    random.shuffle(node_list)
    return node_list
   
##########################################################
# Code for loading computer network graph

NETWORK_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_rf7.txt"

def load_graph(graph_url):
    """
    Function that loads a graph given the URL
    for a text representation of the graph
    
    Returns a dictionary that models a graph
    """
    graph_file = urllib2.urlopen(graph_url)
    graph_text = graph_file.read()
    graph_lines = graph_text.split('\n')
    graph_lines = graph_lines[ : -1]
    
    print ("Loaded graph with",len(graph_lines), "nodes")
    
    answer_graph = {}
    for line in graph_lines:
        neighbors = line.split(' ')
        node = int(neighbors[0])
        answer_graph[node] = set([])
        for neighbor in neighbors[1 : -1]:
            answer_graph[node].add(int(neighbor))

    return answer_graph


graph_NW = load_graph(NETWORK_URL)
# what values of p will get us 3047 edges
graph_ER =  make_ER_graph(1239, 0.002)

def max_edges(graph):
    m = 0 
    for node in graph.keys():
        if ( len(graph[node]) > m  ):
            m = len(graph[node])
    return m

graph_UPA= upa(1239,3)

print max_edges(graph_NW)
print max_edges(graph_ER)
print max_edges(graph_UPA)

def avg_degree(graph):
    """
    computes avg out-degree of a given graph
    """
    summ = 0
    for node,edge_list in graph.items():
        summ += len(edge_list)
    #print summ
    return float(summ)/len(graph)

print avg_degree(graph_NW)
print avg_degree(graph_ER)
print avg_degree(graph_UPA)


def count_more_than_avg(graph, num):
    m = 0 
    for node in graph.keys():
        if ( len(graph[node]) > num  ):
            m +=1
    return m
    
print count_more_than_avg(graph_NW, 4.91)
print count_more_than_avg(graph_ER, 4.92)
print count_more_than_avg(graph_UPA, 5.94)

def edge_count(graph):
    m = 0 
    for node in graph.keys():
       m += len(graph[node])
    print "edges",m/2

#edge_count(graph_NW)
#edge_count(graph_ER)
#edge_count(graph_UPA)

def build_plot_random(graph1, graph2, graph3):
    """
    Build plot of the in degree distribution
    """

    attack_order1 = random_order(graph1)
    largest_cc_list1 = compute_resilience(graph1, attack_order1)
    attack_order2 = random_order(graph2)
    largest_cc_list2 = compute_resilience(graph2, attack_order2)
    attack_order3 = random_order(graph3)
    largest_cc_list3 = compute_resilience(graph3, attack_order3)
    assert len(attack_order1)==len(attack_order2)==len(attack_order3)
    
    plt.title('Connectivity of a network under random Cyber attack')
    plt.xlabel('Nodes Removed')
    plt.ylabel('Size of Largest CC')
    node_index_list = [dummy_var for dummy_var in range(0, len(attack_order3)+1)]
    plt.plot(node_index_list, largest_cc_list1, '-b', label='Example Computer Network Graph')
    plt.plot(node_index_list, largest_cc_list2, '-r', label='ER Graph p=0.002')
    plt.plot(node_index_list, largest_cc_list3, '-g', label='UPA Graph m=3')
    plt.legend(loc='upper right')
    plt.show()                                                    

#build_plot_random(copy_graph(graph_NW), copy_graph(graph_ER),copy_graph(graph_UPA))


def build_plot_targeted(graph1, graph2, graph3):
    """
    Build plot of the in degree distribution
    """

    attack_order1 = targeted_order(graph1)
    largest_cc_list1 = compute_resilience(graph1, attack_order1)
    attack_order2 = targeted_order(graph2)
    largest_cc_list2 = compute_resilience(graph2, attack_order2)
    attack_order3 = targeted_order(graph3)
    largest_cc_list3 = compute_resilience(graph3, attack_order3)
    assert len(attack_order1)==len(attack_order2)==len(attack_order3)
    
    plt.title('Connectivity of a network under Targeted Cyber attack')
    plt.xlabel('Nodes Removed')
    plt.ylabel('Size of Largest CC')
    node_index_list = [dummy_var for dummy_var in range(0, len(attack_order3)+1)]
    plt.plot(node_index_list, largest_cc_list1, '-b', label='Example Computer Network Graph')
    plt.plot(node_index_list, largest_cc_list2, '-r', label='ER Graph p=0.002')
    plt.plot(node_index_list, largest_cc_list3, '-g', label='UPA Graph m=3')
    plt.legend(loc='upper right')
    plt.show()                            

#build_plot_targeted(copy_graph(graph_NW), copy_graph(graph_ER),copy_graph(graph_UPA))
#assert targeted_order(graph_NW) == fast_targeted_order(graph_NW)
#print fast_targeted_order(graph_NW)
#print targeted_order(graph_NW)
c = set(targeted_order(graph_ER)).intersection(fast_targeted_order(graph_ER))
print "intersect",len(c) 
c = set(targeted_order(graph_NW)).intersection(fast_targeted_order(graph_NW))
print "intersect",len(c) 
c = set(targeted_order(graph_UPA)).intersection(fast_targeted_order(graph_UPA))
print "intersect",len(c) 
#assert targeted_order(graph_UPA) == fast_targeted_order(graph_UPA) 
#simpleplot.plot_lines("In-Degree Distribution", 600, 600, 
#                      "log (base e) of indegree", "log (base e) of frequency", [plot1], False,["nw_data", "er_data p:", "upa_data m:"])

import time  
m = 5   
x_list = []
y_list_target = []
y_list_fast_target = [] 
  
for dummy_var in range(10, 1000, 10):
    graph = upa(dummy_var, m)
    x_list.append(dummy_var)
    start = time.clock()
    targeted_order(graph)
    end_target = time.clock()-start
    y_list_target.append(end_target)
    start2 = time.clock()
    fast_targeted_order(graph)
    end_fast = time.clock()-start2
    y_list_fast_target.append(end_fast)

print y_list_target,

print "\n#################################\n"
print y_list_fast_target
plt.title('Desktop python 2.7 : Running Time as a function of nodes')
plt.xlabel('Nodes')
plt.ylabel('running time micro seconds')
plt.plot(x_list, y_list_target, '-b', label='targeted_order')
plt.plot(x_list, y_list_fast_target, '-r', label='fast_targeted_order')
plt.legend(loc='upper right')
plt.show()                       
    
    




