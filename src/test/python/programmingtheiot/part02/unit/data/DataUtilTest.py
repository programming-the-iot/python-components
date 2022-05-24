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

from programmingtheiot.data.DataUtil import DataUtil

from programmingtheiot.data.ActuatorData import ActuatorData
from programmingtheiot.data.SensorData import SensorData
from programmingtheiot.data.SystemPerformanceData import SystemPerformanceData

class DataUtilTest(unittest.TestCase):
	"""
	This test case class contains very basic unit tests for
	DataUtil. It should not be considered complete,
	but serve as a starting point for the student implementing
	additional functionality within their Programming the IoT
	environment.
	"""
	
	@classmethod
	def setUpClass(self):
		logging.basicConfig(format = '%(asctime)s:%(module)s:%(levelname)s:%(message)s', level = logging.DEBUG)
		logging.info("Testing DataUtil class...")
		
		encodeToUtf8 = False
		
		self.dataUtil = DataUtil(encodeToUtf8)

		self.adName = "FooBar ActuatorData"
		self.sdName = "FooBar SensorData"
		self.spdName = "FooBar SystemPerformanceData"
		
	def setUp(self):
		logging.info("================================================")
		logging.info("DataUtil test execution...")
		logging.info("================================================")
		
		pass

	def tearDown(self):
		pass
	
	#@unittest.skip("Ignore for now.")
	def testActuatorDataConversionsFromJson(self):
		logging.info("\n\n----- [ActuatorData Conversions from JSON] -----")
		
		self.assertIsNone(self.dataUtil.jsonToActuatorData(None))
		self.assertIsNone(self.dataUtil.jsonToActuatorData(""))
		
		ad     = ActuatorData()
		ad.setName(self.adName)
		adJson = self.dataUtil.actuatorDataToJson(ad)
		
		adObj1    = self.dataUtil.jsonToActuatorData(adJson)
		adObj1Str = self.dataUtil.actuatorDataToJson(adObj1)
		adObj2    = self.dataUtil.jsonToActuatorData(adObj1Str)

		logging.info("Sample JSON: " + str(adJson))
		logging.info("JSON to ActuatorData: " + str(adObj1))
		logging.info("ActuatorData back to JSON: " + str(adObj1Str))
		
		self.assertEqual(self.adName, adObj1.getName())
		self.assertEqual(self.adName, adObj2.getName())
		self.assertEqual(adObj1.getTimeStamp(), adObj2.getTimeStamp())

	#@unittest.skip("Ignore for now.")
	def testActuatorDataConversionsFromObject(self):
		logging.info("\n\n----- [JSON Conversions from ActuatorData] -----")
		
		adName = "FooBar2 Actuator"
		adObj1 = ActuatorData()
		adObj1.setName(adName)
		
		adObj1Str = self.dataUtil.actuatorDataToJson(adObj1)
		adObj2    = self.dataUtil.jsonToActuatorData(adObj1Str)
		adObj2Str = self.dataUtil.actuatorDataToJson(adObj2)

		logging.info("Sample ActuatorData: " + str(adObj1))
		logging.info("ActuatorData to JSON: " + str(adObj1Str))
		logging.info("JSON back to ActuatorData: " + str(adObj2))
		logging.info("ActuatorData back to JSON: " + str(adObj2Str))

		self.assertEqual(adName, adObj1.getName())
		self.assertEqual(adObj1.getName(), adObj2.getName())
		self.assertEqual(adObj1.getTimeStamp(), adObj2.getTimeStamp())
		self.assertEqual(adObj1Str, adObj2Str)

	#@unittest.skip("Ignore for now.")
	def testSensorDataConversionsFromJson(self):
		logging.info("\n\n----- [SensorData Conversions from JSON] -----")
		
		self.assertIsNone(self.dataUtil.jsonToSensorData(None))
		self.assertIsNone(self.dataUtil.jsonToSensorData(""))
		
		sd     = SensorData()
		sd.setName(self.sdName)
		sdJson = self.dataUtil.sensorDataToJson(sd)
		
		sdObj1    = self.dataUtil.jsonToSensorData(sdJson)
		sdObj1Str = self.dataUtil.sensorDataToJson(sdObj1)
		sdObj2    = self.dataUtil.jsonToSensorData(sdObj1Str)
		
		logging.info("Sample JSON: " + str(sdJson))
		logging.info("JSON to SensorData: " + str(sdObj1))
		logging.info("SensorData back to JSON: " + str(sdObj1Str))
		
		self.assertEqual(self.sdName, sdObj1.getName())
		self.assertEqual(self.sdName, sdObj2.getName())
		self.assertEqual(sdObj1.getTimeStamp(), sdObj2.getTimeStamp())

	#@unittest.skip("Ignore for now.")
	def testSensorDataConversionsFromObject(self):
		logging.info("\n\n----- [JSON Conversions from SensorData] -----")
		
		sdName = "Foobar2 Sensor"
		sdObj1 = SensorData()
		sdObj1.setName(sdName)
		
		sdObj1Str = self.dataUtil.sensorDataToJson(sdObj1)
		sdObj2    = self.dataUtil.jsonToSensorData(sdObj1Str)
		sdObj2Str = self.dataUtil.sensorDataToJson(sdObj2)
		
		logging.info("Sample SensorData: " + str(sdObj1))
		logging.info("SensorData to JSON: " + str(sdObj1Str))
		logging.info("JSON back to SensorData: " + str(sdObj2))
		logging.info("SensorData back to JSON: " + str(sdObj2Str))

		self.assertEqual(sdName, sdObj1.getName())
		self.assertEqual(sdObj1.getName(), sdObj2.getName())
		self.assertEqual(sdObj1.getTimeStamp(), sdObj2.getTimeStamp())
		self.assertEqual(sdObj1Str, sdObj2Str)

	#@unittest.skip("Ignore for now.")
	def testSystemPerformanceConversionsFromJson(self):
		logging.info("\n\n----- [SystemPerformanceData Conversions from JSON] -----")
		
		self.assertIsNone(self.dataUtil.jsonToSystemPerformanceData(None))
		self.assertIsNone(self.dataUtil.jsonToSystemPerformanceData(""))
		
		spd     = SystemPerformanceData()
		spd.setName(self.spdName)
		spdJson = self.dataUtil.systemPerformanceDataToJson(spd)
		
		spdObj1    = self.dataUtil.jsonToSystemPerformanceData(spdJson)
		spdObj1Str = self.dataUtil.systemPerformanceDataToJson(spdObj1)
		spdObj2    = self.dataUtil.jsonToSystemPerformanceData(spdObj1Str)
		
		logging.info("Sample JSON: " + str(spdJson))
		logging.info("JSON to SystemPerformanceData: " + str(spdObj1))
		logging.info("SystemPerformanceData back to JSON: " + str(spdObj1Str))
		
		self.assertEqual(self.spdName, spdObj1.getName())
		self.assertEqual(self.spdName, spdObj2.getName())
		self.assertEqual(spdObj1.getTimeStamp(), spdObj2.getTimeStamp())

	#@unittest.skip("Ignore for now.")
	def testSystemPerformanceDataConversionsFromObject(self):
		logging.info("\n\n----- [JSON Conversions from SystemPerformanceData] -----")
		
		spdName = "Foobar2 SystemPerformanceData"
		spdObj1 = SystemPerformanceData()
		spdObj1.setName(spdName)
		
		spdObj1Str = self.dataUtil.systemPerformanceDataToJson(spdObj1)
		spdObj2    = self.dataUtil.jsonToSystemPerformanceData(spdObj1Str)
		spdObj2Str = self.dataUtil.systemPerformanceDataToJson(spdObj2)
		
		logging.info("Sample SystemPerformanceData: " + str(spdObj1))
		logging.info("SystemPerformanceData to JSON: " + str(spdObj1Str))
		logging.info("JSON back to SystemPerformanceData: " + str(spdObj2))
		logging.info("SystemPerformanceData back to JSON: " + str(spdObj2Str))

		self.assertEqual(spdName, spdObj1.getName())
		self.assertEqual(spdObj1.getName(), spdObj2.getName())
		self.assertEqual(spdObj1.getTimeStamp(), spdObj2.getTimeStamp())
		self.assertEqual(spdObj1Str, spdObj2Str)

if __name__ == "__main__":
	unittest.main()
