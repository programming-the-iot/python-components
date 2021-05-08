#####
# 
# This class is part of the Programming the Internet of Things
# project, and is available via the MIT License, which can be
# found in the LICENSE file at the top level of this repository.
# 
# Copyright (c) 2020 by Andrew D. King
# 

import logging

from programmingtheiot.common.IDataMessageListener import IDataMessageListener

from programmingtheiot.data.DataUtil import DataUtil
from programmingtheiot.data.ActuatorData import ActuatorData

class UpdateActuatorResourceHandler():
	"""
	Standard resource that will handle an incoming actuation command,
	and return the command response.
	
	NOTE: Your implementation will likely need to extend from the selected
	CoAP library's resource base class.
	
	"""

	def __init__(self, dataMsgListener: IDataMessageListener = None):
		pass
		