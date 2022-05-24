#####
# 
# This class is part of the Programming the Internet of Things
# project, and is available via the MIT License, which can be
# found in the LICENSE file at the top level of this repository.
# 
# Copyright (c) 2020 by Andrew D. King
# 

from enum import Enum

import programmingtheiot.common.ConfigConst as ConfigConst

class ResourceNameEnum(Enum):
	"""
	Enum declaration for resource and topic names for the CDA and GDA.
	
	So, why don't we just use the string defined in ConfigConst?
	
	Option 1: (chosen - for now), this may not seem 'Pythonic',
	but it's one way to enforce consistency in resource / topic naming.
	It also limits the number of resource and topic names, which can
	quickly grow out of hand if free reign is provided without any
	semi-strict convention. Finally, it permits relatively straight
	forward mapping to other languages that support Enum's
	(such as Java [and the GDA]).
	
	Option 2: Delegate the resource generation to a separate class
	that generates a resource name based on the typed parameters
	passed into a given function. Similar to Option 1, but names
	are dynamically, yet still consistently, generated.
	
	Option 3: Define resource name keys in ConfigConst,
	and define the resource names within the configuration file.
	I may change over to this model, as it allows for easier
	debugging and on-the-fly changes. Similar to option 1, except
	the resource names are easier to change whenever you'd like.
	
	Option 4: Simply rely on the string to be constructed properly
	within each code module that has to publish / subscribe data to,
	or request / response data from, a server-based resource.
	In short, anything goes.
	
	For now, we'll stick with using Enum's. The name is captured within
	ConfigConst, so it's still relatively easy to debug, IMO.
	
	"""
	CDA_SENSOR_MSG_RESOURCE           = ConfigConst.CDA_SENSOR_DATA_MSG_RESOURCE
	CDA_ACTUATOR_CMD_RESOURCE    	  = ConfigConst.CDA_ACTUATOR_CMD_MSG_RESOURCE
	CDA_ACTUATOR_RESPONSE_RESOURCE    = ConfigConst.CDA_ACTUATOR_RESPONSE_MSG_RESOURCE
	CDA_MGMT_STATUS_MSG_RESOURCE	  = ConfigConst.CDA_MGMT_STATUS_MSG_RESOURCE
	CDA_MGMT_STATUS_CMD_RESOURCE	  = ConfigConst.CDA_MGMT_CMD_MSG_RESOURCE
	CDA_SYSTEM_PERF_MSG_RESOURCE	  = ConfigConst.CDA_SYSTEM_PERF_MSG_RESOURCE
	CDA_UPDATE_NOTIFICATIONS_RESOURCE = ConfigConst.CDA_UPDATE_NOTIFICATIONS_MSG_RESOURCE
	CDA_REGISTRATION_REQUEST_RESOURCE = ConfigConst.CDA_REGISTRATION_REQUEST_RESOURCE

	def getResourceNameByValue(self, val: str) -> str:
		"""
		Looks up the resource enum by its value.
		
		@param val The string value to use for the enum lookup.
		@return ResourceNameEnum On success, the enum will be returned.
		"""
		if val in ResourceNameEnum.__members__:
			return ResourceNameEnum.__members__[val]
	
			