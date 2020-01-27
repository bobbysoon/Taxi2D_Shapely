import numpy as np
from scipy.spatial import distance
import shapely.geometry as sg

def UniformPoints( N , country , nRandomSamples=32 ):
	pa= np.random.uniform(size=(1,2))
	while len(pa)<N:
		pb = np.random.uniform(size=(nRandomSamples,2))
		dists = distance.cdist(pb,pa, 'cityblock')
		dists = [min(dists[i]) for i in range(len(dists))]
		p = pb[dists.index(max(dists))]
		pa=np.append(pa,[p],axis=0)
	
	return pa

def Centroids(nCentroids, country, nRandomSamples=32 ):
	xMin,yMin,xMax,yMax = country.bounds
	xRng,yRng = xMax-xMin , yMax-yMin
	centroids = UniformPoints( nCentroids , country , nRandomSamples )
	centroids*= xRng,yRng
	centroids+= xMin,yMin
	centroids = list(map(tuple, centroids))
	return centroids

