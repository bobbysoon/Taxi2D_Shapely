from geovoronoi import coords_to_points,points_to_coords

def Within(pts,shape):
	pts = coords_to_points(pts)
	pts = [p for p in pts if p.within(shape)]
	return [(x,y) for x,y in points_to_coords(pts)] 

