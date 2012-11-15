"""
cython file used to store all the type info for GNOME.

Pulled from type_defs.pxi -- i.e pulled from C++ headers, etc.

"""

import cython

## pull stuff in from the C++ headers
from type_defs cimport *

def enum(**enums):
    """
    Just found a clever way to do enums in python
    """
    return type('Enum', (), enums)

"""
LE Status as an enum type
"""
oil_status =enum(not_released = OILSTAT_NOTRELEASED,
                 in_water = OILSTAT_INWATER,
                 on_land = OILSTAT_ONLAND,
                 off_maps = OILSTAT_OFFMAPS,
                 evaporated = OILSTAT_EVAPORATED)

"""
disperse status as an enum type
"""
disp_status = enum(dont_disperse = DONT_DISPERSE,
                   disperse = DISPERSE,
                   have_dispersed = HAVE_DISPERSED,
                   disperse_nat = DISPERSE_NAT,
                   have_dispersed_nat = HAVE_DISPERSED_NAT,
                   evaporate = EVAPORATE,
                   have_evaporated = HAVE_EVAPORATED,
                   remove = REMOVE,
                   have_removed = HAVE_REMOVED)

"""
SpillType {FORECAST_LE = 1, UNCERTAINTY_LE = 2};
"""
spill_type = enum(forecast = FORECAST_LE,
                  uncertainty = UNCERTAINTY_LE,)
                

"""
Contains enum type for the contents of a data file. For instance,
a standard wind file would contain magnitude and direction info
data_format.magnitude_direction = 5
"""
data_format = enum(magnitude_direction=M19MAGNITUDEDIRECTION,
                   cartesian_uv=M19REALREAL)

"""
Define units for velocity. In C++, these are #defined as
#define kKnots           1
#define kMetersPerSec    2
#define kMilesPerHour    3

TODO: In C++, these are user_units which are coupled with the GUI and the display.
Leave it in here for now - but the OSSMTimeValue_c and the cy_ossm_time expects long wind file format
and units are read from the file. For the time series case, the user_units are undefined

TODO: Leave velocity_units enum here. Currently, it is used in test_cy_ossm_time.py only
If we don't care about keeping these values consistent with C++, may want to remove this in future,
just to keep things simple.
"""
velocity_units = enum(undefined=-1, knots=1, meters_per_sec=2, miles_per_hour=3)

"""
Lets define error codes here as well, may want to 
group these under an ErrCodes class if it makes sense - but for now, let's see
how many error codes we get.
"""
err_codes = enum(undefined_units=1)
#class ErrCodes:
#    undefined = enum(units=1)
