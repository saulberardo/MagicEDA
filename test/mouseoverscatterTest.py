"""
Test Case for module mouseoverscatter.py.
"""

import matplotlib.pyplot as plt
import pandas as pd
import unittest

from magikeda import bivar

class MouseoverscatterTestCase(unittest.TestCase):

    def test_(selfself):

        # Plota the mouse over scatter with some points
        bivar.plot_mouse_over_scatter([0, 1.5, 2, 2.5], [0, 1.5, 2, 3], ['Message %s'%i for i in [1,2,3, 4]], c=['r','r','b','g'])

if __name__ == '__main__':
    unittest.main()
