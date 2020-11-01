import unittest
from main import *

class UnitTests(unittest.TestCase) :
      def test_statPower(self) : 
          psi4 = scipy.stats.norm.ppf(0.05)
          mdiff = 20 - sample
          for i in range(10) :
              xv = mdiff / ( 2 / np.sqrt(i+1) ) + psi4
              myval = scipy.stats.norm.cdf(xv)
              self.assertTrue( np.abs(statisticalPower(20, 2, sample, i+1)-myval)<1e-7, "Your statistical power function is not working" )
