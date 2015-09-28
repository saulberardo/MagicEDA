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

        # Very simple coordinates, choosen semi-randomly
        lat = pd.Series([41.2, 41.5, 41.1, 41.6, 42.2, 43.3, 42.5])
        lon = pd.Series([-2.2, -1.9, -1.4, -1.8, -0.5, -3.1, -3.6])

        # Colors
        color_idxs = [1, 5, 10, 3, 2, 7, 5]
        colors = plt.cm.get_cmap('rainbow', len(color_idxs))

        # Create an axe where to plot (it is not strictly necessary, but we want to test it here)
        fig, ax = plt.subplots()

        # Plot path
        geo.plot_path_from_above(lon, lat, color=colors(color_idxs), show_map=True, padding=2, aspect_ratio= 2./4, ax=ax)
        plt.show()

    def tearDown(self):
        gc.collect()


if __name__ == '__main__':
    unittest.main()
