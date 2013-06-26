PythonForPicam
==============

A Python 2.7 Interface for PICAM Library
----------------------------------------

The interface can nominally be run by building Main.py

The interface uses the built in Python ctypes module.  The interface reads in 
a library, Picam.dll, provided by Princeton Instruments at 
ftp://ftp.princetoninstruments.com/Public/Software/Official/PICam/

Main.py is the main application.  When compiled, Main.py reads in external types 
defined in PiTypes.py and PiTypesMore.py as well as functions from PiFunctions.py.
PiParameterLookup.py is used to read in camera parameter values.  This is mainly 
a workaround to address the fact that Python ctypes does not have a built in enum 
class.  


2013 June 26 -- Initial Release
------------------------------
Main.py
PiTypes.py
PiTypesMore.py
PiFunctions.py
PiParameterLookup.py
