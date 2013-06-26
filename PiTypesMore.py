import ctypes as ctypes

from PiTypes import *

##### Some of the types defined dependent on an enum: PicamStringSize.  From picam.h we have the following:
"""
typedef enum PicamStringSize
{
    PicamStringSize_SensorName     =  64,
    PicamStringSize_SerialNumber   =  64,
    PicamStringSize_FirmwareName   =  64,
    PicamStringSize_FirmwareDetail = 256
} PicamStringSize;
"""
### Which is why I define the following:
PicamStringSize_SensorName = PicamStringSize_SerialNumber = PicamStringSize_FirmwareName = 64
PicamStringSize_FirmwareDetail = 256

"""
typedef struct PicamCameraID
{
    PicamModel          model;
    PicamComputerInterface computer_interface;
    pichar                 sensor_name[PicamStringSize_SensorName];
    pichar                 serial_number[PicamStringSize_SerialNumber];
} PicamCameraID;
"""
class PicamCameraID(ctypes.Structure):
    _fields_ = [("model", PicamModel),
                ("computer_interface", PicamComputerInterface),
                ("sensor_name", pichar * PicamStringSize_SensorName),
                ("serial_number", pichar * PicamStringSize_SerialNumber)]

# PicamHandle
PicamHandle = ctypes.c_void_p


# PicamFirmwareDetail
"""
typedef struct PicamFirmwareDetail
{
    pichar name[PicamStringSize_FirmwareName];
    pichar detail[PicamStringSize_FirmwareDetail];
} PicamFirmwareDetail;
"""

class PicamFirmwareDetail(ctypes.Structure):
    _fields_ = [("name", pichar * PicamStringSize_FirmwareName),
                ("detail", pichar * PicamStringSize_FirmwareDetail)]

##### Types defined on pp57-70 (chapter 4: Camera Parameter Values, Inofrmation, Constraints, and Commitment)
    ### Saving this for later!

##### Types defined on p76 (chapter 5: Camera Data Acquisition)

# PicamAvailableData
"""
typedef struct PicamAvailableData
{
    void* initial_readout;
    pi64s readout_count;
} PicamAvailableData;
"""
class PicamAvailableData(ctypes.Structure):
    _fields_ = [("initial_readout", ctypes.c_void_p), ("readout_count", pi64s)]

class PicamAvailableData2(ctypes.Structure):
    _fields_ = [ ( "initial_readout", ctypes.POINTER(type(ctypes.c_void_p()))), ("readout_count", pi64s)]

# PicamAcquisitionErrorsMask
"""
typedef enum PicamAcquisitionErrorsMask
{
    PicamAcquisitionErrorsMask_None           = 0x0,
    PicamAcquisitionErrorsMask_DataLost       = 0x1,
    PicamAcquisitionErrorsMask_ConnectionLost = 0x2
} PicamAcquisitionErrorsMask; /* (0x4) */
"""
PicamAcquisitionErrorsMask = ctypes.c_int

# PicamAcquisitionStatus
class PicamAcquisitionStatus(ctypes.Structure):
    _fields_ = [("running",pibln),
                ("errors",PicamAcquisitionErrorsMask),
                ("readout_rate",piflt)]

