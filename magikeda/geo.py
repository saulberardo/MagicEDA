# -*- coding: utf-8 -*-
"""
Functions to plot maps and coordinates.

"""


from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
import gc

import pandas as pd


def plot_path_from_above(lon, lat, padding=2., show_map=True, color='red', connect_points=False):
    """

    Parameters
    ----------
        lon : pd.Series
            Series containing the list of longitudes.

        lat : pd.Series
            Series containing the list of latitudes.

        padding : float
            Space to add arond path (in degrees). Default is 2 degrees.

        show_map : boolean
            Wheter to draw the map around the path. Default is True.

        color : color
            The color of the path. Default is red.

        connect_points : float
            Wheter to connect the dots composing the path.

    """

    # Determine min and max longitude and latitude and add padding around them
    min_lat = lat.min() - padding
    max_lat = lat.max() + padding
    min_lon = lon.min() - padding
    max_lon = lon.max() + padding

    # Create map centered around the path
    m = Basemap(projection='merc',
        resolution = 'l', area_thresh = 0.1,
        llcrnrlon= min_lon,
        urcrnrlon= max_lon,
        llcrnrlat= min_lat,
        urcrnrlat= min_lat + np.abs(max_lon - min_lon)*3/4
    )

    # Draw map, is specified
    if show_map:

        # Draw paralles and meridians
        m.drawparallels(np.arange(-80.,81.,2.))
        m.drawmeridians(np.arange(-180.,181.,2.))

        # Draw relief and rivers
        m.shadedrelief()
        m.drawrivers()

    # Draw path
    if connect_points:
        m.plot(lon.values, lat.values, latlon=True, color=color)
    else:
        m.scatter(lon.values, lat.values, latlon=True, color=color)

    gc.collect()

if __name__=='__main__':

    pass

