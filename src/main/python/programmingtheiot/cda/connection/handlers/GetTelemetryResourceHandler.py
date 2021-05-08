#####
# 
# This class is part of the Programming the Internet of Things
# project, and is available via the MIT License, which can be
# found in the LICENSE file at the top level of this repository.
# 
# Copyright (c) 2020 by Andrew D. King
# 

import logging

import programmingtheiot.common.ConfigConst as ConfigConst

from programmingtheiot.common.ConfigUtil import ConfigUtil
from programmingtheiot.common.ITelemetryDataListener import ITelemetryDataListener

from programmingtheiot.data.DataUtil import DataUtil
from programmingtheiot.data.SensorData import SensorData

class GetTelemetryResourceHandler(ITelemetryDataListener):
	"""
	Observable resource that will collect telemetry based on the given
	name from the data message listener implementation.
	
	NOTE: Your implementation will likely need to extend from the selected
	CoAP library's observable resource base class.
	
	"""

	def __init__(self):
		pass
		
	def onSensorDataUpdate(self, data: SensorData = None) -> bool:
		pass
	