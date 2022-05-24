#####
# 
# This class is part of the Programming the Internet of Things
# project, and is available via the MIT License, which can be
# found in the LICENSE file at the top level of this repository.
# 
# Copyright (c) 2020 by Andrew D. King
# 

import logging
import time
import unittest

from time import sleep

from programmingtheiot.cda.connection.CoapClientConnector import CoapClientConnector

from programmingtheiot.common.ResourceNameEnum import ResourceNameEnum

from programmingtheiot.data.DataUtil import DataUtil
from programmingtheiot.data.SensorData import SensorData

class CoapClientPerformanceTest(unittest.TestCase):
	"""
	This test case class contains very basic performance tests for
	CoapClientConnector. It should not be considered complete,
	but serve as a starting point for the student implementing
	additional functionality within their Programming the IoT
	environment.
	"""
	NS_IN_MILLIS = 1000000
	MAX_TEST_RUNS = 10000
	
	@classmethod
	def setUpClass(self):
		logging.disable(level = logging.WARNING)
		
	def setUp(self):
		self.coapClient = CoapClientConnector()

	def tearDown(self):
		self.coapClient.disconnectClient()
					
	@unittest.skip("Ignore for now.")
	def testGetRequestCon(self):
		"""
		Comment the annotation to perf test CON GET
		"""
		print("Testing GET - CON")
		
		self._execTestGet(self.MAX_TEST_RUNS, True)

	@unittest.skip("Ignore for now.")
	def testGetRequestNon(self):
		"""
		Comment the annotation to perf test NON GET
		"""
		print("Testing GET - NON")
		
		self._execTestGet(self.MAX_TEST_RUNS, False)

	@unittest.skip("Ignore for now.")
	def testPostRequestCon(self):
		"""
		Comment the annotation to perf test CON POST
		"""
		print("Testing POST - CON")
		
		self._execTestPost(self.MAX_TEST_RUNS, True)

	@unittest.skip("Ignore for now.")
	def testPostRequestNon(self):
		"""
		Comment the annotation to perf test NON POST
		"""
		print("Testing POST - NON")
		
		self._execTestPost(self.MAX_TEST_RUNS, False)

	@unittest.skip("Ignore for now.")
	def testPutRequestCon(self):
		"""
		Comment the annotation to perf test CON PUT
		"""
		print("Testing PUT - CON")
		
		self._execTestPut(self.MAX_TEST_RUNS, True)

	@unittest.skip("Ignore for now.")
	def testPutRequestNon(self):
		"""
		Comment the annotation to perf test NON PUT
		"""
		print("Testing PUT - NON")
		
		self._execTestPut(self.MAX_TEST_RUNS, False)

	def _execTestGet(self, maxTestRuns: int, useCon: bool):
		startTime = time.time_ns()
		
		for seqNo in range(0, maxTestRuns):
			self.coapClient.sendGetRequest(resource = ResourceNameEnum.CDA_ACTUATOR_CMD_RESOURCE, enableCON = useCon)
			
		endTime = time.time_ns()
		elapsedMillis = (endTime - startTime) / self.NS_IN_MILLIS
		
		print("\nGET message - useCON = " + str(useCon) + " [" + str(maxTestRuns) + "]: " + str(elapsedMillis) + " ms")
		
		sleep(2)
		
	def _execTestPost(self, maxTestRuns: int, useCon: bool):
		sensorData = SensorData()
		payload = DataUtil().sensorDataToJson(sensorData)
		
		startTime = time.time_ns()
		
		for seqNo in range(0, maxTestRuns):
			self.coapClient.sendPostRequest(resource = ResourceNameEnum.CDA_SENSOR_MSG_RESOURCE, enableCON = useCon, payload = payload)
			
		endTime = time.time_ns()
		elapsedMillis = (endTime - startTime) / self.NS_IN_MILLIS
		
		print("\nPOST message - useCON = " + str(useCon) + " [" + str(maxTestRuns) + "]: " + str(elapsedMillis) + " ms. Payload Len: " + str(len(payload)))
		
		sleep(2)
		
	def _execTestPut(self, maxTestRuns: int, useCon: bool):
		sensorData = SensorData()
		payload = DataUtil().sensorDataToJson(sensorData)
		
		startTime = time.time_ns()
		
		for seqNo in range(0, maxTestRuns):
			self.coapClient.sendPostRequest(resource = ResourceNameEnum.CDA_SENSOR_MSG_RESOURCE, enableCON = useCon, payload = payload)
			
		endTime = time.time_ns()
		elapsedMillis = (endTime - startTime) / self.NS_IN_MILLIS
		
		print("\nPUT message - useCON = " + str(useCon) + " [" + str(maxTestRuns) + "]: " + str(elapsedMillis) + " ms. Payload Len: " + str(len(payload)))
		
		sleep(2)
	
if __name__ == "__main__":
	unittest.main()
	