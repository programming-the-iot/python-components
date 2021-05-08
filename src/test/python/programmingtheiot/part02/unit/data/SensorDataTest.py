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

import programmingtheiot.common.ConfigConst as ConfigConst

from programmingtheiot.data.SensorData import SensorData

class SensorDataTest(unittest.TestCase):
	"""
	This test case class contains very basic unit tests for
	SensorData. It should not be considered complete,
	but serve as a starting point for the student implementing
	additional functionality within their Programming the IoT
	environment.
	"""
	
	DEFAULT_NAME = "SensorDataFooBar"
	TEST_COUNT = 2
	MIN_VALUE = 10.0
	MAX_VALUE = 50.0
	AVG_VALUE = ((MIN_VALUE + MAX_VALUE) / TEST_COUNT)
	
	@classmethod
	def setUpClass(self):
		logging.basicConfig(format = '%(asctime)s:%(module)s:%(levelname)s:%(message)s', level = logging.DEBUG)
		logging.info("Testing SensorData class...")
		
	def setUp(self):
		pass

	def tearDown(self):
		pass
	
	def testDefaultValues(self):
		sd = SensorData()
		
		self.assertEquals(sd.getName(), ConfigConst.NOT_SET)
		self.assertEquals(sd.getValue(), ConfigConst.DEFAULT_VAL)
		
		logging.info("Sensor data as string: " + str(sd))

	def testParameterUpdates(self):
		sd = self._createTestSensorData()
		
		self.assertEquals(sd.getName(), self.DEFAULT_NAME)
		self.assertEquals(sd.getValue(), self.MIN_VALUE)

	def testFullUpdate(self):
		sd = SensorData()
		sd2 = self._createTestSensorData()
		
		sd.updateData(sd2)
		
		self.assertEquals(sd.getName(), self.DEFAULT_NAME)
		self.assertEquals(sd.getValue(), self.MIN_VALUE)
	
	def _createTestSensorData(self):
		sd = SensorData()
		
		sd.setName(self.DEFAULT_NAME)
		sd.setValue(self.MIN_VALUE)
		
		logging.info("Sensor data as string: " + str(sd))
		
		return sd

if __name__ == "__main__":
	unittest.main()
	