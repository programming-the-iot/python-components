#####
# 
# This class is part of the Programming the Internet of Things
# project, and is available via the MIT License, which can be
# found in the LICENSE file at the top level of this repository.
# 
# Copyright (c) 2020 by Andrew D. King
# 

import logging
import random
import unittest

from apscheduler.schedulers.background import BackgroundScheduler

from time import sleep

import programmingtheiot.common.ConfigConst as ConfigConst

from programmingtheiot.common.ConfigUtil import ConfigUtil
from programmingtheiot.common.DefaultDataMessageListener import DefaultDataMessageListener
from programmingtheiot.common.ResourceNameEnum import ResourceNameEnum

from programmingtheiot.cda.connection.CoapClientConnector import CoapClientConnector
from programmingtheiot.cda.connection.CoapServerAdapter import CoapServerAdapter

from programmingtheiot.cda.connection.handlers.GetSystemPerformanceResourceHandler import GetSystemPerformanceResourceHandler
from programmingtheiot.cda.connection.handlers.GetTelemetryResourceHandler import GetTelemetryResourceHandler

from programmingtheiot.data.SystemPerformanceData import SystemPerformanceData
from programmingtheiot.data.SensorData import SensorData

class CoapServerAdapterTest(unittest.TestCase):
	"""
	This test case class contains very basic integration tests for
	CoapServerAdapter and CoapClientConnector using your Python
	CoapServerAdapter instance.
	
	It should not be considered complete,
	but serve as a starting point for the student implementing
	additional functionality within their Programming the IoT
	environment.
	
	NOTE: This is different from CoapClientConnectorTest in that it uses
	an internal CoAP server; however, your PiotConfig.props for your CoAP
	client must point to the localhost for this to work, and you should
	NOT run another CoAP server (e.g., the GDA's CoAP server at the
	same time).
	"""
	
	@classmethod
	def setUpClass(self):
		logging.basicConfig(format = '%(asctime)s:%(module)s:%(levelname)s:%(message)s', level = logging.INFO)
		logging.info("Testing CoapServerAdapter and CoapClientConnector classes...")
		
		self.dataMsgListener = DefaultDataMessageListener()
		
		self.pollRate = ConfigUtil().getInteger(ConfigConst.CONSTRAINED_DEVICE, ConfigConst.POLL_CYCLES_KEY, ConfigConst.DEFAULT_POLL_CYCLES)
		
		self.coapClient = CoapClientConnector()
		self.coapServer = CoapServerAdapter(dataMsgListener = self.dataMsgListener)
		
		self.tempDataUpdateListener = GetTelemetryResourceHandler()
		self.sysPerfDataUpdateListener = GetSystemPerformanceResourceHandler()
		
		# add these CoAP resource handlers as listeners to the IDataMessageListener impl
		self.dataMsgListener.setTelemetryDataListener(ConfigConst.TEMP_SENSOR_NAME, self.tempDataUpdateListener)
		self.dataMsgListener.setSystemPerformanceDataListener(self.sysPerfDataUpdateListener)
		
		# add these CoAP resource handlers to the CoAP server
		self.coapServer.addResource( \
			ResourceNameEnum.CDA_SENSOR_MSG_RESOURCE, \
			ConfigConst.TEMP_SENSOR_NAME, \
			self.tempDataUpdateListener)
		
		self.coapServer.addResource( \
			ResourceNameEnum.CDA_SYSTEM_PERF_MSG_RESOURCE, \
			ConfigConst.SYSTEM_PERF_NAME, \
			self.sysPerfDataUpdateListener)
		
		# create a scheduler to update system perf data and temp sensor data at pollCycles
		self.scheduler = BackgroundScheduler()
		self.scheduler.add_job(self._updateTelemetry, 'interval', seconds = self.pollRate)
		
		# start the server and the scheduled data updater
		self.coapServer.startServer()
		self.scheduler.start()
		
	@classmethod
	def tearDownClass(self):
		self.scheduler.shutdown()
		self.coapServer.stopServer()
	
	def setUp(self):
		pass

	def tearDown(self):
		pass

	#@unittest.skip("Ignore for now.")
	def testConnectAndDiscover(self):
		"""
		Comment the annotation to test Connect and Discover
		"""
		self.coapClient.sendDiscoveryRequest(timeout = 5)
		
		sleep(5)

	#@unittest.skip("Ignore for now.")
	def testConnectAndGetCon(self):
		"""
		Comment the annotation to test CON GET
		"""
		self.coapClient.sendGetRequest( \
			resource = ResourceNameEnum.CDA_SENSOR_MSG_RESOURCE, name = ConfigConst.TEMP_SENSOR_NAME, enableCON = True, timeout = 5)
		
		sleep(5)
		
		self.coapClient.sendGetRequest( \
			resource = ResourceNameEnum.CDA_SENSOR_MSG_RESOURCE, name = ConfigConst.TEMP_SENSOR_NAME, enableCON = True, timeout = 5)
		
		sleep(5)
		
		self.coapClient.sendGetRequest( \
			resource = ResourceNameEnum.CDA_SENSOR_MSG_RESOURCE, name = ConfigConst.TEMP_SENSOR_NAME, enableCON = True, timeout = 5)
		
	@unittest.skip("Ignore for now.")
	def testConnectAndGetNon(self):
		"""
		Comment the annotation to test NON GET
		"""
		self.coapClient.sendGetRequest( \
			resource = ResourceNameEnum.CDA_MGMT_STATUS_MSG_RESOURCE, enableCON = False, timeout = 5)

	@unittest.skip("Ignore for now.")
	def testConnectAndDeleteCon(self):
		"""
		Comment the annotation to test CON DELETE
		"""
		self.coapClient.sendDeleteRequest( \
			resource = ResourceNameEnum.CDA_MGMT_STATUS_MSG_RESOURCE, enableCON = True, timeout = 5)
	
	@unittest.skip("Ignore for now.")
	def testConnectAndDeleteNon(self):
		"""
		Comment the annotation to test NON DELETE
		"""
		self.coapClient.sendDeleteRequest( \
			resource = ResourceNameEnum.CDA_MGMT_STATUS_MSG_RESOURCE, enableCON = False, timeout = 5)

	@unittest.skip("Ignore for now.")
	def testObserveForTwoMinutes(self):
		"""
		Comment the annotation to test Observe
		"""
		self._startObserver()
		sleep(120)
		self._stopObserver()
	
	@unittest.skip("Ignore for now.")
	def testConnectAndPostCon(self):
		"""
		Comment the annotation to test CON POST
		"""
		msg = "This is a test."
		self.coapClient.sendPostRequest(resource = ResourceNameEnum.CDA_MGMT_STATUS_MSG_RESOURCE, payload = msg, enableCON = True, timeout = 5)

	@unittest.skip("Ignore for now.")
	def testConnectAndPostNon(self):
		"""
		Comment the annotation to test NON POST
		"""
		msg = "This is a test."
		self.coapClient.sendPostRequest(resource = ResourceNameEnum.CDA_MGMT_STATUS_MSG_RESOURCE, payload = msg, enableCON = False, timeout = 5)

	@unittest.skip("Ignore for now.")
	def testConnectAndPutCon(self):
		"""
		Comment the annotation to test CON PUT
		"""
		msg = "This is a test."
		self.coapClient.sendPutRequest(resource = ResourceNameEnum.CDA_MGMT_STATUS_MSG_RESOURCE, payload = msg, enableCON = True, timeout = 5)

	@unittest.skip("Ignore for now.")
	def testConnectAndPutNon(self):
		"""
		Comment the annotation to test NON PUT
		"""
		msg = "This is a test."
		self.coapClient.sendPutRequest(resource = ResourceNameEnum.CDA_MGMT_STATUS_MSG_RESOURCE, payload = msg, enableCON = False, timeout = 5)
	
	@classmethod
	def _updateTelemetry(self):
		sysPerfVal = random.uniform(1.0, 50.0)
		tempVal = random.uniform(18.0, 22.0)
		
		sysPerfData = SystemPerformanceData()
		sysPerfData.setName("SystemPerfMsg")
		sysPerfData.setCpuUtilization(sysPerfVal)
		sysPerfData.setDiskUtilization(sysPerfVal)
		sysPerfData.setMemoryUtilization(sysPerfData)
		
		# Uncomment the next SLOC to trigger data message listener callback for perf data
		#self.dataMsgListener.handleSystemPerformanceMessage(sysPerfData)
	
		sensorData = SensorData()
		sensorData.setName(ConfigConst.TEMP_SENSOR_NAME)
		sensorData.setValue(tempVal)
		
		self.dataMsgListener.handleSensorMessage(sensorData)
		
	def _startObserver(self):
		self.coapClient.startObserver(resource = ResourceNameEnum.CDA_SENSOR_MSG_RESOURCE, name = ConfigConst.TEMP_SENSOR_NAME)
		self.coapClient.startObserver(resource = ResourceNameEnum.CDA_SYSTEM_PERF_MSG_RESOURCE, name = ConfigConst.SYSTEM_PERF_NAME)

	def _stopObserver(self):
		self.coapClient.stopObserver(resource = ResourceNameEnum.CDA_SENSOR_MSG_RESOURCE, name = ConfigConst.TEMP_SENSOR_NAME)
		self.coapClient.stopObserver(resource = ResourceNameEnum.CDA_SYSTEM_PERF_MSG_RESOURCE, name = ConfigConst.SYSTEM_PERF_NAME)

if __name__ == "__main__":
	unittest.main()
	