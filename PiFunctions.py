import ctypes as ctypes
picamDll = 'DLLs/Picam.dll'
picam = ctypes.cdll.LoadLibrary(picamDll)


    
### Begin imported Functions

def Picam_GetVersion(major, minor, distribution, released):
	""" PICAM_API Picam_GetVersion( piint* major, piint* minor, piint* distribution, piint* released) """
	err = picam.Picam_GetVersion( major, minor, distribution, released)
	err = ReturnPicamError(err)
	return err

def Picam_IsLibraryInitialized(inited):
	""" PICAM_API Picam_IsLibraryInitialized( pibln* inited ) """
	err = picam.Picam_IsLibraryInitialized(inited)
	err = ReturnPicamError(err)
	return err

def Picam_InitializeLibrary():
	""" PICAM_API Picam_InitializeLibrary( void ) """
	err = picam.Picam_InitializeLibrary()
	err = ReturnPicamError(err)
	return err

def Picam_UninitializeLibrary():
    """ PICAM_API Picam_UninitializeLibrary( void ) """
    err = picam.Picam_UninitializeLibrary()
    err = ReturnPicamError(err)
    return err

def Picam_DestroyString(s):
    """ PICAM_API Picam_DestroyString( const pichar* s ) """
    err = picam.Picam_DestroyString(s)
    err = ReturnPicamError(err)
    return err

def Picam_GetEnumerationString(type, value, s):
	""" PICAM_API Picam_GetEnumerationString( PicamEnumeratedType type, piint value, const pichar** s) """
	err = picam.Picam_GetEnumerationString( type, value, s)
	err = ReturnPicamError(err)
	return err

def Picam_DestroyCameraIDs(id_array):
	""" PICAM_API Picam_DestroyCameraIDs( const PicamCameraID* id_array ) """
	err = picam.Picam_DestroyCameraIDs(id_array)
	err = ReturnPicamError(err)
	return err

def Picam_GetAvailableCameraIDs(id_array, id_count):
	""" PICAM_API Picam_GetAvailableCameraIDs( const PicamCameraID** id_array, piint* id_count) """
	err = picam.Picam_GetAvailableCameraIDs( id_array, id_count)
	err = ReturnPicamError(err)
	return err

def Picam_GetUnavailableCameraIDs(id_array, id_count):
	""" PICAM_API Picam_GetUnavailableCameraIDs( const PicamCameraID** id_array, piint* id_count) """
	err = picam.Picam_GetUnavailableCameraIDs( id_array, id_count)
	err = ReturnPicamError(err)
	return err

def Picam_IsCameraIDConnected(id, connected):
	""" PICAM_API Picam_IsCameraIDConnected( const PicamCameraID* id, pibln* connected) """
	err = picam.Picam_IsCameraIDConnected( id, connected)
	err = ReturnPicamError(err)
	return err

def Picam_IsCameraIDOpenElsewhere(id, open_elsewhere):
	""" PICAM_API Picam_IsCameraIDOpenElsewhere( const PicamCameraID* id, pibln* open_elsewhere) """
	err = picam.Picam_IsCameraIDOpenElsewhere( id, open_elsewhere)
	err = ReturnPicamError(err)
	return err

def Picam_DestroyHandles(handle_array):
	""" PICAM_API Picam_DestroyHandles( const PicamHandle* handle_array ) """
	err = picam.Picam_DestroyHandles(handle_array)
	err = ReturnPicamError(err)
	return err

def Picam_OpenFirstCamera(camera):
	""" PICAM_API Picam_OpenFirstCamera( PicamHandle* camera ) """
	err = picam.Picam_OpenFirstCamera(camera)
	err = ReturnPicamError(err)
	return err

def Picam_OpenCamera(id, camera):
	""" PICAM_API Picam_OpenCamera( const PicamCameraID* id, PicamHandle* camera) """
	err = picam.Picam_OpenCamera( id, camera)
	err = ReturnPicamError(err)
	return err

def Picam_CloseCamera(camera):
	""" PICAM_API Picam_CloseCamera( PicamHandle camera ) """
	err = picam.Picam_CloseCamera(camera)
	err = ReturnPicamError(err)
	return err

def Picam_GetOpenCameras(camera_array, camera_count):
	""" PICAM_API Picam_GetOpenCameras( const PicamHandle** camera_array, piint* camera_count) """
	err = picam.Picam_GetOpenCameras( camera_array, camera_count)
	err = ReturnPicamError(err)
	return err

def Picam_IsCameraConnected(camera, connected):
	""" PICAM_API Picam_IsCameraConnected( PicamHandle camera, pibln* connected) """
	err = picam.Picam_IsCameraConnected( camera, connected)
	err = ReturnPicamError(err)
	return err

def Picam_GetCameraID(camera, id):
	""" PICAM_API Picam_GetCameraID( PicamHandle camera, PicamCameraID* id) """
	err = picam.Picam_GetCameraID( camera, id)
	err = ReturnPicamError(err)
	return err

def Picam_DestroyFirmwareDetails(firmware_array):
	""" PICAM_API Picam_DestroyFirmwareDetails( const PicamFirmwareDetail* firmware_array) """
	err = picam.Picam_DestroyFirmwareDetails( firmware_array)
	err = ReturnPicamError(err)
	return err

def Picam_GetFirmwareDetails(id, firmware_array, firmware_count):
	""" PICAM_API Picam_GetFirmwareDetails( const PicamCameraID* id, const PicamFirmwareDetail** firmware_array, piint* firmware_count) """
	err = picam.Picam_GetFirmwareDetails( id, firmware_array, firmware_count)
	err = ReturnPicamError(err)
	return err

def Picam_DestroyModels(model_array):
	""" PICAM_API Picam_DestroyModels( const PicamModel* model_array ) """
	err = picam.Picam_DestroyModels(model_array)
	err = ReturnPicamError(err)
	return err

def Picam_GetAvailableDemoCameraModels(model_array, model_count):
	""" PICAM_API Picam_GetAvailableDemoCameraModels( const PicamModel** model_array, piint* model_count) """
	err = picam.Picam_GetAvailableDemoCameraModels( model_array, model_count)
	err = ReturnPicamError(err)
	return err

def Picam_ConnectDemoCamera(model, serial_number, id):
	""" PICAM_API Picam_ConnectDemoCamera( PicamModel model, const pichar* serial_number, PicamCameraID* id) """
	err = picam.Picam_ConnectDemoCamera( model, serial_number, id)
	err = ReturnPicamError(err)
	return err

def Picam_DisconnectDemoCamera(id):
	""" PICAM_API Picam_DisconnectDemoCamera( const PicamCameraID* id ) """
	err = picam.Picam_DisconnectDemoCamera(id)
	err = ReturnPicamError(err)
	return err

def Picam_IsDemoCamera(id, demo):
	""" PICAM_API Picam_IsDemoCamera( const PicamCameraID* id, pibln* demo) """
	err = picam.Picam_IsDemoCamera( id, demo)
	err = ReturnPicamError(err)
	return err

def Picam_GetParameterIntegerValue(camera, parameter, value):
	""" PICAM_API Picam_GetParameterIntegerValue( PicamHandle camera, PicamParameter parameter, piint* value) """
	err = picam.Picam_GetParameterIntegerValue( camera, parameter, value)
	err = ReturnPicamError(err)
	return err

def Picam_SetParameterIntegerValue(camera, parameter, value):
	""" PICAM_API Picam_SetParameterIntegerValue( PicamHandle camera, PicamParameter parameter, piint value) """
	err = picam.Picam_SetParameterIntegerValue( camera, parameter, value)
	err = ReturnPicamError(err)
	return err

def Picam_CanSetParameterIntegerValue(camera, parameter, value, settable):
	""" PICAM_API Picam_CanSetParameterIntegerValue( PicamHandle camera, PicamParameter parameter, piint value, pibln* settable) """
	err = picam.Picam_CanSetParameterIntegerValue( camera, parameter, value, settable)
	err = ReturnPicamError(err)
	return err

def Picam_GetParameterLargeIntegerValue(camera, parameter, value):
	""" PICAM_API Picam_GetParameterLargeIntegerValue( PicamHandle camera, PicamParameter parameter, pi64s* value) """
	err = picam.Picam_GetParameterLargeIntegerValue( camera, parameter, value)
	err = ReturnPicamError(err)
	return err

def Picam_SetParameterLargeIntegerValue(camera, parameter, value):
	""" PICAM_API Picam_SetParameterLargeIntegerValue( PicamHandle camera, PicamParameter parameter, pi64s value) """
	err = picam.Picam_SetParameterLargeIntegerValue( camera, parameter, value)
	err = ReturnPicamError(err)
	return err

def Picam_CanSetParameterLargeIntegerValue(camera, parameter, value, settable):
	""" PICAM_API Picam_CanSetParameterLargeIntegerValue( PicamHandle camera, PicamParameter parameter, pi64s value, pibln* settable) """
	err = picam.Picam_CanSetParameterLargeIntegerValue( camera, parameter, value, settable)
	err = ReturnPicamError(err)
	return err

def Picam_GetParameterFloatingPointValue(camera, parameter, value):
	""" PICAM_API Picam_GetParameterFloatingPointValue( PicamHandle camera, PicamParameter parameter, piflt* value) """
	err = picam.Picam_GetParameterFloatingPointValue( camera, parameter, value)
	err = ReturnPicamError(err)
	return err

def Picam_SetParameterFloatingPointValue(camera, parameter, value):
	""" PICAM_API Picam_SetParameterFloatingPointValue( PicamHandle camera, PicamParameter parameter, piflt value) """
	err = picam.Picam_SetParameterFloatingPointValue( camera, parameter, value)
	err = ReturnPicamError(err)
	return err

def Picam_CanSetParameterFloatingPointValue(camera, parameter, value, settable):
	""" PICAM_API Picam_CanSetParameterFloatingPointValue( PicamHandle camera, PicamParameter parameter, piflt value, pibln* settable) """
	err = picam.Picam_CanSetParameterFloatingPointValue( camera, parameter, value, settable)
	err = ReturnPicamError(err)
	return err

def Picam_DestroyRois(rois):
	""" PICAM_API Picam_DestroyRois( const PicamRois* rois ) """
	err = picam.Picam_DestroyRois(rois)
	err = ReturnPicamError(err)
	return err

def Picam_GetParameterRoisValue(camera, parameter, value):
	""" PICAM_API Picam_GetParameterRoisValue( PicamHandle camera, PicamParameter parameter, const PicamRois** value) """
	err = picam.Picam_GetParameterRoisValue( camera, parameter, value)
	err = ReturnPicamError(err)
	return err

def Picam_SetParameterRoisValue(camera, parameter, value):
	""" PICAM_API Picam_SetParameterRoisValue( PicamHandle camera, PicamParameter parameter, const PicamRois* value) """
	err = picam.Picam_SetParameterRoisValue( camera, parameter, value)
	err = ReturnPicamError(err)
	return err

def Picam_CanSetParameterRoisValue(camera, parameter, value, settable):
	""" PICAM_API Picam_CanSetParameterRoisValue( PicamHandle camera, PicamParameter parameter, const PicamRois* value, pibln* settable) """
	err = picam.Picam_CanSetParameterRoisValue( camera, parameter, value, settable)
	err = ReturnPicamError(err)
	return err

def Picam_DestroyPulses(pulses):
	""" PICAM_API Picam_DestroyPulses( const PicamPulse* pulses ) """
	err = picam.Picam_DestroyPulses(pulses)
	err = ReturnPicamError(err)
	return err

def Picam_GetParameterPulseValue(camera, parameter, value):
	""" PICAM_API Picam_GetParameterPulseValue( PicamHandle camera, PicamParameter parameter, const PicamPulse** value) """
	err = picam.Picam_GetParameterPulseValue( camera, parameter, value)
	err = ReturnPicamError(err)
	return err

def Picam_SetParameterPulseValue(camera, parameter, value):
	""" PICAM_API Picam_SetParameterPulseValue( PicamHandle camera, PicamParameter parameter, const PicamPulse* value) """
	err = picam.Picam_SetParameterPulseValue( camera, parameter, value)
	err = ReturnPicamError(err)
	return err

def Picam_CanSetParameterPulseValue(camera, parameter, value, settable):
	""" PICAM_API Picam_CanSetParameterPulseValue( PicamHandle camera, PicamParameter parameter, const PicamPulse* value, pibln* settable) """
	err = picam.Picam_CanSetParameterPulseValue( camera, parameter, value, settable)
	err = ReturnPicamError(err)
	return err

def Picam_DestroyModulations(modulations):
	""" PICAM_API Picam_DestroyModulations( const PicamModulations* modulations ) """
	err = picam.Picam_DestroyModulations(modulations)
	err = ReturnPicamError(err)
	return err

def Picam_GetParameterModulationsValue(camera, parameter, value):
	""" PICAM_API Picam_GetParameterModulationsValue( PicamHandle camera, PicamParameter parameter, const PicamModulations** value) """
	err = picam.Picam_GetParameterModulationsValue( camera, parameter, value)
	err = ReturnPicamError(err)
	return err

def Picam_SetParameterModulationsValue(camera, parameter, value):
	""" PICAM_API Picam_SetParameterModulationsValue( PicamHandle camera, PicamParameter parameter, const PicamModulations* value) """
	err = picam.Picam_SetParameterModulationsValue( camera, parameter, value)
	err = ReturnPicamError(err)
	return err

def Picam_CanSetParameterModulationsValue(camera, parameter, value, settable):
	""" PICAM_API Picam_CanSetParameterModulationsValue( PicamHandle camera, PicamParameter parameter, const PicamModulations* value, pibln* settable) """
	err = picam.Picam_CanSetParameterModulationsValue( camera, parameter, value, settable)
	err = ReturnPicamError(err)
	return err

def Picam_GetParameterIntegerDefaultValue(camera, parameter, value):
	""" PICAM_API Picam_GetParameterIntegerDefaultValue( PicamHandle camera, PicamParameter parameter, piint* value) """
	err = picam.Picam_GetParameterIntegerDefaultValue( camera, parameter, value)
	err = ReturnPicamError(err)
	return err

def Picam_GetParameterLargeIntegerDefaultValue(camera, parameter, value):
	""" PICAM_API Picam_GetParameterLargeIntegerDefaultValue( PicamHandle camera, PicamParameter parameter, pi64s* value) """
	err = picam.Picam_GetParameterLargeIntegerDefaultValue( camera, parameter, value)
	err = ReturnPicamError(err)
	return err

def Picam_GetParameterFloatingPointDefaultValue(camera, parameter, value):
	""" PICAM_API Picam_GetParameterFloatingPointDefaultValue( PicamHandle camera, PicamParameter parameter, piflt* value) """
	err = picam.Picam_GetParameterFloatingPointDefaultValue( camera, parameter, value)
	err = ReturnPicamError(err)
	return err

def Picam_GetParameterRoisDefaultValue(camera, parameter, value):
	""" PICAM_API Picam_GetParameterRoisDefaultValue( PicamHandle camera, PicamParameter parameter, const PicamRois** value) """
	err = picam.Picam_GetParameterRoisDefaultValue( camera, parameter, value)
	err = ReturnPicamError(err)
	return err

def Picam_GetParameterPulseDefaultValue(camera, parameter, value):
	""" PICAM_API Picam_GetParameterPulseDefaultValue( PicamHandle camera, PicamParameter parameter, const PicamPulse** value) """
	err = picam.Picam_GetParameterPulseDefaultValue( camera, parameter, value)
	err = ReturnPicamError(err)
	return err

def Picam_GetParameterModulationsDefaultValue(camera, parameter, value):
	""" PICAM_API Picam_GetParameterModulationsDefaultValue( PicamHandle camera, PicamParameter parameter, const PicamModulations** value) """
	err = picam.Picam_GetParameterModulationsDefaultValue( camera, parameter, value)
	err = ReturnPicamError(err)
	return err

def Picam_CanSetParameterOnline(camera, parameter, onlineable):
	""" PICAM_API Picam_CanSetParameterOnline( PicamHandle camera, PicamParameter parameter, pibln* onlineable) """
	err = picam.Picam_CanSetParameterOnline( camera, parameter, onlineable)
	err = ReturnPicamError(err)
	return err

def Picam_SetParameterIntegerValueOnline(camera, parameter, value):
	""" PICAM_API Picam_SetParameterIntegerValueOnline( PicamHandle camera, PicamParameter parameter, piint value) """
	err = picam.Picam_SetParameterIntegerValueOnline( camera, parameter, value)
	err = ReturnPicamError(err)
	return err

def Picam_SetParameterFloatingPointValueOnline(camera, parameter, value):
	""" PICAM_API Picam_SetParameterFloatingPointValueOnline( PicamHandle camera, PicamParameter parameter, piflt value) """
	err = picam.Picam_SetParameterFloatingPointValueOnline( camera, parameter, value)
	err = ReturnPicamError(err)
	return err

def Picam_SetParameterPulseValueOnline(camera, parameter, value):
	""" PICAM_API Picam_SetParameterPulseValueOnline( PicamHandle camera, PicamParameter parameter, const PicamPulse* value) """
	err = picam.Picam_SetParameterPulseValueOnline( camera, parameter, value)
	err = ReturnPicamError(err)
	return err

def Picam_CanReadParameter(camera, parameter, readable):
	""" PICAM_API Picam_CanReadParameter( PicamHandle camera, PicamParameter parameter, pibln* readable) """
	err = picam.Picam_CanReadParameter( camera, parameter, readable)
	err = ReturnPicamError(err)
	return err

def Picam_ReadParameterIntegerValue(camera, parameter, value):
	""" PICAM_API Picam_ReadParameterIntegerValue( PicamHandle camera, PicamParameter parameter, piint* value) """
	err = picam.Picam_ReadParameterIntegerValue( camera, parameter, value)
	err = ReturnPicamError(err)
	return err

def Picam_ReadParameterFloatingPointValue(camera, parameter, value):
	""" PICAM_API Picam_ReadParameterFloatingPointValue( PicamHandle camera, PicamParameter parameter, piflt* value) """
	err = picam.Picam_ReadParameterFloatingPointValue( camera, parameter, value)
	err = ReturnPicamError(err)
	return err

def Picam_DestroyParameters(parameter_array):
	""" PICAM_API Picam_DestroyParameters( const PicamParameter* parameter_array ) """
	err = picam.Picam_DestroyParameters(parameter_array)
	err = ReturnPicamError(err)
	return err

def Picam_GetParameters(camera, parameter_array, parameter_count):
	""" PICAM_API Picam_GetParameters( PicamHandle camera, const PicamParameter** parameter_array, piint* parameter_count) """
	err = picam.Picam_GetParameters( camera, parameter_array, parameter_count)
	err = ReturnPicamError(err)
	return err

def Picam_DoesParameterExist(camera, parameter, exists):
	""" PICAM_API Picam_DoesParameterExist( PicamHandle camera, PicamParameter parameter, pibln* exists) """
	err = picam.Picam_DoesParameterExist( camera, parameter, exists)
	err = ReturnPicamError(err)
	return err

def Picam_IsParameterRelevant(camera, parameter, relevant):
	""" PICAM_API Picam_IsParameterRelevant( PicamHandle camera, PicamParameter parameter, pibln* relevant) """
	err = picam.Picam_IsParameterRelevant( camera, parameter, relevant)
	err = ReturnPicamError(err)
	return err

def Picam_GetParameterValueType(camera, parameter, type):
	""" PICAM_API Picam_GetParameterValueType( PicamHandle camera, PicamParameter parameter, PicamValueType* type) """
	err = picam.Picam_GetParameterValueType( camera, parameter, type)
	err = ReturnPicamError(err)
	return err

def Picam_GetParameterEnumeratedType(camera, parameter, type):
	""" PICAM_API Picam_GetParameterEnumeratedType( PicamHandle camera, PicamParameter parameter, PicamEnumeratedType* type) """
	err = picam.Picam_GetParameterEnumeratedType( camera, parameter, type)
	err = ReturnPicamError(err)
	return err

def Picam_GetParameterValueAccess(camera, parameter, access):
	""" PICAM_API Picam_GetParameterValueAccess( PicamHandle camera, PicamParameter parameter, PicamValueAccess* access) """
	err = picam.Picam_GetParameterValueAccess( camera, parameter, access)
	err = ReturnPicamError(err)
	return err

def Picam_GetParameterConstraintType(camera, parameter, type):
	""" PICAM_API Picam_GetParameterConstraintType( PicamHandle camera, PicamParameter parameter, PicamConstraintType* type) """
	err = picam.Picam_GetParameterConstraintType( camera, parameter, type)
	err = ReturnPicamError(err)
	return err

def Picam_DestroyCollectionConstraints(constraint_array):
	""" PICAM_API Picam_DestroyCollectionConstraints( const PicamCollectionConstraint* constraint_array) """
	err = picam.Picam_DestroyCollectionConstraints( constraint_array)
	err = ReturnPicamError(err)
	return err

def Picam_GetParameterCollectionConstraint(camera, parameter, category, constraint):
	""" PICAM_API Picam_GetParameterCollectionConstraint( PicamHandle camera, PicamParameter parameter, PicamConstraintCategory category, const PicamCollectionConstraint** constraint) """
	err = picam.Picam_GetParameterCollectionConstraint( camera, parameter, category, constraint)
	err = ReturnPicamError(err)
	return err

def Picam_DestroyRangeConstraints(constraint_array):
	""" PICAM_API Picam_DestroyRangeConstraints( const PicamRangeConstraint* constraint_array) """
	err = picam.Picam_DestroyRangeConstraints( constraint_array)
	err = ReturnPicamError(err)
	return err

def Picam_GetParameterRangeConstraint(camera, parameter, category, constraint):
	""" PICAM_API Picam_GetParameterRangeConstraint( PicamHandle camera, PicamParameter parameter, PicamConstraintCategory category, const PicamRangeConstraint** constraint) """
	err = picam.Picam_GetParameterRangeConstraint( camera, parameter, category, constraint)
	err = ReturnPicamError(err)
	return err

def Picam_DestroyRoisConstraints(constraint_array):
	""" PICAM_API Picam_DestroyRoisConstraints( const PicamRoisConstraint* constraint_array) """
	err = picam.Picam_DestroyRoisConstraints( constraint_array)
	err = ReturnPicamError(err)
	return err

def Picam_GetParameterRoisConstraint(camera, parameter, category, constraint):
	""" PICAM_API Picam_GetParameterRoisConstraint( PicamHandle camera, PicamParameter parameter, PicamConstraintCategory category, const PicamRoisConstraint** constraint) """
	err = picam.Picam_GetParameterRoisConstraint( camera, parameter, category, constraint)
	err = ReturnPicamError(err)
	return err

def Picam_DestroyPulseConstraints(constraint_array):
	""" PICAM_API Picam_DestroyPulseConstraints( const PicamPulseConstraint* constraint_array) """
	err = picam.Picam_DestroyPulseConstraints( constraint_array)
	err = ReturnPicamError(err)
	return err

def Picam_GetParameterPulseConstraint(camera, parameter, category, constraint):
	""" PICAM_API Picam_GetParameterPulseConstraint( PicamHandle camera, PicamParameter parameter, PicamConstraintCategory category, const PicamPulseConstraint** constraint) """
	err = picam.Picam_GetParameterPulseConstraint( camera, parameter, category, constraint)
	err = ReturnPicamError(err)
	return err

def Picam_DestroyModulationsConstraints(constraint_array):
	""" PICAM_API Picam_DestroyModulationsConstraints( const PicamModulationsConstraint* constraint_array) """
	err = picam.Picam_DestroyModulationsConstraints( constraint_array)
	err = ReturnPicamError(err)
	return err

def Picam_GetParameterModulationsConstraint(camera, parameter, category, constraint):
	""" PICAM_API Picam_GetParameterModulationsConstraint( PicamHandle camera, PicamParameter parameter, PicamConstraintCategory category, const PicamModulationsConstraint** constraint) """
	err = picam.Picam_GetParameterModulationsConstraint( camera, parameter, category, constraint)
	err = ReturnPicamError(err)
	return err

def Picam_AreParametersCommitted(camera, committed):
	""" PICAM_API Picam_AreParametersCommitted( PicamHandle camera, pibln* committed) """
	err = picam.Picam_AreParametersCommitted( camera, committed)
	err = ReturnPicamError(err)
	return err

def Picam_CommitParameters(camera, failed_parameter_array, failed_parameter_count):
	""" PICAM_API Picam_CommitParameters( PicamHandle camera, const PicamParameter** failed_parameter_array, piint* failed_parameter_count) """
	err = picam.Picam_CommitParameters( camera, failed_parameter_array, failed_parameter_count)
	err = ReturnPicamError(err)
	return err

def Picam_Acquire(camera, readout_count, readout_time_out, available, errors):
	""" PICAM_API Picam_Acquire( PicamHandle camera, pi64s readout_count, piint readout_time_out, PicamAvailableData* available, PicamAcquisitionErrorsMask* errors) """
	err = picam.Picam_Acquire( camera, readout_count, readout_time_out, available, errors)
	err = ReturnPicamError(err)
	return err

def Picam_StartAcquisition(camera):
	""" PICAM_API Picam_StartAcquisition( PicamHandle camera ) """
	err = picam.Picam_StartAcquisition(camera)
	err = ReturnPicamError(err)
	return err

def Picam_StopAcquisition(camera):
	""" PICAM_API Picam_StopAcquisition( PicamHandle camera ) """
	err = picam.Picam_StopAcquisition(camera)
	err = ReturnPicamError(err)
	return err

def Picam_IsAcquisitionRunning(camera, running):
	""" PICAM_API Picam_IsAcquisitionRunning( PicamHandle camera, pibln* running) """
	err = picam.Picam_IsAcquisitionRunning( camera, running)
	err = ReturnPicamError(err)
	return err

def Picam_WaitForAcquisitionUpdate(camera, readout_time_out, available, status):
	""" PICAM_API Picam_WaitForAcquisitionUpdate( PicamHandle camera, piint readout_time_out, PicamAvailableData* available, PicamAcquisitionStatus* status) """
	err = picam.Picam_WaitForAcquisitionUpdate( camera, readout_time_out, available, status)
	err = ReturnPicamError(err)
	return err


def ReturnPicamError(errcode):
    """expects integer error code.  Returns string with description"""
    if(errcode == 0):
        err = "PicamError_None"
    if(errcode == 4):
        err = "PicamError_UnexpectedError"
    if(errcode == 3):
        err = "PicamError_UnexpectedNullPointer"
    if(errcode == 35):
        err = "PicamError_InvalidPointer"
    if(errcode == 39):
        err = "PicamError_InvalidCount"
    if(errcode == 42):
        err = "PicamError_InvalidOperation"
    if(errcode == 1):
        err = "PicamError_LibraryNotInitialized"
    if(errcode == 5):
        err = "PicamError_LibraryAlreadyInitialized"
    if(errcode == 16):
        err = "PicamError_InvalidEnumeratedType"
    if(errcode == 17):
        err = "PicamError_EnumerationValueNotDefined"
    if(errcode == 18):
        err = "PicamError_NotDiscoveringCameras"
    if(errcode == 19):
        err = "PicamError_AlreadyDiscoveringCameras"
    if(errcode == 34):
        err = "PicamError_NoCamerasAvailable"
    if(errcode == 7):
        err = "PicamError_CameraAlreadyOpened"
    if(errcode == 8):
        err = "PicamError_InvalidCameraID"
    if(errcode == 9):
        err = "PicamError_InvalidHandle"
    if(errcode == 15):
        err = "PicamError_DeviceCommunicationFailed"
    if(errcode == 23):
        err = "PicamError_DeviceDisconnected"
    if(errcode == 24):
        err = "PicamError_DeviceOpenElsewhere"
    if(errcode == 6):
        err = "PicamError_InvalidDemoModel"
    if(errcode == 21):
        err = "PicamError_InvalidDemoSerialNumber"
    if(errcode == 22):
        err = "PicamError_DemoAlreadyConnected"
    if(errcode == 40):
        err = "PicamError_DemoNotSupported"
    if(errcode == 11):
        err = "PicamError_ParameterHasInvalidValueType"
    if(errcode == 13):
        err = "PicamError_ParameterHasInvalidConstraintType"
    if(errcode == 12):
        err = "PicamError_ParameterDoesNotExist"
    if(errcode == 10):
        err = "PicamError_ParameterValueIsReadOnly"
    if(errcode == 2):
        err = "PicamError_InvalidParameterValue"
    if(errcode == 38):
        err = "PicamError_InvalidConstraintCategory"
    if(errcode == 14):
        err = "PicamError_ParameterValueIsIrrelevant"
    if(errcode == 25):
        err = "PicamError_ParameterIsNotOnlineable"
    if(errcode == 26):
        err = "PicamError_ParameterIsNotReadable"
    if(errcode == 28):
        err = "PicamError_InvalidParameterValues"
    if(errcode == 29):
        err = "PicamError_ParametersNotCommitted"
    if(errcode == 30):
        err = "PicamError_InvalidAcquisitionBuffer"
    if(errcode == 36):
        err = "PicamError_InvalidReadoutCount"
    if(errcode == 37):
        err = "PicamError_InvalidReadoutTimeOut"
    if(errcode == 31):
        err = "PicamError_InsufficientMemory"
    if(errcode == 20):
        err = "PicamError_AcquisitionInProgress"
    if(errcode == 27):
        err = "PicamError_AcquisitionNotInProgress"
    if(errcode == 32):
        err = "PicamError_TimeOutOccurred"
    if(errcode == 33):
        err = "PicamError_AcquisitionUpdatedHandlerRegistered"
    if(errcode == 41):
        err = "PicamError_InvalidNvramSection"
    return err


