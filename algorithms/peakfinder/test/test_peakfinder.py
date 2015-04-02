
# Author: Tom Pauwaert
# Date: 2/4/2015
# Description: 
#    Testing the peakfinder methods. Both for 1D peakfinding
#    as for 2D peakfinding

# In order to allow us to import the actual module from a 
# different directory we must first add our application directory
# to the system path.
import sys
sys.path.append("~/work/dev/one-off-projects/algorithms/peakfinder")

import unittest
from .. import peakfinder

class PeakFinder1DTestCase(unittest.TestCase):

    def test_dummy(self):
        self.assertEqual(True, True)



if __name__ == "__main__":
    unittest.main()

