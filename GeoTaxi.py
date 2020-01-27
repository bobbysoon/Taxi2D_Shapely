#!/usr/bin/python3

from Taxi_Shapely import Taxi,sg

def flattenMultis(l):
	l = [l]
	i=0
	while i<len(l):
		if type(l[i]) is sg.multipolygon.MultiPolygon:
			l.extend(l.pop(i)[:])
		elif type(l[i]) is sg.collection.GeometryCollection:
			l.extend(l.pop(i)[:])
		elif type(l[i]) is list:
			l.extend(l.pop(i))
		elif type(l[i]) is sg.polygon.Polygon:
			if l[i].is_empty:
				l.pop(i)
			else:
				i+= 1
		else:
			print(type(l[i]))
			idk()
	
	return l

def GeoTaxi(country,centroids):
	taxiPolies = Taxi( centroids , country.bounds )
	
	tPolies = flattenMultis(taxiPolies)
	aPolies = flattenMultis(country)
	
	polies = []
	for tPoly in tPolies:
		for aPoly in aPolies:
			polies.extend( flattenMultis(aPoly.intersection(tPoly)) )
	
	return polies # list of shapely.geometry.Polygon
