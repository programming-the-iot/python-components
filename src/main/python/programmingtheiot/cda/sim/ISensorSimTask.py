#####
# 
# This class is part of the Programming the Internet of Things
# project, and is available via the MIT License, which can be
# found in the LICENSE file at the top level of this repository.
# 
# Copyright (c) 2020 by Andrew D. King
# 

from programmingtheiot.data.SensorData import SensorData

class ISensorSimTask():
	"""
	This is a simple 'interface' definition for a sensor task abstraction.
	
	You may consider using this as a base class for all actuator
	sim task implementations or not - it's not required.
	"""
	
	def generateTelemetry(self) -> SensorData:
		"""
		Creates a SensorData instance with the current simulator value
		and associated timestamp. If self.useRandomizer is enabled, a random
		value between self.minVal and self.maxVal will be generated along
		with the current time stamp. If self.dataSet is valid, the data
		and time entries associated with self.dataSetIndex will be used,
		and self.dataSetIndex will be incremented to the next index, up
		to size - 1, after which it will revert back to 0.
		
		@return The SensorData instance.
		"""
		pass
	
	def getLatestTelemetry(self) -> SensorData:
		"""
		Returns a newly created SensorData instance as a copy
		of the latest telemetry data generated.
		
		If no telemetry has been generated when this method is
		called, None is returned.
		
		@return SensorData
		"""
		pass
	
	def getName(self) -> str:
		"""
		Returns the name of this simulator.
		
		@return str
		"""
		pass
	
	def getTypeID(self) -> int:
		"""
		Returns the type ID of this simulator.
		
		@return int
		"""
		pass
	
	def getTelemetryValue(self) -> float:
		"""
		Returns the current value from the stored self.latestSensorData instance.
		If it hasn't been generated yet, this will invoke self.generateTelemetry()
		and then return the current value from the generated SensorData.
		
		@return float
		"""
		pass
