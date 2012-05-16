/*
 *  Mover_c.h
 *  gnome
 *
 *  Created by Generic Programmer on 10/18/11.
 *  Copyright 2011 __MyCompanyName__. All rights reserved.
 *
 */

#ifndef __Mover_c__
#define __Mover_c__

#include "Earl.h"
#include "TypeDefs.h"
#include "Mover_b.h"
#include "ClassID/ClassID_c.h"
#include "RectUtils.h"

class Mover_c : virtual public Mover_b, virtual public ClassID_c {

public:
	
	virtual OSErr		AddUncertainty (long setIndex, long leIndex, VelocityRec *v) { return 0; }
	//virtual WorldPoint3D	GetMove (Seconds timeStep,long setIndex,long leIndex,LERec *theLE,LETYPE leType) {WorldPoint3D theLE3D = {(*theLE).p.pLat,(*theLE).p.pLong,(*theLE).z}; return theLE3D;}
	virtual WorldPoint3D	GetMove (Seconds timeStep,long setIndex,long leIndex,LERec *theLE,LETYPE leType); 
	
	virtual Boolean		VelocityStrAtPoint(WorldPoint3D wp, char *velStr) {return false;}
	virtual Boolean		IAmA3DMover() {return false;}
	virtual float		GetArrowDepth(){return 0.;}
	virtual LongPointHdl	GetPointsHdl(){return nil;}
	
	virtual OSErr		InitMover ();
	virtual OSErr		UpdateUncertainty(void);
	
};




#endif