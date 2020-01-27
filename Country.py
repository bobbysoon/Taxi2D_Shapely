import geopandas as gpd

def Country(COUNTRY):
	world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
	wArea = world[world.name == COUNTRY]
	area = wArea.to_crs(epsg=3395)    # convert to World Mercator CRS
	if len(area):
		area_shape = area.iloc[0].geometry   # get the Polygon
		return area_shape
	else:
		print('"%s" returned None'%COUNTRY)
