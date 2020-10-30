import unittest
import scipy.stats as st
from main import *

class UnitTests(unittest.TestCase) :
    def test_function(self) : 
        for a in range(-2,3) : 
            for b in range(3,10) :
                mean=0
                for i in range(100) : 
                    var = uniform_discrete(a,b)
                    self.assertTrue( np.fabs( np.floor(var) - var)<1e-7, "your discrete random variable has a non-integer value" )
                    self.assertTrue( var>=a and var<=b, "your discrete random variable is not between a and b" )
                    mean = mean + var
                mean = mean / 100
                var = 1/12*( (b-a+1)*(b-a+1) - 1 )
                bar = np.sqrt(var/100)*st.norm.ppf( (0.99 + 1) / 2 )
                self.assertTrue( np.fabs( mean - 0.5*(b+a) )<bar, "you appear to be sampling from the wrong distribution" )
