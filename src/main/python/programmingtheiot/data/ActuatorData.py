#####
# 
# This class is part of the Programming the Internet of Things project.
# 
# It is provided as a simple shell to guide the student and assist with
# implementation for the Programming the Internet of Things exercises,
# and designed to be modified by the student as needed.
#

import programmingtheiot.common.ConfigConst as ConfigConst

from programmingtheiot.data.BaseIotData import BaseIotData

class ActuatorData(BaseIotData):
	"""
	Shell representation of class for student implementation.
	
	"""

	def __init__(self, typeID: int = ConfigConst.DEFAULT_ACTUATOR_TYPE, name = ConfigConst.NOT_SET, d = None):
		super(ActuatorData, self).__init__(name = name, typeID = typeID, d = d)
		pass
	
	def getCommand(self) -> int:
		pass
	
	def getStateData(self) -> str:
		pass
	
	def getValue(self) -> float:
		pass
	
	def isResponseFlagEnabled(self) -> bool:
		return False
	
	def setCommand(self, command: int):
		pass
	
	def setAsResponse(self):
		pass
		
	def setStateData(self, stateData: str):
		pass
	
	def setValue(self, val: float):
		pass
		
	def _handleUpdateData(self, data):
		pass
		