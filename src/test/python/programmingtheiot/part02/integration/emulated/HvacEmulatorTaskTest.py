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
from programmingtheiot.cda.emulated.HvacEmulatorTask import HvacEmulatorTask

class HvacEmulatorTaskTest(unittest.TestCase):
	"""
	This test case class contains very basic unit tests for
	HvacEmulatorTaskTest. It should not be considered complete,
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
		logging.info("Testing HvacEmulatorTask class [using SenseHAT emulator]...")
		self.hvSimTask = HvacEmulatorTask()
		
	def setUp(self):
		pass

	def tearDown(self):
		pass

	def testUpdateEmulator(self):
		ad = ActuatorData(typeID = ConfigConst.HVAC_ACTUATOR_TYPE)
		ad.setCommand(ConfigConst.COMMAND_ON)
		ad.setValue(22.0)
		
		adr = self.hvSimTask.updateActuator(ad)
		
		if adr:
			self.assertEqual(adr.getCommand(), ConfigConst.COMMAND_ON)
			self.assertEqual(adr.getStatusCode(), 0)
			logging.info("ActuatorData: " + str(adr))
			
			# wait 5 seconds
			sleep(5)
		else:
			logging.warning("ActuatorData is None.")
			
		ad.setValue(20.0)
		
		adr = self.hvSimTask.updateActuator(ad)
		
		if adr:
			self.assertEqual(adr.getCommand(), ConfigConst.COMMAND_ON)
			self.assertEqual(adr.getStatusCode(), 0)
			logging.info("ActuatorData: " + str(adr))
			
			# wait 5 seconds
		else:
			logging.warning("ActuatorData is None.")
			
		ad.setCommand(ConfigConst.COMMAND_OFF)
		
		adr = self.hvSimTask.updateActuator(ad)
		
		if adr:
			self.assertEqual(adr.getCommand(), ConfigConst.COMMAND_OFF)
			self.assertEqual(adr.getStatusCode(), 0)
			logging.info("ActuatorData: " + str(adr))
		else:
			logging.warning("ActuatorData is None.")
			
if __name__ == "__main__":
	unittest.main()
	