"""Test for talking to Picam"""
import ctypes as ctypes

""" Import standard type definitions from PiTypes.py """
from PiTypes import *

""" Import non-standard type definitions from PiTypesMore.py """
from PiTypesMore import *

""" Import function definitions from PiFunctions.py """
""" This should contian all of the function from picam.h """
from PiFunctions import *

""" Import parameter lookup from PiParameterLookup.py """
""" This file includes a function PI_V and a lookup table to return the code
    for different Picam Parameters described in chapter 4 """
from PiParameterLookup import *

############################
##### Custom Functions #####
############################
    
def pointer(x):
    """Returns a ctypes pointer"""
    ptr = ctypes.pointer(x)
    return ptr


def load(x):
    """Loads DLL library where argument is location of library"""
    x = ctypes.cdll.LoadLibrary(x)
    return x


#########################
##### Main Routine  #####
#########################

if __name__ == '__main__':

    """ Load the picam.dll """
    # picamDll = 'C:/Users/becgroup/Documents/Python/DriverTest/Princeton Instruments/Picam/Runtime/Picam.dll'
    picamDll = 'DLLs/Picam.dll'
    picam = load(picamDll)
    
    print 'Initialize Camera.',Picam_InitializeLibrary()
    print '\n'

    """ Print version of PICAM """
    major = piint()
    minor = piint()
    distribution = piint()
    release = piint()
    print 'Check Software Version. ',Picam_GetVersion(pointer(major),pointer(minor),pointer(distribution),pointer(release))
    print 'Picam Version ',major.value,'.',minor.value,'.',distribution.value,' Released: ',release.value
    print '\n'

    ## Test Routine to connect a demo camera
    ## p23
    print 'Preparing to connect Demo Camera'   
    model = ctypes.c_int(10)
    serial_number = ctypes.c_char_p('Demo Cam 1')
    PicamID = PicamCameraID()  
    """
    PICAM_API Picam_ConnectDemoCamera(
    PicamModel     model,
    const pichar*  serial_number,
    PicamCameraID* id );
    """
    print 'Demo camera connetcted with return value = ',Picam_ConnectDemoCamera(model, serial_number, pointer(PicamID))
    print '\n'
    
    print 'Camera model is ',PicamID.model
    print 'Camera computer interface is ',PicamID.computer_interface
    print 'Camera sensor_name is ', PicamID.sensor_name
    print 'Camera serial number is', PicamID.serial_number
    print '\n'

    ## Test routine to open first camera
    ## p20
    """
    PICAM_API Picam_OpenFirstCamera( PicamHandle* camera );
    """
    camera = PicamHandle()
    print 'Opening First Camera', Picam_OpenFirstCamera(ctypes.addressof(camera))


    ## Test routine to acquire image
    ## p73
    """
    PICAM_API Picam_Acquire(
    PicamHandle                 camera,
    pi64s                       readout_count,
    piint                       readout_time_out,
    PicamAvailableData*         available,
    PicamAcquisitionErrorsMask* errors );
    """
    readoutstride = piint(0);
    print "Getting readout stride. ", Picam_GetParameterIntegerValue( camera, ctypes.c_int(PicamParameter_ReadoutStride), ctypes.byref(readoutstride) );

    """
    Prototype
    PICAM_API Picam_Acquire(
    PicamHandle                 camera,
    pi64s                       readout_count,
    piint                       readout_time_out,
    PicamAvailableData*         available,
    PicamAcquisitionErrorsMask* errors );
    """

    """
    typedef struct PicamAvailableData
    {
        void* initial_readout;
        pi64s readout_count;
    } PicamAvailableData;
    """
    readout_count = pi64s(1)
    readout_time_out = piint(1000)
    available = PicamAvailableData()

    """ Print Debug Information on initial readout """
    print '\n'
    print "available.initial_readout: ",available.initial_readout
    print "Initial readout type is", type(available.initial_readout)
    errors = PicamAcquisitionErrorsMask()

    """
    Prototype
    PICAM_API Picam_Acquire(
    PicamHandle                 camera,
    pi64s                       readout_count,
    piint                       readout_time_out,
    PicamAvailableData*         available,
    PicamAcquisitionErrorsMask* errors );
    """
    Picam_Acquire.argtypes = PicamHandle, pi64s, piint, ctypes.POINTER(PicamAvailableData), ctypes.POINTER(PicamAcquisitionErrorsMask)
    Picam_Acquire.restype = piint
    
    print '\nAcquiring... ',Picam_Acquire(camera, readout_count, readout_time_out, ctypes.byref(available), ctypes.byref(errors))
    print '\n'

    print "available.initial_readout: ",available.initial_readout
    print "Initial readout type is", type(available.initial_readout)
    print '\n'
    
    """ Close out Library Resources """
    ## Disconnected the above cameras
    print 'Disconnecting demo camera', Picam_DisconnectDemoCamera(pointer(PicamID))
    ## Close down library    
    print 'Uninitializing',Picam_UninitializeLibrary()



    """ Test Routine to Access Data """
    
    """ Create an array type to hold 1024x1024 16bit integers """
    DataArrayType = pi16u*1048576

    """ Create pointer type for the above array type """
    DataArrayPointerType = ctypes.POINTER(pi16u*1048576)

    """ Create an instance of the pointer type, and point it to initial readout contents (memory address?) """
    DataPointer = ctypes.cast(available.initial_readout,DataArrayPointerType)


    """ Create a separate array with readout contents """
    data = DataPointer.contents


    """ Write contents of Data to binary file"""
    libc = ctypes.cdll.msvcrt
    fopen = libc.fopen
    fopen.argtypes = ctypes.c_char_p, ctypes.c_char_p
    fopen.restype = ctypes.c_void_p

    fwrite = libc.fwrite
    fwrite.argtypes = ctypes.c_void_p, ctypes.c_size_t, ctypes.c_size_t, ctypes.c_void_p
    fwrite.restype = ctypes.c_size_t

    fclose = libc.fclose
    fclose.argtypes = ctypes.c_void_p,
    fclose.restype = ctypes.c_int

    fp = fopen('PythonBinOutput.raw', 'wb')
    print 'fwrite returns: ',fwrite(data, readoutstride.value, 1, fp)

    fclose(fp)
