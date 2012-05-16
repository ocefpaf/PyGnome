/*
 *  Map_b.h
 *  gnome
 *
 *  Created by Generic Programmer on 10/21/11.
 *  Copyright 2011 __MyCompanyName__. All rights reserved.
 *
 */

#ifndef __Map_b__
#define __Map_b__

#include "Basics.h"
#include "TypeDefs.h"
#include "ClassID_b.h"
#include "CMYLIST.H"

class Map_b : virtual public ClassID_b {

public:
	WorldRect			fMapBounds; 				// bounding rectangle of map
	CMyList				*moverList;					// list of this map's movers
	Boolean				bMoversOpen;				// movers list open (display)	
	float				fRefloatHalfLifeInHrs;	
	Boolean				bIAmPartOfACompoundMap;

};




#endif