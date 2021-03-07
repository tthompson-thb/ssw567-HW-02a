# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin


    def testIsATriangle(self): 
        self.assertEqual(classifyTriangle(3,4,0),'Not a triangle')
        
    def testRightTriangle(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testScaleneTriangle(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Scalene','5,3,4 is a Scalene triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 is a Equilateral triangle')
        
    def testIsocelesTriangles(self): 
        self.assertEqual(classifyTriangle(5,5,1),'Isosceles','5,1,5 is a Isosceles triangle')

if __name__ == '__main__':
    print('\nRunning unit tests')
    unittest.main()


