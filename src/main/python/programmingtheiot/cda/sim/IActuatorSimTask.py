#####
# 
# This class is part of the Programming the Internet of Things
# project, and is available via the MIT License, which can be
# found in the LICENSE file at the top level of this repository.
# 
# Copyright (c) 2020 by Andrew D. King
# 

from programmingtheiot.data.ActuatorData import ActuatorData

class IActuatorSimTask():
	"""
	This is a simple 'interface' for an Actuator abstraction.
	
	You may consider using this as a base class for all actuator
	sim task implementations or not - it's not required.
	"""

	def getSimpleName(self) -> str:
		"""
		Returns the simplified name passed in from the sub-class.
		
		@return String
		"""
		pass
	
	def updateActuator(self, data: ActuatorData) -> ActuatorData:
		"""
		Updates the actuator state using the given ActuatorData.
		Performs basic validation internally - optionally, add a
		template method definition (e.g. def _validateData(data: ActuatorData) -> bool:),
		call, which can be overridden by the sub-class if needed.
		May also trigger a call to activate or deactivate the
		actuator, depending upon the command within data.
		
		This will setup the actuation call after validating
		'data', then invoke the 'private' _handleActuation() method,
		which in turn returns the status code to be used in the
		response data.
		
		@param data The ActuatorData to process.
		@return ActuatorData A new ActuatorData updated with the original command and the response flag enabled.
		"""
		pass
	