import numpy as np

def CrossingsTest( pgon, (tx, ty) ):
    """
    Point in polygon test using the "Crossings" algorithm.
    
    CrossingsTest(pgon, (tx, ty))
    
    pgon is an NX2 numpy array of points (or something that can be turned into one)
    
    (tx, ty) is the coords of the point to check
        
    translated from C code from "Graphics Gems"
    
    This could be compiled with cython nicely
    
    Note: This code will ignore the last point if the first and last points
          are the same.
    
    """
    # make it a numpy array if it isn't one
    pgon = np.asarray(pgon)
    
    if pgon[0,0] == pgon[-1,0] and pgon[0,1] == pgon[-1,1]:
        # first and last points are the same, so ignore the last point
        numverts = len(pgon) - 1
    else:
        numverts = len(pgon)
    vtx0 = pgon[numverts-1] # the last vertex
    # get test bit for above/below X axis 
    yflag0 = ( vtx0[1] >= ty )
    vtx1 = pgon[0]
    inside_flag = False
    for j in xrange(numverts):
        vtx1 = pgon[j]
        yflag1 = ( vtx1[1] >= ty ) 
        #check if endpoints straddle (are on opposite sides) of X axis
        #(i.e. the Y's differ); if so, +X ray could intersect this edge.
        if ( yflag0 != yflag1 ):
            xflag0 = ( vtx0[0] >= tx )
            # check if endpoints are on same side of the Y axis (i.e. X's
            # are the same); if so, it's easy to test if edge hits or misses.
            if ( xflag0 == ( vtx1[0] >= tx ) ) :
                # if edge's X values both right of the point, must hit
                if ( xflag0 ):
                    inside_flag = not inside_flag 
            else:
                # compute intersection of pgon segment with +X ray, note
                # if >= point's X; if so, the ray hits it.
                if ( (vtx1[0] - (vtx1[1]-ty)* ( vtx0[0]-vtx1[0])/(vtx0[1]-vtx1[1])) >= tx ):
                    inside_flag = not inside_flag 
        # move to next pair of vertices, retaining info as possible
        yflag0 = yflag1
        vtx0 = vtx1
    return inside_flag








