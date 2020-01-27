#!/usr/bin/python

TPP_LDict = {
		(-1,-1): ( 1.0,-1.0),
		(-1, 1): (-1.0,-1.0),
		( 1, 1): (-1.0, 1.0),
		( 1,-1): ( 1.0, 1.0),
		( 1, 0): ( 0.0, 1.0),
		( 0, 1): (-1.0, 0.0),
		(-1, 0): ( 0.0,-1.0),
		( 0,-1): ( 1.0, 0.0)
	}

def TaxiPP(c1,c2,minMaxXY):
		xMin,yMin , xMax,yMax = minMaxXY
		xRng = xMax-xMin
		yRng = yMax-yMin
		
		x1,y1 = c1 ; x2,y2=c2
		cx,cy = (x1+x2)/2.0 , (y1+y2)/2.0
		
		dx,dy = x2-x1 , y2-y1
		if dx or dy:
			
			ax,ay = abs(dx),abs(dy)
			sx = -1.0 if dx<0.0 else 1.0 if dx>0.0 else 0.0
			sy = -1.0 if dy<0.0 else 1.0 if dy>0.0 else 0.0
			s = int(sx),int(sy)
			# s is perp plane's normal, at center
			
			# ldx,ldy = 90 degrees right of sx,sy
			# ldx,ldy is also drawn line's direction, at center
			ldx,ldy = TPP_LDict[s]
			
			l= min(ax,ay)/2.0
			
			if ax==ay or not (sx and sy): # infinite line
				p0 = None
				p1 = cx-xRng*ldx , cy-yRng*ldy
				p2 = cx+xRng*ldx , cy+yRng*ldy
			else: # ray-seg-ray
				p1 = cx-l*ldx , cy-l*ldy
				p2 = cx+l*ldx , cy+l*ldy
				if ax<ay:
					p0 = cx-xRng*ldx , cy-l*ldy
					p3 = cx+xRng*ldx , cy+l*ldy
				elif ax>ay:
					p0 = cx-l*ldx , cy-yRng*ldy
					p3 = cx+l*ldx , cy+yRng*ldy
			
			points = [p0,p1,p2,p3] if p0 else [p1,p2]
			
		else:
			points = []
		
		return points

