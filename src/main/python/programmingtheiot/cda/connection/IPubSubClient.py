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

class IPubSubClient():
	"""
	Interface definition for pub/sub clients.
	
	"""
	
	def connectClient(self) -> bool:
		"""
		Connects to the pub/sub broker / server using configuration parameters
		specified by the sub-class.
		
		@return bool True on success; False otherwise.
		"""
		pass

	def disconnectClient(self) -> bool:
		"""
		Disconnects from the pub/sub broker / server if the client is already connected.
		If not, this call is ignored, but will return a False.
		
		@return bool True on success; False otherwise.
		"""
		pass

	def publishMessage(self, resource: ResourceNameEnum = None, payload: str = None, qos: int = ConfigConst.DEFAULT_QOS) -> bool:
		"""
		Attempts to publish a message to the given topic with the given qos
		to the pub/sub broker / server. If not already connected, the sub-class
		implementation should either throw an exception, or handle the exception
		and log a message, and return False.
		
		@param resource The topic Enum containing the topic value to publish the message to.
		@param msg The message to publish. This is expected to be well-formed JSON.
		@param qos The QoS level. This is expected to be 0 - 2. Default is DEFAULT_QOS.
		@return bool True on success; False otherwise.
		"""
		pass

	def subscribeToTopic(self, resource: ResourceNameEnum = None, callback = None, qos: int = ConfigConst.DEFAULT_QOS) -> bool:
		"""
		Attempts to subscribe to a topic with the given qos hosted by the
		pub/sub broker / server. If not already connected, the sub-class
		implementation should either throw an exception, or handle the exception
		and log a message, and return False.
		
		@param resource The topic Enum containing the topic value to subscribe to.
		@param callback The callback function reference to use for incoming messages
		destined for the resource named topic. Default is None, which means the default
		incoming message callback should be used instead.
		@param qos The QoS level. This is expected to be 0 - 2. Default is DEFAULT_QOS.
		@return bool True on success; False otherwise.
		"""
		pass

	def unsubscribeFromTopic(self, resource: ResourceNameEnum = None) -> bool:
		"""
		Attempts to unsubscribe from a topic hosted by the pub/sub broker / server.
		If not already connected, the sub-class implementation should either
		throw an exception, or handle the exception and log a message, and return False.
		
		@param resource The topic Enum containing the topic value to unsubscribe from.
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
	