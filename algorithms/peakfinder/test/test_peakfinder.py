
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

    def test_peakfind1(self):
        a = [1,2]
        self.assertEqual(peakfinder_1d(a), 2,
                "Wrong peak element")
        peak = peakfinder_1d(a)
        self.assertEqual(peak, 2,
                "Wrong peak element {0}; expected {1}".format(peak,2))

    def test_peakfind2(self):
        a = [1,2,3]
        self.assertEqual(peakfinder_1d(a), 3,
                "Wrong peak element")
        peak = peakfinder_1d(a)
        self.assertEqual(peak, 3,
                "Wrong peak element {0}; expected {1}".format(peak,3))

    def test_peakfind3(self):
        a = [3,2,1]
        self.assertEqual(peakfinder_1d(a), 3,
                "Wrong peak element")
        peak = peakfinder_1d(a)
        self.assertEqual(peak, 3,
                "Wrong peak element {0}; expected {1}".format(peak,3))

    def test_peakfind4(self):
        a = [1,2,3,4]
        self.assertEqual(peakfinder_1d(a), 4,
                "Wrong peak element")
        peak = peakfinder_1d(a)
        self.assertEqual(peak, 4,
                "Wrong peak element {0}; expected {1}".format(peak,4))

    def test_peakfind5(self):
        a = [4,3,2,1]
        self.assertEqual(peakfinder_1d(a), 4,
                "Wrong peak element")
        peak = peakfinder_1d(a)
        self.assertEqual(peak, 4,
                "Wrong peak element {0}; expected {1}".format(peak,4))

    def test_peakfind6(self):
        a = [-1,4,2,0]
        peak = peakfinder_1d(a)
        self.assertEqual(peak, 4,
                "Wrong peak element {0}; expected {1}".format(peak,4))

    def test_peakfind7(self):
        a = [-1,2,4,0]
        peak = peakfinder_1d(a)
        self.assertEqual(peak, 4,
                "Wrong peak element {0}; expected {1}".format(peak,4))

    def test_peakfind8(self):
        a = [-1,2,4,0,8,2]
        peak = peakfinder_1d(a)
        peaks = [4,8]
        self.assertIn(peak, peaks,
                "Wrong peak element {0}; expected {1}".format(peak,peaks))

    def test_peakfind9(self):
        a = [-1,2,4,0,8,2]
        a.reverse()
        peak = peakfinder_1d(a)
        peaks = [4,8]
        self.assertIn(peak, peaks,
                "Wrong peak element {0}; expected {1}".format(peak,peaks))

    def test_peakfind10(self):
        a = [10,3,2,0,5,-1,2,4,0,8,2]
        #a = [2,8,0,4,2,-1,5,0,2,3,10]
        a.reverse()
        peak = peakfinder_1d(a)
        peaks = [10,5,4,8]
        self.assertIn(peak, peaks,
                "Wrong peak element {0}; expected {1}".format(peak,peaks))

    def test_peakfind11(self):
        a = [10,3,2,0,5,-1,2,4,0,8,2]
        peak = peakfinder_1d(a)
        peaks = [10,5,4,8]
        self.assertIn(peak, peaks,
                "Wrong peak element {0}; expected {1}".format(peak,peaks))

if __name__ == "__main__":
    unittest.main()
    #suite = unittest.TestLoader().loadTestsFromTestCase(PeakFinder1DTestCase)
    #unittest.TextTestRunner(verbosity=2).run(suite)

