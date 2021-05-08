#####
# 
# This class is part of the Programming the Internet of Things
# project, and is available via the MIT License, which can be
# found in the LICENSE file at the top level of this repository.
# 
# Copyright (c) 2020 by Andrew D. King
# 

from programmingtheiot.data.SensorData import SensorData

class ITelemetryDataListener():
	"""
	Interface definition for telemetry data listener clients.
	
	"""
	
	def onSensorDataUpdate(self, data: SensorData) -> bool:
		"""
		Callback function to handle a sensor message packaged as a SensorData object.
		
		@param data The SensorData message received.
		@return bool True on success; False otherwise.
		"""
		pass
	