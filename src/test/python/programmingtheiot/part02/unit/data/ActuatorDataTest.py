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

from programmingtheiot.data.ActuatorData import ActuatorData

class ActuatorDataTest(unittest.TestCase):
	"""
	This test case class contains very basic unit tests for
	ActuatorData. It should not be considered complete,
	but serve as a starting point for the student implementing
	additional functionality within their Programming the IoT
	environment.
	"""
	
	DEFAULT_NAME = "ActuatorDataFooBar"
	DEFAULT_STATE_DATA = "{state: None}"
	DEFAULT_VALUE = 15.2
	
	@classmethod
	def setUpClass(self):
		logging.basicConfig(format = '%(asctime)s:%(module)s:%(levelname)s:%(message)s', level = logging.DEBUG)
		logging.info("Testing ActuatorData class...")
		
	def setUp(self):
		pass

	def tearDown(self):
		pass
	
	def testDefaultValues(self):
		ad = ActuatorData()
		
		self.assertEquals(ad.getCommand(), ConfigConst.DEFAULT_COMMAND)
		self.assertEquals(ad.getStatusCode(), ConfigConst.DEFAULT_STATUS)
		
		logging.info("Actuator data as string: " + str(ad))

	def testParameterUpdates(self):
		ad = self._createTestActuatorData()
		
		self.assertEquals(ad.getName(), self.DEFAULT_NAME)
		self.assertEquals(ad.getCommand(), ConfigConst.COMMAND_ON)
		self.assertEquals(ad.getStateData(), self.DEFAULT_STATE_DATA)
		self.assertEquals(ad.getValue(), self.DEFAULT_VALUE)

	def testFullUpdate(self):
		ad = ActuatorData()
		ad2 = self._createTestActuatorData()
		
		ad.updateData(ad2)
		
		self.assertEquals(ad.getCommand(), ConfigConst.COMMAND_ON)
		self.assertEquals(ad.getStateData(), self.DEFAULT_STATE_DATA)
		self.assertEquals(ad.getValue(), self.DEFAULT_VALUE)
		
	def _createTestActuatorData(self):
		ad = ActuatorData()
		
		ad.setName(self.DEFAULT_NAME)
		ad.setCommand(ConfigConst.COMMAND_ON)
		ad.setStateData(self.DEFAULT_STATE_DATA)
		ad.setValue(self.DEFAULT_VALUE)
		
		logging.info("Actuator data as string: " + str(ad))
		
		return ad

if __name__ == "__main__":
	unittest.main()
	