"""
Test Case for module geo.py.
"""

import matplotlib.pyplot as plt
import pandas as pd
import unittest
import gc
from magikeda import geo


class GeoTestCase(unittest.TestCase):

    def test_plot_path_from_above(self):

        # Very simple coordinates, choosen same randomly
        lat = pd.Series([41.2, 41.1, 41.6, 42.2, 43.3, 42.5])
        lon = pd.Series([-2.2, -1.4, -1.8, -0.5, -3.1, -3.6])

        # Plot path
        geo.plot_path_from_above(lon, lat, show_map=True, padding=1, connect_points=True)
        plt.show()

    def tearDown(self):
        gc.collect()


if __name__ == '__main__':
    unittest.main()
