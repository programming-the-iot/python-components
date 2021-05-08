#####
# 
# This class is part of the Programming the Internet of Things
# project, and is available via the MIT License, which can be
# found in the LICENSE file at the top level of this repository.
# 
# Copyright (c) 2020 by Andrew D. King
# 

import logging

from programmingtheiot.common.ResourceNameEnum import ResourceNameEnum
from programmingtheiot.common.IDataMessageListener import IDataMessageListener
from programmingtheiot.data.ActuatorData import ActuatorData
from programmingtheiot.data.SensorData import SensorData
from programmingtheiot.data.SystemPerformanceData import SystemPerformanceData
from programmingtheiot.common.ITelemetryDataListener import ITelemetryDataListener
from programmingtheiot.common.ISystemPerformanceDataListener import ISystemPerformanceDataListener

class DefaultDataMessageListener(IDataMessageListener):
	"""
	Basic (default) implementation of the IDataMessageListener interface for testing.
	
	"""

	def __init__(self):
		"""
		Default constructor. This will set remote server information and client connection
		information based on the default configuration file contents.
		
		"""
		self.sysPerfDataListener = None
		self.telemetryDataListeners = {}
		
	def getLatestActuatorDataResponseFromCache(self, name: str = None) -> ActuatorData:
		"""
		Retrieves the named actuator data (response) item from the internal data cache.
		
		@param name
		@return ActuatorData
		"""
		pass
		
	def getLatestSensorDataFromCache(self, name: str = None) -> SensorData:
		"""
		Retrieves the named sensor data item from the internal data cache.
		
		@param name
		@return SensorData
		"""
		sd = SensorData()
		sd.setValue(15.0)
		
		return sd
	
	def getLatestSystemPerformanceDataFromCache(self, name: str = None) -> SystemPerformanceData:
		"""
		Retrieves the named system performance data from the internal data cache.
		
		@param name
		@return SystemPerformanceData
		"""
		pass
	
	def handleActuatorCommandMessage(self, data: ActuatorData) -> bool:
		"""
		Callback function to handle an actuator command message packaged as a ActuatorData object.
		
		@param data The ActuatorData message received.
		@return bool True on success; False otherwise.
		"""
		if data:
			logging.info('Actuator Command Msg: ' + str(data.getCommand()))
			
		return True
	
	def handleActuatorCommandResponse(self, data: ActuatorData) -> bool:
		"""
		Callback function to handle an actuator command response packaged as a ActuatorData object.
		
		@param data The ActuatorData message received.
		@return bool True on success; False otherwise.
		"""
		if data:
			logging.info('Actuator Command: ' + str(data.getCommand()))
			
		return True
	
	def handleIncomingMessage(self, resourceEnum: ResourceNameEnum, msg: str) -> bool:
		"""
		Callback function to handle incoming messages on a given topic with
		a string-based payload.
		
		@param resourceEnum The topic enum associated with this message.
		@param msg The message received. It is expected to be in JSON format.
		@return bool True on success; False otherwise.
		"""
		logging.info('Topic: %s  Message: %s', resourceEnum.value(), msg)
		return True

	def handleSensorMessage(self, data: SensorData) -> bool:
		"""
		Callback function to handle a sensor message packaged as a SensorData object.
		
		@param data The SensorData message received.
		@return bool True on success; False otherwise.
		"""
		if data:
			logging.info('Sensor Message: ' + str(data))
			
			if data.getName() in self.telemetryDataListeners:
				self.telemetryDataListeners[data.getName()].onSensorDataUpdate(data)
			
		return True
	
	def handleSystemPerformanceMessage(self, data: SystemPerformanceData) -> bool:
		"""
		Callback function to handle a system performance message packaged as
		SystemPerformanceData object.
		
		@param data The SystemPerformanceData message received.
		@return bool True on success; False otherwise.
		"""
		if data:
			logging.info('System Performance Message: ' + str(data))
			
			if self.sysPerfDataListener:
				self.sysPerfDataListener.onSystemPerformanceDataUpdate(data)
				
		return True
	
	def setSystemPerformanceDataListener(self, listener: ISystemPerformanceDataListener = None):
		"""
		Setter for the ITelemetryDataListener for system performance data.
		
		@param listener
		"""
		if listener:
			self.sysPerfDataListener = listener
			
	def setTelemetryDataListener(self, name: str = None, listener: ITelemetryDataListener = None):
		"""
		Sets the named telemetry data listener. The listener's callback function will be invoked
		when telemetry data is available for the given name.
		
		@param name The name of the listener.
		@param listener The listener reference.
		"""
		if listener:
			self.telemetryDataListeners[name] = listener
			