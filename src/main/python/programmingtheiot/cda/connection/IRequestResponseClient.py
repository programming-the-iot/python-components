#####
# 
# This class is part of the Programming the Internet of Things
# project, and is available via the MIT License, which can be
# found in the LICENSE file at the top level of this repository.
# 
# Copyright (c) 2020 by Andrew D. King
# 

import programmingtheiot.common.ConfigConst as ConfigConst

from programmingtheiot.common.ResourceNameEnum import ResourceNameEnum
from programmingtheiot.common.IDataMessageListener import IDataMessageListener

class IRequestResponseClient():
	"""
	Interface definition for request/response clients.
	
	"""
	DEFAULT_TIMEOUT = 5
	DEFAULT_TTL = 300
	
	def sendDiscoveryRequest(self, timeout: int = 5) -> bool:
		"""
		Connects to the server and sends a discovery request to the server.
		IDataMessageListener callback must be set to receive response.
		
		@param timeout The number of seconds to wait for a response before returning (default is DEFAULT_TIMEOUT).
		@return bool True on success; False otherwise.
		"""
		pass

	def sendDeleteRequest(self, resource: ResourceNameEnum = None, name: str = None, enableCON: bool = False, timeout: int = ConfigConst.DEFAULT_TIMEOUT) -> bool:
		"""
		Connects to the server and sends DELETE request to resource at path.
		IDataMessageListener callback must be set to receive response.
		
		@param resource The resource enum containing the resource path string.
		@param enableCON If true, CON (confirmed) messaging will be used; otherwise use NON (non-confirmed).
		@param timeout The number of seconds to wait for a response before returning (default is DEFAULT_TIMEOUT).
		@return bool True on success; False otherwise.
		"""
		pass

	def sendGetRequest(self, resource: ResourceNameEnum = None, name: str = None, enableCON: bool = False, timeout: int = ConfigConst.DEFAULT_TIMEOUT) -> bool:
		"""
		Connects to the server and sends GET request for resource at path.
		IDataMessageListener callback must be set to receive response.
		
		@param resource The resource enum containing the resource path string.
		@param enableCON If true, CON (confirmed) messaging will be used; otherwise use NON (non-confirmed).
		@param timeout The number of seconds to wait for a response before returning (default is DEFAULT_TIMEOUT).
		@return bool True on success; False otherwise.
		"""
		pass

	def sendPostRequest(self, resource: ResourceNameEnum = None, name: str = None, enableCON: bool = False, payload: str = None, timeout: int = ConfigConst.DEFAULT_TIMEOUT) -> bool:
		"""
		Connects to the server and sends POST request of payload to resource at path.
		IDataMessageListener callback must be set to receive response.
		
		@param resource The resource enum containing the resource path string.
		@param enableCON If true, CON (confirmed) messaging will be used; otherwise use NON (non-confirmed).
		@param payload The JSON payload to send.
		@param timeout The number of seconds to wait for a response before returning (default is DEFAULT_TIMEOUT).
		@return bool True on success; False otherwise.
		"""
		pass

	def sendPutRequest(self, resource: ResourceNameEnum = None, name: str = None, enableCON: bool = False, payload: str = None, timeout: int = ConfigConst.DEFAULT_TIMEOUT) -> bool:
		"""
		Connects to the server and sends GET request for resource at path.
		IDataMessageListener callback must be set to receive response.
		
		@param resource The resource enum containing the resource path string.
		@param enableCON If true, CON (confirmed) messaging will be used; otherwise use NON (non-confirmed).
		@param payload The JSON payload to send.
		@param timeout The number of seconds to wait for a response before returning (default is DEFAULT_TIMEOUT).
		@return bool True on success; False otherwise.
		"""
		pass

	def setDataMessageListener(self, listener: IDataMessageListener = None) -> bool:
		"""
		Sets the data message listener reference, assuming listener is non-null.
		
		@param listener The data message listener instance to use for passing relevant
		messages, such as those received from a subscription event.
		@return bool True on success (if listener is non-null will always be the case); False otherwise.
		"""
		pass

	def startObserver(self, resource: ResourceNameEnum = None, name: str = None, ttl: int = ConfigConst.DEFAULT_TTL) -> bool:
		"""
		Connects to the server and sends a discovery request to the server.
		IDataMessageListener callback must be set to receive response.
		
		@param resource The resource enum containing the resource path string.
		@param ttl The time to live of the observation. By default, will run for DEFAULT_TTL seconds,
		then stop. If set to 0 or less, will run indefinitely until stopObserver() is called.
		@return bool True on success; False otherwise.
		"""
		pass

	def stopObserver(self, resource: ResourceNameEnum = None, name: str = None, timeout: int = ConfigConst.DEFAULT_TIMEOUT) -> bool:
		"""
		Connects to the server and sends a discovery request to the server.
		IDataMessageListener callback must be set to receive response.
		
		@param timeout The number of seconds to wait for a response before returning (default is DEFAULT_TIMEOUT).
		@return bool True on success; False otherwise.
		"""
		pass
