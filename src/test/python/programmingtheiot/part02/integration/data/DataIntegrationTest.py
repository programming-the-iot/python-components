#####
# 
# This class is part of the Programming the Internet of Things
# project, and is available via the MIT License, which can be
# found in the LICENSE file at the top level of this repository.
# 
# Copyright (c) 2020 by Andrew D. King
# 

import logging
import os
import unittest

import programmingtheiot.common.ConfigConst as ConfigConst

from pathlib import Path

from programmingtheiot.common.ConfigUtil import ConfigUtil
from programmingtheiot.data.DataUtil import DataUtil

from programmingtheiot.data.ActuatorData import ActuatorData
from programmingtheiot.data.SensorData import SensorData
from programmingtheiot.data.SystemPerformanceData import SystemPerformanceData

class DataIntegrationTest(unittest.TestCase):
	"""
	This test case class contains very basic integration tests for
	DataUtil and data container classes for use between the CDA and
	GDA to verify JSON compatibility. It should not be considered complete,
	but serve as a starting point for the student implementing
	additional functionality within their Programming the IoT
	environment.
	"""
	
	@classmethod
	def setUpClass(self):
		logging.basicConfig(format = '%(asctime)s:%(module)s:%(levelname)s:%(message)s', level = logging.DEBUG)
		logging.info("Running DataIntegrationTest test cases...")
		
		encodeToUtf8 = False
		
		self.dataUtil = DataUtil(encodeToUtf8)

		self.cdaDataPath = ConfigUtil().getProperty(ConfigConst.CONSTRAINED_DEVICE, ConfigConst.TEST_CDA_DATA_PATH_KEY)
		self.gdaDataPath = ConfigUtil().getProperty(ConfigConst.CONSTRAINED_DEVICE, ConfigConst.TEST_GDA_DATA_PATH_KEY)
		
		if not os.path.exists(self.cdaDataPath):
			logging.info("================================================")
			logging.info("DataIntegrationTest - path needs to be created: " + self.cdaDataPath)
			os.makedirs(self.cdaDataPath, exist_ok = True)
			
	def setUp(self):
		logging.info("================================================")
		logging.info("DataIntegrationTest test execution...")
		logging.info("================================================")
		
		pass

	def tearDown(self):
		pass
	
	#@unittest.skip("Ignore for now.")
	def testWriteActuatorDataToCdaDataPath(self):
		logging.info("\n\n----- [ActuatorData to JSON to file] -----")
		
		dataObj  = ActuatorData()
		dataStr  = self.dataUtil.actuatorDataToJson(dataObj)
		fileName = self.cdaDataPath + '/ActuatorData.dat'

		logging.info("Sample ActuatorData JSON (validated): " + str(dataStr))
		logging.info("Writing ActuatorData JSON to CDA data path: " + fileName)
		
		fileRef = Path(fileName)
		fileRef.write_text(dataStr, encoding = 'utf-8')
		
	#@unittest.skip("Ignore for now.")
	def testWriteSensorDataToCdaDataPath(self):
		logging.info("\n\n----- [SensorData to JSON to file] -----")
		
		dataObj  = SensorData()
		dataStr  = self.dataUtil.sensorDataToJson(dataObj)
		fileName = self.cdaDataPath + '/SensorData.dat'

		logging.info("Sample SensorData JSON (validated): " + str(dataStr))
		logging.info("Writing SensorData JSON to CDA data path: " + fileName)
		
		fileRef = Path(fileName)
		fileRef.write_text(dataStr, encoding = 'utf-8')

	#@unittest.skip("Ignore for now.")
	def testWriteSystemPerformanceDataToCdaDataPath(self):
		logging.info("\n\n----- [SystemPerformanceData to JSON to file] -----")
		
		dataObj  = SystemPerformanceData()
		dataStr  = self.dataUtil.sensorDataToJson(dataObj)
		fileName = self.cdaDataPath + '/SystemPerformanceData.dat'

		logging.info("Sample SystemPerformanceData JSON (validated): " + str(dataStr))
		logging.info("Writing SystemPerformanceData JSON to CDA data path: " + fileName)
		
		fileRef = Path(fileName)
		fileRef.write_text(dataStr, encoding = 'utf-8')

	#@unittest.skip("Ignore for now.")
	def testReadActuatorDataFromGdaDataPath(self):
		logging.info("\n\n----- [ActuatorData JSON from file to object] -----")
		
		fileName = self.gdaDataPath + '/ActuatorData.dat'
		fileRef  = Path(fileName)
		dataStr  = fileRef.read_text(encoding = 'utf-8')

		dataObj  = self.dataUtil.jsonToActuatorData(dataStr)

		logging.info("ActuatorData JSON from GDA: " + dataStr)
		logging.info("ActuatorData object: " + str(dataObj))

	#@unittest.skip("Ignore for now.")
	def testReadSensorDataFromGdaDataPath(self):
		logging.info("\n\n----- [SensorData JSON from file to object] -----")
		
		fileName = self.gdaDataPath + '/SensorData.dat'
		fileRef  = Path(fileName)
		dataStr  = fileRef.read_text(encoding = 'utf-8')

		dataObj  = self.dataUtil.jsonToSensorData(dataStr)

		logging.info("SensorData JSON from GDA: " + dataStr)
		logging.info("SensorData object: " + str(dataObj))

	#@unittest.skip("Ignore for now.")
	def testReadSystemPerformanceDataFromGdaDataPath(self):
		logging.info("\n\n----- [SystemPerformanceData JSON from file to object] -----")
		
		fileName = self.gdaDataPath + '/SystemPerformanceData.dat'
		fileRef  = Path(fileName)
		dataStr  = fileRef.read_text(encoding = 'utf-8')

		dataObj  = self.dataUtil.jsonToSystemPerformanceData(dataStr)

		logging.info("SystemPerformanceData JSON from GDA: " + dataStr)
		logging.info("SystemPerformanceData object: " + str(dataObj))

if __name__ == "__main__":
	unittest.main()
