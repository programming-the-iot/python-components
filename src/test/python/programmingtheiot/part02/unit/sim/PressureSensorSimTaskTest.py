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

from programmingtheiot.cda.sim.PressureSensorSimTask import PressureSensorSimTask

class PressureSensorSimTaskTest(unittest.TestCase):
	"""
	This test case class contains very basic unit tests for
	PressureSensorSimTask. It should not be considered complete,
	but serve as a starting point for the student implementing
	additional functionality within their Programming the IoT
	environment.
	"""
	
	@classmethod
	def setUpClass(self):
		logging.basicConfig(format = '%(asctime)s:%(module)s:%(levelname)s:%(message)s', level = logging.DEBUG)
		logging.info("Testing PressureSensorSimTask class...")
		self.pSimTask = PressureSensorSimTask()
		
	def setUp(self):
		pass

	def tearDown(self):
		pass

	def testGenerateTelemetry(self):
		sd = self.pSimTask.generateTelemetry()
		
		if sd:
			logging.info("SensorData: " + str(sd))
		else:
			logging.warning("SensorData is None.")
			
	def testGetTelemetryValue(self):
		val = self.pSimTask.getTelemetryValue()
		logging.info("Pressure data: %f", val)
		self.assertGreater(val, 0.0)

if __name__ == "__main__":
	unittest.main()
	