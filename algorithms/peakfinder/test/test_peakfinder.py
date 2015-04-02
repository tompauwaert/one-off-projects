
# Author: Tom Pauwaert
# Date: 2/4/2015
# Description: 
#    Testing the peakfinder methods. Both for 1D peakfinding
#    as for 2D peakfinding

# In order to allow us to import the actual module from a 
# different directory we must first add our application directory
# to the system path.
import os
import sys
sys.path.insert(0, os.path.abspath(".."))

import unittest
from peakfinder import peakfinder_1d

class PeakFinder1DTestCase(unittest.TestCase):

    def test_empty_list(self):
        self.assertRaises(ValueError, peakfinder_1d, [])

    def test_single_element_pos(self):
        self.assertEqual(peakfinder_1d([5]), 5, "Wrong peak detected")

    def test_single_element_neg(self):
        self.assertEqual(peakfinder_1d([-5]), -5, "Wrong peak detected")

    def test_equal_elements1(self):
        self.assertEqual(peakfinder_1d([3, 3]), 3, 
                "Wrong peak detected")

    def test_equal_elements2(self):
        self.assertEqual(peakfinder_1d([3, 3, 3]), 3, 
                "Wrong peak detected")

    def test_equal_elements3(self):
        self.assertEqual(peakfinder_1d([3 for _ in range(10)]), 3, 
                "Wrong peak detected")

    def test_equal_elements4(self):
        self.assertEqual(peakfinder_1d([3 for _ in range(11)]), 3, 
                "Wrong peak detected")

    def test_equal_elements5(self):
        self.assertEqual(peakfinder_1d([-356 for _ in range(100)]), -356, 
                "Wrong peak detected")

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(PeakFinder1DTestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)

