#####
# 
# This class is part of the Programming the Internet of Things
# project, and is available via the MIT License, which can be
# found in the LICENSE file at the top level of this repository.
# 
# Copyright (c) 2020 by Andrew D. King
# 

from programmingtheiot.common.IDataMessageListener import IDataMessageListener

class IDataManager(object):
	"""
	Interface definition for data manager implementations.
	
	"""
	
	def startManager(self) -> bool:
		"""
		Starts the manager.
		
		"""
		pass
		
	def stopManager(self) -> bool:
		"""
		Stops the manager.
		
		"""
		pass
	
	def setDataMessageListener(self, listener: IDataMessageListener = None):
		"""
		Sets the data message listener if non-null.
		
		@param listener
		"""
		pass
	