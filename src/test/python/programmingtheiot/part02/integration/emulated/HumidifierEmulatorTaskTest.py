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

from time import sleep

import programmingtheiot.common.ConfigConst as ConfigConst

from programmingtheiot.data.ActuatorData import ActuatorData
from programmingtheiot.cda.emulated.HumidifierEmulatorTask import HumidifierEmulatorTask

class HumidifierEmulatorTaskTest(unittest.TestCase):
	"""
	This test case class contains very basic unit tests for
	HumidifierEmulatorTask. It should not be considered complete,
	but serve as a starting point for the student implementing
	additional functionality within their Programming the IoT
	environment.
	
	NOTE: This test requires the sense_emu_gui to be running
	and must have access to the underlying libraries that
	support the pisense module. On Windows, one way to do
	this is by installing pisense and sense-emu within the
	Bash on Ubuntu on Windows environment and then execute this
	test case from the command line, as it will likely fail
	if run within an IDE in native Windows.
	
	"""
	
	@classmethod
	def setUpClass(self):
		logging.basicConfig(format = '%(asctime)s:%(module)s:%(levelname)s:%(message)s', level = logging.DEBUG)
		logging.info("Testing HumidifierEmulatorTask class [using SenseHAT emulator]...")
		self.huSimTask = HumidifierEmulatorTask()
		
	def setUp(self):
		pass

	def tearDown(self):
		pass

	def testUpdateEmulator(self):
		ad = ActuatorData(typeID = ConfigConst.HUMIDIFIER_ACTUATOR_TYPE)
		ad.setCommand(ConfigConst.COMMAND_ON)
		ad.setValue(50.0)
		
		adr = self.huSimTask.updateActuator(ad)
		
		if adr:
			self.assertEqual(adr.getCommand(), ConfigConst.COMMAND_ON)
			self.assertEqual(adr.getStatusCode(), 0)
			logging.info("ActuatorData: " + str(adr))
			
			# wait 5 seconds
			sleep(5)
		else:
			logging.warning("ActuatorData is None.")
			
		ad.setValue(35.0)
		
		adr = self.huSimTask.updateActuator(ad)
		
		if adr:
			self.assertEqual(adr.getCommand(), ConfigConst.COMMAND_ON)
			self.assertEqual(adr.getStatusCode(), 0)
			logging.info("ActuatorData: " + str(adr))
			
			# wait 5 seconds
		else:
			logging.warning("ActuatorData is None.")
			
		ad.setCommand(ConfigConst.COMMAND_OFF)
		
		adr = self.huSimTask.updateActuator(ad)
		
		if adr:
			self.assertEqual(adr.getCommand(), ConfigConst.COMMAND_OFF)
			self.assertEqual(adr.getStatusCode(), 0)
			logging.info("ActuatorData: " + str(adr))
		else:
			logging.warning("ActuatorData is None.")
			
if __name__ == "__main__":
	unittest.main()
	