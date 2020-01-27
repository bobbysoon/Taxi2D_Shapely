#!/usr/bin/python

import shapely.geometry as sg
import shapely.ops as ops

from scipy.spatial import distance

def mDist(p1,p2):
	return abs(p2[0]-p1[0])+abs(p2[1]-p1[1])

epsilon=1e-04

def RegionsAt(p,pa):
	dists = distance.cdist([p],pa, 'cityblock')[0]
	dists = sorted(zip(dists,pa),key=lambda x:x[0])
	i=1
	while dists[i+1][0]-dists[i][0]<epsilon:
		i+= 1
	dists,pa = zip(*dists)
	return pa[:i]

from TaxiPP import TaxiPP

def _rSide(r,o,s):
	if len(s)==2:
		m1,m2 = s
		p = sg.Point(*r)
		if p.within(m1): return m1
		if p.within(m2): return m2

def rSide(r,o,s):
	if len(s)==2:
		m1,m2 = s
		if len(m1.exterior.coords)>len(m2.exterior.coords):
			m2,m1 = m1,m2
		
		for v in m1.exterior.coords:
			d = mDist(v,o)-mDist(v,r)
			if d>epsilon:
				return m1
			elif -d>epsilon:
				return m2

def NearestFirst(p,pa):
	dists = distance.cdist([p],pa, 'cityblock')[0]
	dists = sorted(zip(dists,pa),key=lambda x:x[0])
	dists,pa = zip(*dists)
	return pa

def Taxi(centroids,minMaxXY):
	vertRegions = dict()
	polies = list()
	for c in centroids:
		mesh = sg.box(*minMaxXY)
		others = list(set(centroids)-{c})
		for other in NearestFirst(c,others):
			pp = sg.LineString(TaxiPP(c,other,minMaxXY))
			r = rSide(c,other,ops.split(mesh,pp))
			if r: mesh=r
			
			finished = True
			for p in mesh.exterior.coords:
				if not p in vertRegions:
					vertRegions[p] = RegionsAt(p,centroids)
				if len(vertRegions[p])==1: finished = False
			if finished:
				break
				# region mesh verts are all bordering 2 or 3 regions
		
		if mesh.is_empty: oopes()
		polies.append( mesh )
	
	# remove invalid verts
	#vertRegions = {v:vertRegions[v] for v in vertRegions if len(vertRegions[v])>1}
	
	return polies

