# MagikEDA
MagikEDA is a python library which provides a set of functions to create graphs meant to be useful in Exploratory Data Analysis (EDA). It is conceived to be at one layer above libraries such as Pandas and Basemap. For now it is nothing more than a crude collection of some functions I needed to create in the last few months and decided to move to a public repository;

# Features

There are currently three packages available. The packages `univar` and `bivar` have functions for plotting one and two variables, respectively. The package `geo` has functions for calculating distances and plotting maps. The functions included are able of executing the following:

* Plotting a "data frame profile", which consists in a figure having one subplot for each variable in the dataset. Each subplot shows the variable distribution (histograms for numeric variables and bar charts for categorical).
* Plotting scatter plots with a tip box that is shown when points are hovered.
* Function to add an additional x axis bellow a figure.
* Function to compute the distance between a point and a segment (composed by two points).
* Function to plot a path (composed by a list o coordinates) over a map (the function automattically chooses a viewpoint to show the path (optionally with a padding)).

# Documentation

For documentation, see:
http://magikeda.readthedocs.org/en/latest/
