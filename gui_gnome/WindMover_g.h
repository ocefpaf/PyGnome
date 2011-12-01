#ifndef __WindMover_g__
#define __WindMover_g__

#include "Earl.h"
#include "TypeDefs.h"
#include "WindSettings.h"
#include "WindMover_b.h"
#include "Mover_g.h"

class TWindMover;

class WindMover_g : virtual public WindMover_b, virtual public Mover_g {
	
public:
	virtual ClassID 	GetClassID () { return TYPE_WINDMOVER; }
	virtual Boolean		IAm(ClassID id) { if(id==TYPE_WINDMOVER) return TRUE; return Mover_g::IAm(id); }
	virtual OSErr		MakeClone(TWindMover **clonePtrPtr);
	virtual OSErr		BecomeClone(TWindMover *clone);
	// I/O methods
	virtual OSErr 		Read (BFPB *bfpb);  // read from current position
	virtual OSErr 		Write (BFPB *bfpb); // write to  current position
	
	// list display methods
	virtual long		GetListLength ();
	virtual ListItem 	GetNthListItem (long n, short indent, short *style, char *text);
	virtual Boolean 	ListClick (ListItem item, Boolean inBullet, Boolean doubleClick);
	virtual Boolean 	FunctionEnabled (ListItem item, short buttonID);
	//		virtual OSErr 		AddItem (ListItem item);
	virtual OSErr		SettingsItem (ListItem item);
	virtual OSErr 		DeleteItem (ListItem item);

	void 				DrawWindVector(Rect r, WorldRect view);
	void				GetFileName(char* fileName) ;
	virtual OSErr 		CheckAndPassOnMessage(TModelMessage *message);
	OSErr 				ExportVariableWind(char* path);

};

#endif