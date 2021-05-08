#####
# 
# This class is part of the Programming the Internet of Things
# project, and is available via the MIT License, which can be
# found in the LICENSE file at the top level of this repository.
# 
# Copyright (c) 2020 by Andrew D. King
# 

from datetime import datetime, timezone

import programmingtheiot.common.ConfigConst as ConfigConst

from programmingtheiot.common.ConfigUtil import ConfigUtil

class BaseIotData(object):
	"""
	This is the base class for all data containers. It stores values that each
	sub-class is expected to set and / or utilization, including the name,
	location ID, type ID, location specifics, and status information.
	
	Sub-classes add parameters and accessors specific to their needs.
	
	"""

	def __init__(self, name = ConfigConst.NOT_SET, typeID = ConfigConst.DEFAULT_TYPE_ID, d = None):
		"""
		Constructor.
		
		@param d Defaults to None. The data (dict) to use for setting all parameters.
		It's provided here as a convenience - mostly for testing purposes. The utility
		in DataUtil should be used instead.
		"""
			
		self.updateTimeStamp()
		self.hasError = False
		
		useDefaults = True
		
		if d:
			try:
				self.name       = d[ConfigConst.NAME_PROP]
				self.typeID     = d[ConfigConst.TYPE_ID_PROP]
				self.statusCode = d[ConfigConst.STATUS_CODE_PROP]
				self.latitude   = d[ConfigConst.LATITUDE_PROP]
				self.longitude  = d[ConfigConst.LONGITUDE_PROP]
				self.elevation  = d[ConfigConst.ELEVATION_PROP]
				
				useDefaults = False
			except:
				pass
			
		if useDefaults:
			self.name       = name
			self.typeID     = typeID
			self.statusCode = ConfigConst.DEFAULT_STATUS
			self.latitude   = ConfigConst.DEFAULT_LAT
			self.longitude  = ConfigConst.DEFAULT_LON
			self.elevation  = ConfigConst.DEFAULT_ELEVATION
		
		if not self.name:
			self.name = ConfigConst.NOT_SET
			
		# always pull location ID from configuration file
		self.locationID = ConfigUtil().getProperty(ConfigConst.CONSTRAINED_DEVICE, ConfigConst.DEVICE_LOCATION_ID_KEY)
		
	def getElevation(self) -> float:
		"""
		Returns the elevation.
		
		@return The elevation value as a float.
		"""
		return self.elevation
	
	def getLatitude(self) -> float:
		"""
		Returns the latitude.
		
		@return The latitude value as a float.
		"""
		return self.latitude
	
	def getLongitude(self) -> float:
		"""
		Returns the longitude.
		
		@return The longitude value as a float.
		"""
		return self.longitude
	
	def getLocationID(self) -> str:
		"""
		Returns the location ID.
		
		@return The location ID as a string.
		"""
		return self.locationID
	
	def getName(self) -> str:
		"""
		Returns the name.
		
		@return The name as a string.
		"""
		return self.name
	
	def getStatusCode(self) -> int:
		"""
		Returns the status code value.
		
		@return The status code value as an integer.
		"""
		return self.statusCode
	
	def getTimeStamp(self) -> str:
		"""
		Returns the time stamp in ISO 8601 format, as follows:
		%Y%m%dT%H:%M:%S%z
		
		@return The time stamp as a string.
		"""
		return self.timeStamp
	
	def getTypeID(self) -> int:
		"""
		Returns the type ID as an integer. This allows for additional granularity
		in determining the sensor, actuator, or other data representation.
		
		@return The type ID as an integer.
		"""
		return self.typeID
	
	def hasErrorFlag(self):
		"""
		Returns the boolean flag indicating if an error is present.
		
		@return The boolean flag representing the error state.
		True if there's an error condition; false otherwise.
		"""
		return self.hasError
	
	def setElevation(self, val: float):
		"""
		Sets the elevation value.
		
		@param val The elevation value as a float.
		"""
		self.elevation = val
	
	def setLatitude(self, val: float):
		"""
		Sets the latitude value.
		
		@param val The latitude value as a float.
		"""
		self.latitude = val
	
	def setLongitude(self, val: float):
		"""
		Sets the longitude value.
		
		@param val The longitude value as a float.
		"""
		self.longitude = val
	
	def setLocationID(self, idStr: str):
		"""
		Sets the location ID. If invalid, no action is taken.
		
		@param idStr The id as a string.
		"""
		if idStr:
			self.locationID = idStr
		
	def setName(self, name: str):
		"""
		Sets the name. If invalid, no action is taken.
		
		@param The name as a string.
		"""
		if name:
			self.name = name
		
	def setStatusCode(self, val: int):
		"""
		Sets the status code value. If the status code is
		less than 0, the error flag will be set.
		
		@param val The status code value as an integer.
		"""
		self.statusCode = val
		
		if val < 0:
			self.hasError = True
			
	def setTypeID(self, val: int):
		"""
		Sets the type ID value.
		
		@param val The type ID value as an integer.
		"""
		self.typeID = val
	
	def updateData(self, data):
		"""
		Sets the internal values of this object to be that of 'data',
		which is assumed to be an BaseIotData instance.
		
		NOTE: The time stamp will also be updated by this action.
		
		@param data The BaseIotData data to apply to this instance.
		"""
		if data and isinstance(data, BaseIotData):
			self.setName(data.getName())
			self.setTypeID(data.getTypeID())
			self.setStatusCode(data.getStatusCode())
			self.setElevation(data.getElevation())
			self.setLatitude(data.getLatitude())
			self.setLongitude(data.getLongitude())
			self.setLocationID(data.getLocationID())
			
			self.updateTimeStamp()
			
			self._handleUpdateData(data)
		
	def updateTimeStamp(self):
		"""
		Updates the internal time stamp to the current date / time
		in Zulu time.
		This retrieves the time since Epoch and converts to an ISO 8601
		string, with second granularity, as follows:
		
		e.g. 2020-12-27T17:12:40.032631+00:00
		
		NOTE: the '+00:00' is the offset from GMT, and can be replaced
		with 'Z' if desired. In testing, the format above is
		compatible with the GDA's parsing logic.
		"""
		self.timeStamp = str(datetime.now(timezone.utc).isoformat())
	
	def __str__(self):
		"""
		Returns a string representation of this instance.
		
		@return The string representing this instance, returned in CSV 'key=value' format.
		"""
		return '{}={},{}={},{}={},{}={},{}={},{}={},{}={},{}={},{}={}'.format(
			ConfigConst.NAME_PROP, self.name,
			ConfigConst.TYPE_ID_PROP, self.typeID,
			ConfigConst.TIMESTAMP_PROP, self.timeStamp,
			ConfigConst.STATUS_CODE_PROP, self.statusCode,
			ConfigConst.HAS_ERROR_PROP, self.hasError,
			ConfigConst.LOCATION_ID_PROP, self.locationID,
			ConfigConst.ELEVATION_PROP, self.elevation,
			ConfigConst.LATITUDE_PROP, self.latitude,
			ConfigConst.LONGITUDE_PROP, self.longitude)
			
	def _handleUpdateData(self, data):
		"""
		Template method definition to update sub-class data.
		
		@param data The BaseIotData data to apply to this instance.
		"""
		pass
