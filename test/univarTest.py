"""
Test Case for module univar.py
"""

import unittest
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from magikeda import univar


class UnivarTestCase(unittest.TestCase):

    def test_plot_bar_chart(self):

        # Test series with categorical data
        d1 = pd.Series(pd.Categorical(['c', 'a', 'c', 'a', 'c', 'b'], ['c', 'b', 'a']))
        univar.plot_bar_chart(d1)

        # Test series with string data
        d2 = pd.Series(['b', 'b', 'b', 'a', 'b', 'c'])
        univar.plot_bar_chart(d2)

        # Test both series at the same time
        univar.plot_bar_chart([d1, d2])

    def test_dataframe_profile(self):

        # Plot a simple data frame with two categorical variables and one numerical
        d1 = pd.Series(pd.Categorical(['c', 'a', 'c', 'a', 'c', 'b'], ['c', 'b', 'a']))
        d2 = pd.Series(['b', 'b', 'b', 'a', 'b', 'c'])
        d3 = pd.Series(np.random.rand(6))
        univar.plot_dataframe_profile(
            pd.DataFrame({'Var 1': d1, 'Var 2': d2, 'Var 3': d3}),
            default_ylabel='Time (%)',
            ylabels={'Var 1': 'Label of Var 1'},
            default_xlabel='State',
            xlabels={'Var 2': 'X lable of Var 2'}
        )

    def test_add_extra_xaxis(self):

        # Create a new figure
        f, _ = plt.subplots()

        # Plota a curve
        plt.plot([1,2,3,2,5])

        # Add a new xaxis
        univar.add_extra_xaxis(f, [1,4],['a','b'])



    def setUp(self):
        # Disable auto-plotting
        plt.ioff()

    def tearDown(self):
        # Close all figures created (probably it is not necessary)
        plt.close('all')


if __name__ == '__main__':
    unittest.main()
