#####
# 
# This class is part of the Programming the Internet of Things
# project, and is available via the MIT License, which can be
# found in the LICENSE file at the top level of this repository.
# 
# Copyright (c) 2020 by Andrew D. King
# 

import logging
import unittest

import time

from programmingtheiot.cda.connection.MqttClientConnector import MqttClientConnector

from programmingtheiot.common.ResourceNameEnum import ResourceNameEnum

from programmingtheiot.data.DataUtil import DataUtil
from programmingtheiot.data.SensorData import SensorData

class MqttClientConnectorTest(unittest.TestCase):
	"""
	This test case class contains very basic unit tests for
	MqttClientConnector. It should not be considered complete,
	but serve as a starting point for the student implementing
	additional functionality within their Programming the IoT
	environment.
	"""
	NS_IN_MILLIS = 1000000
	MAX_TEST_RUNS = 10000
	
	@classmethod
	def setUpClass(self):
		logging.basicConfig(format = '%(asctime)s:%(module)s:%(levelname)s:%(message)s', level = logging.DEBUG)
		
	def setUp(self):
		self.mqttClient = MqttClientConnector(clientID = 'CDAMqttClientPerformanceTest001')
		pass

	def tearDown(self):
		pass

	@unittest.skip("Ignore for now.")
	def testConnectAndDisconnect(self):
		startTime = time.time_ns()
		
		self.assertTrue(self.mqttClient.connectClient())
		self.assertTrue(self.mqttClient.disconnectClient())
		
		endTime = time.time_ns()
		elapsedMillis = (endTime - startTime) / self.NS_IN_MILLIS
		
		logging.info("Connect and Disconnect: " + str(elapsedMillis) + " ms")
		
	@unittest.skip("Ignore for now.")
	def testPublishQoS0(self):
		self._execTestPublish(self.MAX_TEST_RUNS, 0)

	@unittest.skip("Ignore for now.")
	def testPublishQoS1(self):
		self._execTestPublish(self.MAX_TEST_RUNS, 1)

	@unittest.skip("Ignore for now.")
	def testPublishQoS2(self):
		self._execTestPublish(self.MAX_TEST_RUNS, 2)

	def _execTestPublish(self, maxTestRuns: int, qos: int):
		self.assertTrue(self.mqttClient.connectClient())
		
		sensorData = SensorData()
		payload = DataUtil().sensorDataToJson(sensorData)
		payloadLen = len(payload)
		startTime = time.time_ns()
		
		for seqNo in range(0, maxTestRuns):
			self.mqttClient.publishMessage(resource = ResourceNameEnum.CDA_SENSOR_MSG_RESOURCE, msg = payload, qos = qos)
			
		endTime = time.time_ns()
		elapsedMillis = (endTime - startTime) / self.NS_IN_MILLIS
		
		self.assertTrue(self.mqttClient.disconnectClient())
		
		logging.info( \
			"\n\tTesting Publish: QoS = %r | msgs = %r | payload size = %r | start = %r | end = %r | elapsed = %r", \
			qos, maxTestRuns, payloadLen, startTime / 1000, endTime / 1000, elapsedMillis / 1000)
		
		#logging.info("Publish message - QoS " + str(qos) + " [" + str(maxTestRuns) + "]: " + str(elapsedMillis) + " ms")
	
if __name__ == "__main__":
	unittest.main()
	