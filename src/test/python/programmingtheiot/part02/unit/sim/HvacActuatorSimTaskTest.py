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
from programmingtheiot.cda.sim.HvacActuatorSimTask import HvacActuatorSimTask

class HvacActuatorSimTaskTest(unittest.TestCase):
	"""
	This test case class contains very basic unit tests for
	HvacActuatorSimTask. It should not be considered complete,
	but serve as a starting point for the student implementing
	additional functionality within their Programming the IoT
	environment.
	"""
	DEFAULT_VAL_A = 18.2
	DEFAULT_VAL_B = 21.4
	
	@classmethod
	def setUpClass(self):
		logging.basicConfig(format = '%(asctime)s:%(module)s:%(levelname)s:%(message)s', level = logging.DEBUG)
		logging.info("Testing HvacActuatorSimTask class...")
		self.hSimTask = HvacActuatorSimTask()
		
	def setUp(self):
		pass

	def tearDown(self):
		pass

	def testUpdateActuator(self):
		ad = ActuatorData(typeID = ConfigConst.HVAC_ACTUATOR_TYPE)
		ad.setCommand(ConfigConst.COMMAND_ON)
		ad.setValue(self.DEFAULT_VAL_A)
		
		adr = self.hSimTask.updateActuator(ad)
		
		self.assertIsNotNone(adr)
		self.assertEquals(adr.getValue(), self.DEFAULT_VAL_A)
		logging.info("ActuatorData: " + str(adr))
		
		ad.setValue(self.DEFAULT_VAL_B)
		
		adr = self.hSimTask.updateActuator(ad)
		
		self.assertIsNotNone(adr)
		self.assertEquals(adr.getValue(), self.DEFAULT_VAL_B)
		logging.info("ActuatorData: " + str(adr))
		
		ad.setCommand(ConfigConst.COMMAND_OFF)
		
		adr = self.hSimTask.updateActuator(ad)
		
		self.assertIsNotNone(adr)
		self.assertEquals(adr.getCommand(), ConfigConst.COMMAND_OFF)
		logging.info("ActuatorData: " + str(adr))
		
	@unittest.skip("Ignore for now.")
	def testUpdateActuatorRepeatCommands(self):
		ad = ActuatorData(typeID = ConfigConst.HVAC_ACTUATOR_TYPE)
		
		# new command ON with new value - should succeed
		ad.setCommand(ConfigConst.COMMAND_ON)
		ad.setValue(self.DEFAULT_VAL_A)
		
		adr = self.hSimTask.updateActuator(ad)
		
		self.assertIsNotNone(adr)
		self.assertEquals(adr.getValue(), self.DEFAULT_VAL_A)
		logging.info("ActuatorData: " + str(adr))
		
		# same command ON with same value - should fail
		ad.setCommand(ConfigConst.COMMAND_ON)
		ad.setValue(self.DEFAULT_VAL_A)
		
		adr = self.hSimTask.updateActuator(ad)
		
		self.assertIsNone(adr)
		logging.info("ActuatorData: " + str(adr))
		
		# new command OFF with same value - should succeed
		ad.setCommand(ConfigConst.COMMAND_OFF)
		ad.setValue(self.DEFAULT_VAL_A)
		
		adr = self.hSimTask.updateActuator(ad)
		
		self.assertIsNotNone(adr)
		self.assertEquals(adr.getValue(), self.DEFAULT_VAL_A)
		logging.info("ActuatorData: " + str(adr))
		
		# same command OFF with different value - should succeed
		ad.setCommand(ConfigConst.COMMAND_OFF)
		ad.setValue(self.DEFAULT_VAL_B)
		
		adr = self.hSimTask.updateActuator(ad)
		
		self.assertIsNotNone(adr)
		logging.info("ActuatorData: " + str(adr))
		
		# new command ON with same value - should succeed
		ad.setCommand(ConfigConst.COMMAND_ON)
		ad.setValue(self.DEFAULT_VAL_B)
		
		adr = self.hSimTask.updateActuator(ad)
		
		self.assertIsNotNone(adr)
		logging.info("ActuatorData: " + str(adr))
		
		# same command ON with new value - should succeed
		ad.setCommand(ConfigConst.COMMAND_ON)
		ad.setValue(self.DEFAULT_VAL_A)
		
		adr = self.hSimTask.updateActuator(ad)
		
		self.assertIsNotNone(adr)
		logging.info("ActuatorData: " + str(adr))
		
		# new command OFF with same value - should succeed
		ad.setCommand(ConfigConst.COMMAND_OFF)
		ad.setValue(self.DEFAULT_VAL_A)
		
		adr = self.hSimTask.updateActuator(ad)
		
		self.assertIsNotNone(adr)
		self.assertEquals(adr.getValue(), self.DEFAULT_VAL_A)
		logging.info("ActuatorData: " + str(adr))
		
		# same command OFF with same value - should fail
		ad.setCommand(ConfigConst.COMMAND_OFF)
		ad.setValue(self.DEFAULT_VAL_A)
		
		adr = self.hSimTask.updateActuator(ad)
		
		self.assertIsNone(adr)
		logging.info("ActuatorData: " + str(adr))
		
if __name__ == "__main__":
	unittest.main()
	