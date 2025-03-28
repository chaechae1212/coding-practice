from math import gcd 
def solution (dots):
	
	save=[[0, 1, 2, 3] , [0, 2, 1, 3], [0, 3, 1, 2]]
	
	for sav in save:

		dx = dots[sav[1]][0]-dots[sav[0]][0]
		dy=dots[sav[1]][1]-dots[sav[0]][1]
	
		dx2=dots[sav[3]][0]-dots[sav[2]][0]
		dy2=dots[sav[3]][1]-dots[sav[2]][1]
	    
		if (dx==0 and dy==0) or (dx2==0 and dy2==0):
				return 1
        
		f=gcd(dx, dy)
		s=gcd(dx2, dy2)
	
		dx=dx//f
		dy=dy//f
	
		dx2=dx2//s
		dy2=dy2//s
        
	
		if (dx == dx2 and dy == dy2) or (dx == -dx2 and dy == -dy2):
				return 1

	return 0
      
    
    
    