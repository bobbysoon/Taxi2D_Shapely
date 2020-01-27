#!/usr/bin/python3

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection

import numpy as np

def MatPlot_GeoTaxi( polies , centroids=None ):
	patches = [Polygon(p.exterior.coords[:]) for p in polies]
	
	p = PatchCollection(patches, cmap=matplotlib.cm.jet, alpha=0.4)
	
	colors = 100*np.random.rand(len(patches))
	p.set_array(np.array(colors))
	
	fig, ax = plt.subplots()
	ax.add_collection(p)
	
	for p in polies:
		x,y = zip(*(p.exterior.coords[:]))
		ax.plot(x, y, alpha=0.7, linewidth=2, solid_capstyle='round')
	
	if centroids:
		plt.scatter(*zip(*centroids))
	
	plt.axis('scaled')
	plt.show()

if __name__ == '__main__':
	import sys
	args = sys.argv[1:]
	nCentroids = 128
	nRandomSamples = 4
	if not args:
		print(__file__,'<country> [nCentroids=128] [nRandomSamples=4]')
	else:
		country = args.pop(0)
		if args: nCentroids = int(args.pop(0))
		if args: nRandomSamples = int(args.pop(0))
		
		from Country import Country
		country = Country(country)
		if country:
			from Centroids import Centroids
			centroids = Centroids(nCentroids,country)
			
			from GeoTaxi import GeoTaxi
			polies = GeoTaxi(country,centroids)
			
			MatPlot_GeoTaxi( polies , centroids )
