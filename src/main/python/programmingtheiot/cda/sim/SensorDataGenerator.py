#####
# 
# This class is part of the Programming the Internet of Things
# project, and is available via the MIT License, which can be
# found in the LICENSE file at the top level of this repository.
# 
# Copyright (c) 2020 by Andrew D. King
# 

import logging
import math
import numpy as calcLib
import matplotlib.pyplot as plotLib

class SensorDataGenerator(object):
	"""
	This is a simple sine wave generator utility class that supports
	approximate emulation of temperature, pressure, and humidity values
	that one might expect from an environmental sensor package.
	
	This is provided for simple testing purposes only.
	"""
	MIN_HOURS = 0
	MAX_HOURS = 24 * 7
	
	DEFAULT_MIN_VALUE = 0.0
	DEFAULT_MAX_VALUE = 100.0
	
	MIN_INDOOR_TEMP = 15.0
	LOW_NORMAL_INDOOR_TEMP = 18.0
	HI_NORMAL_INDOOR_TEMP = 22.0
	MAX_INDOOR_TEMP = 25.0
	
	MIN_ENV_TEMP = DEFAULT_MIN_VALUE
	MAX_ENV_TEMP = 40.0
	
	MIN_MONITOR_TEMP = -100.0
	MAX_MONITOR_TEMP = 100.0
	
	MIN_ENV_HUMIDITY = DEFAULT_MIN_VALUE
	LOW_NORMAL_ENV_HUMIDITY = 35.0
	HI_NORMAL_ENV_HUMIDITY = 45.0
	MAX_ENV_HUMIDITY = 100.0
	
	MIN_ENV_PRESSURE = 500.0
	LOW_NORMAL_ENV_PRESSURE = 990.0
	HI_NORMAL_ENV_PRESSURE = 1010.0
	MAX_ENV_PRESSURE = 1500.0
	
	MIN_MONITOR_PRESSURE = DEFAULT_MIN_VALUE
	MAX_MONITOR_PRESSURE = 50000.0
	
	DEFAULT_DATA_POINTS = 60 * MAX_HOURS
	
	NO_NOISE = 0
	MIN_NOISE = 1
	MAX_NOISE = 100
	DEFAULT_NOISE = 10
	
	FULL_WAVE = 0
	BELL_CURVE = 5
	INVERSE_CURVE = -5
	CURVE_UP = 10
	CURVE_DOWN = -10
	
	DEFAULT_TEMP_CURVE = FULL_WAVE
	DEFAULT_HUMIDITY_CURVE = BELL_CURVE
	DEFAULT_PRESSURE_CURVE = INVERSE_CURVE
	
	def __init__(self, epochOffsetSeconds: float = 0.0, useCurrentTime: bool = True, alignGeneratorToDay: bool = True):
		"""
		Constructor.
		
		@param epochOffsetSeconds The float representing the start time - in seconds - for this data set.
		Must be positive, and will represent the offset from this system's Epoch, unless overridden
		by the useCurrentTime flag (default).
		@param useCurrentTime If True (default), the current time (since Epoch) will be used as
		the starting time, regardless of the startTime parameter. If False, an attempt will be
		made to use startTime as the starting time
		@param alignGeneratorToDay Defaults to True. If enabled, the data
		generator logic will be aligned to create a single sine wave for
		a day - meaning the 24 hr start and end values will be approximately
		the same.
		"""
		self.epochOffsetSeconds = epochOffsetSeconds
		self.useCurrentTime = useCurrentTime
		self.alignGeneratorToDay = alignGeneratorToDay
		self.dayDenominator = (1 - (calcLib.pi / 10)) + calcLib.pi
		
	def generateDailyEnvironmentHumidityDataSet(self, noiseLevel: int = DEFAULT_NOISE, minValue: float = MIN_ENV_HUMIDITY, maxValue: float = MAX_ENV_HUMIDITY, useSeconds: bool = False):
		"""
		Generates a time-series data set for indoor temperature simulation over a 24-hour period.
		
		@param: noiseLevel Any positive integer between 0 (no noise) and 100 (max noise).
		Defaults to DEFAULT_NOISE (some noise).
		@param: minValue Defaults to MIN_ENV_HUMIDITY. Can be overridden and set between
		MIN_ENV_HUMIDITY and MAX_ENV_HUMIDITY. If equal to or greater than maxValue,
		will be set to maxValue - 1.
		@param: MAX_ENV_HUMIDITY Defaults to MAX_ENV_HUMIDITY. Can be overridden and set between
		MIN_ENV_HUMIDITY and MAX_ENV_HUMIDITY. If less than or equal to minValue,
		will be set to minValue + 1.
		@param: useSeconds Defaults to False. If True, the data set will be generated using
		second-level granularity; that is, one data pair for every second between
		startHour and endHour.
		@return SensorDataSet The sensor data set containing both time entries and data
		values for those time entries.
		"""
		if maxValue < self.MIN_ENV_HUMIDITY or maxValue > self.MAX_ENV_HUMIDITY: maxValue = self.MAX_ENV_HUMIDITY
		if minValue < self.MIN_ENV_HUMIDITY or minValue >= maxValue: minValue = maxValue - 1
		
		return self.generateDailySensorDataSet(curveType = self.DEFAULT_HUMIDITY_CURVE, noiseLevel = noiseLevel, minValue = minValue, maxValue = maxValue, startHour = 0, endHour = 24, useSeconds = useSeconds)
		
	def generateDailyEnvironmentPressureDataSet(self, noiseLevel: int = DEFAULT_NOISE, minValue: float = MIN_ENV_PRESSURE, maxValue: float = MAX_ENV_PRESSURE, useSeconds: bool = False):
		"""
		Generates a time-series data set for indoor temperature simulation over a 24-hour period.
		
		@param: noiseLevel Any positive integer between 0 (no noise) and 100 (max noise).
		Defaults to DEFAULT_NOISE (some noise).
		@param: minValue Defaults to MIN_ENV_PRESSURE. Can be overridden and set between
		MIN_ENV_PRESSURE and MAX_ENV_PRESSURE. If equal to or greater than maxValue,
		will be set to maxValue - 1.
		@param: maxValue Defaults to MAX_ENV_PRESSURE. Can be overridden and set between
		MIN_ENV_PRESSURE and MAX_ENV_PRESSURE. If less than or equal to minValue,
		will be set to minValue + 1.
		@param: useSeconds Defaults to False. If True, the data set will be generated using
		second-level granularity; that is, one data pair for every second between
		startHour and endHour.
		@return SensorDataSet The sensor data set containing both time entries and data
		values for those time entries.
		"""
		if maxValue < self.MIN_ENV_PRESSURE or maxValue > self.MAX_ENV_PRESSURE: maxValue = self.MAX_ENV_PRESSURE
		if minValue < self.MIN_ENV_PRESSURE or minValue >= maxValue: minValue = maxValue - 1
		
		return self.generateDailySensorDataSet(curveType = self.DEFAULT_PRESSURE_CURVE, noiseLevel = noiseLevel, minValue = minValue, maxValue = maxValue, startHour = 0, endHour = 24, useSeconds = useSeconds)
		
	def generateDailyIndoorTemperatureDataSet(self, noiseLevel: int = DEFAULT_NOISE, minValue: float = MIN_INDOOR_TEMP, maxValue: float = MAX_INDOOR_TEMP, useSeconds: bool = False):
		"""
		Generates a time-series data set for indoor temperature simulation over a 24-hour period.
		
		@param: noiseLevel Any positive integer between 0 (no noise) and 100 (max noise).
		Defaults to DEFAULT_NOISE (some noise).
		@param: minValue Defaults to MIN_INDOOR_TEMP. Can be overridden and set between
		MIN_ENV_TEMP and MAX_ENV_TEMP. If equal to or greater than maxValue,
		will be set to maxValue - 1.
		@param: maxValue Defaults to MAX_INDOOR_TEMP. Can be overridden and set between
		MIN_ENV_TEMP and MAX_ENV_TEMP. If less than or equal to minValue,
		will be set to minValue + 1.
		@param: useSeconds Defaults to False. If True, the data set will be generated using
		second-level granularity; that is, one data pair for every second between
		startHour and endHour.
		@return SensorDataSet The sensor data set containing both time entries and data
		values for those time entries.
		"""
		if maxValue < self.MIN_ENV_TEMP or maxValue > self.MAX_ENV_TEMP: maxValue = self.MAX_ENV_TEMP
		if minValue < self.MIN_ENV_TEMP or minValue >= maxValue: minValue = maxValue - 1
		
		return self.generateDailySensorDataSet(curveType = self.DEFAULT_TEMP_CURVE, noiseLevel = noiseLevel, minValue = minValue, maxValue = maxValue, startHour = 0, endHour = 24, useSeconds = useSeconds)
		
	def generateDailyMonitorTemperatureDataSet(self, noiseLevel: int = DEFAULT_NOISE, minValue: float = MIN_MONITOR_TEMP, maxValue: float = MAX_MONITOR_TEMP, useSeconds: bool = False):
		"""
		Generates a time-series data set for indoor temperature simulation over a 24-hour period.
		
		@param: noiseLevel Any positive integer between 0 (no noise) and 100 (max noise).
		Defaults to DEFAULT_NOISE (some noise).
		@param: minValue Defaults to MIN_MONITOR_TEMP. Can be overridden and set between
		MIN_MONITOR_TEMP and MAX_MONITOR_TEMP. If equal to or greater than maxValue,
		will be set to maxValue - 1.
		@param: maxValue Defaults to MAX_MONITOR_TEMP. Can be overridden and set between
		MIN_MONITOR_TEMP and MAX_MONITOR_TEMP. If less than or equal to minValue,
		will be set to minValue + 1.
		@param: useSeconds Defaults to False. If True, the data set will be generated using
		second-level granularity; that is, one data pair for every second between
		startHour and endHour.
		@return SensorDataSet The sensor data set containing both time entries and data
		values for those time entries.
		"""
		if maxValue < self.MIN_MONITOR_TEMP or maxValue > self.MAX_MONITOR_TEMP: maxValue = self.MAX_MONITOR_TEMP
		if minValue < self.MIN_MONITOR_TEMP or minValue >= maxValue: minValue = maxValue - 1
		
		return self.generateDailySensorDataSet(curveType = self.DEFAULT_TEMP_CURVE, noiseLevel = noiseLevel, minValue = minValue, maxValue = maxValue, startHour = 0, endHour = 24, useSeconds = useSeconds)
		
	def generateDailySensorDataSet(self, curveType: int = FULL_WAVE, noiseLevel: int = DEFAULT_NOISE, minValue: float = DEFAULT_MIN_VALUE, maxValue: float = DEFAULT_MAX_VALUE, startHour: int = MIN_HOURS, endHour: int = MAX_HOURS, useSeconds = False):
		"""
		Generates a time-series data set. This call will use the parameters to generate
		time-series data that includes the ordered time points and their values stored
		within a SensorDataSet instance.
		
		The default behavior is to generate a data pair (time point and value) for every
		minute between startHour and stopHour. If startHour and stopHour are the same, a
		single data pair will be generated.
		
		@param curveType The type of curve to implement - FULL_WAVE, CURVE_UP, CURVE_DOWN,
		BELL_CURVE, INVERSE_CURVE. Defaults to FULL_WAVE.
		@param: noiseLevel Any positive integer between 0 (no noise) and 100 (max noise).
		Defaults to DEFAULT_NOISE (some noise).
		@param: minValue The minimum value, or floor, of the data. Defaults to DEFAULT_MIN_VALUE.
		If greater than maxValue, will be set to maxValue.
		@param: maxValue The maximum value, or ceiling, of the data. Defaults to DEFAULT_MAX_VALUE.
		If less than minValue, will be set to minValue.
		@param: startHour The beginning hour. Must be between MIN_HOURS and MAX_HOURS.
		If less than MIN_HOURS or greater than MAX_HOURS, will be set to MIN_HOURS.
		If greater than endHour, will be set to endHour.
		@param: endHour The ending hour. Must be between MIN_HOURS and MAX_HOURS.
		If less than MIN_HOURS or greater than MAX_HOURS, will be set to MAX_HOURS.
		If less than startHour, will be set to MAX_HOURS.
		@param: useSeconds Defaults to False. If True, the data set will be generated using
		second-level granularity; that is, one data pair for every second between
		startHour and endHour.
		@return SensorDataSet The sensor data set containing both time entries and data
		values for those time entries.
		"""
		# validate noise level - ensure it's between 1 and 100
		if noiseLevel < self.NO_NOISE: noiseLevel = self.NO_NOISE
		if noiseLevel > self.MAX_NOISE: noiseLevel = self.MAX_NOISE
		
		# validate min and max values
		if maxValue < minValue: maxValue = minValue
		if minValue > maxValue: minValue = maxValue
		
		# validate start and end hours
		if startHour < self.MIN_HOURS or minValue > self.MAX_HOURS: startHour = self.MIN_HOURS
		if endHour < 0 or endHour > self.MAX_HOURS: endHour = self.MAX_HOURS
		
		# calc total data points to be generated
		totalDataPoints = (endHour - startHour) * 60
		
		if useSeconds: totalDataPoints = totalDataPoints * 60
		if totalDataPoints == 0: totalDataPoints = 1
		
		# create evenly spaced number of 'totalDataPoints' between 'startHour' and 'endHour'
		timeEntries = calcLib.linspace(start = startHour, stop = endHour, num = totalDataPoints)
		
		# generate the distribution data for each point - quick ramp up curve
		# followed by a more gradual ramp down
		if self.alignGeneratorToDay:
			if curveType > 0:
				denominator = (curveType + self.dayDenominator)
			elif curveType == 0:
				denominator = self.dayDenominator
			else:
				denominator = abs(curveType) * self.dayDenominator
				
			dataValuesClean = calcLib.sin(timeEntries / denominator)
		else:
			if curveType > 0:
				denominator = curveType
			elif curveType == 0:
				denominator = 1
			else:
				denominator = 1 / abs(curveType)
				
			dataValuesClean = calcLib.sin(timeEntries / denominator)
		
		# re-scale array with 'minValue' as floor and 'maxValue' as ceiling
		scaledValuesClean = calcLib.interp(dataValuesClean, (dataValuesClean.min(), dataValuesClean.max()), (minValue, maxValue))
		dataSet = SensorDataSet(epochOffsetSeconds = self.epochOffsetSeconds, useCurrentTime = self.useCurrentTime, timeEntries = timeEntries)
		
		# check if noise should be added
		if noiseLevel != self.NO_NOISE:
			# get the mean value, generate base10 log and calculate noise numerator
			meanValue = calcLib.mean(scaledValuesClean)
			
			# calc order of magnitude of mean value - this is necessary to ensure
			# the generated noisyness aligns with the magnitude of the values
			meanMag = int(math.log10(meanValue))
			noiseScale = ((noiseLevel / 100) * ((10 ** meanMag) / 10))
			noisyTemp = calcLib.random.normal(0, noiseScale, len(scaledValuesClean))
			
			logging.debug("Noise=%f; Noise Scale=%f; Mean Magnitude=%f" % (noiseLevel, noiseScale, meanMag))
			
			# update the data set to add in noise with clean values
			scaledValuesNoisy = (scaledValuesClean + noisyTemp)
			
			dataSet.setDataEntries(scaledValuesNoisy)
		else:
			dataSet.setDataEntries(scaledValuesClean)
		
		return dataSet
		
	def generateOnScreenGraph(self, dataSet = None, chartTitle: str = "Sample Data", chartXLabel: str = "X Axis", chartYLabel: str = "Y Axis"):
		"""
		A simple graph generator using the title info passed in
		and the sample data set, which must be of type SensorDataSet.
		
		This will generate a graph, so there must be a window manager
		running on the system for this to function correctly.
		
		@param dataSet The SensorDataSet instance.
		@param chartTitle The string representing the title of the chart. Should be no more than 100 characters.
		@param chartXLabel The string to use for the X Label.
		@param chartYLabel The string to use for the Y Label.
		"""
		self.plotter = plotLib
		
		self.plotter.plot(dataSet.getTimeEntries(), dataSet.getDataEntries())
		self.plotter.title(chartTitle)
		self.plotter.ylabel(chartYLabel)
		self.plotter.xlabel(chartXLabel)
		self.plotter.grid(True, which = 'both')
		self.plotter.show()
		

from time import time, ctime

class SensorDataSet():
	"""
	Class definition of the data structure that will hold the time entries and
	corresponding data entries for the generated data.
	
	NOTE: No check is made to determine if the resultant arrays from time entries
	and data entries are from the same data generation set or of equivalent length.
	It is expected that this class will be used to store numpy generated data
	using one of the functions embedded above.
	"""
	
	def __init__(self, epochOffsetSeconds: float = 0.0, timeEntries = None, dataEntries = None, useCurrentTime: bool = True):
		"""
		Constructor.
		
		@param epochOffsetSeconds The float representing the start time - in seconds - for this data set.
		Must be positive, and will represent the offset from this system's Epoch, unless overridden
		by the useCurrentTime flag (default).
		@param timeEntries The ndarray tuple representing time entries. It is expected this can
		be converted to a single dim array.
		@param dataEntries The ndarray tuple representing data entries. It is expected this can
		be converted to a single dim array.
		@param useCurrentTime If True (default), the current time (since Epoch) will be used as
		the starting time, regardless of the startTime parameter. If False, an attempt will be
		made to use startTime as the starting time
		"""
		self.currentTime = time()
		
		if not useCurrentTime:
			try:
				offsetSeconds = abs(float(epochOffsetSeconds))
				self.currentTime = offsetSeconds
			except:
				logging.warning("Offset seconds since epoch not a float. Using current time instead.")
		
		self.currentTimeStamp = ctime(self.currentTime)
		
		logging.info("Current time set to: " + self.currentTimeStamp)
			
		self.setTimeEntries(timeEntries)
		self.setDataEntries(dataEntries)
		
	def getCurrentTime(self) -> float:
		"""
		Returns the current time in seconds.
		
		@return float The current time in seconds based on the time offset
		value from this system's Epoch set during initialization.
		"""
		return self.currentTime
	
	def getCurrentTimeStamp(self) -> str:
		"""
		Returns the current time stamp as a well-formed time / date string.
		
		@return String The current time stamp based on the time offset value
		from this system's Epoch set during initialization.
		"""
		return self.currentTimeStamp
	
	def getTimeEntries(self):
		"""
		Returns the timeEntries offset tuple. This is an array that contains
		one index for each time offset from from the configured start time
		(e.g. hour '0') to the configured end time (e.g. hour '24') in the
		configured increments (e.g. minutes).
		"""
		return self.timeEntries
	
	def getTimeEntry(self, index: int = 0) -> float:
		"""
		Returns the float value at 'index' in the time entries array.
		If index is < 0 or > timeEntries.size - 1, 0 will be used.
		
		@return float
		"""
		if index < 0 or index > self.timeEntries.size - 1:
			index = 0
		
		return self.timeEntries[index]
	
	def getDataEntries(self):
		"""
		Returns the dataEntries structure.
		"""
		return self.dataEntries
	
	def getDataEntry(self, index = 0) -> float:
		"""
		Returns the float value at 'index' in the data entries array.
		If index is < 0 or > dataEntries.size - 1, 0 will be used.
		
		@return float
		"""
		if index < 0 or index > self.dataEntries.size - 1:
			index = 0
		
		return self.dataEntries[index]
	
	def getDataEntryCount(self) -> int:
		"""
		Returns the number of data entries in the data entry array.
		
		@return int
		"""
		return self.dataEntries.size
	
	def setTimeEntries(self, timeEntries):
		"""
		Setter for time entry values.
		
		@param: timeEntries The ndarray tuple (actually a single dim array) containing time entries
		(evenly spaced from start to end) that should correspond to dataEntries - element by element.
		"""
		if not timeEntries is None:
			# data generator uses a single dimension array, so it's safe to flatten
			self.timeEntries = timeEntries.flatten()
			logging.info("timeEntries tuple. Array Size: %s  ND Size: %s  Dimensions: %s  Shape: %s  Type: %s", self.timeEntries.size, timeEntries.size, timeEntries.ndim, timeEntries.shape, timeEntries.dtype)
		
	def setDataEntries(self, dataEntries):
		"""
		Setter for data entry values.
		
		@param: dataEntries The ndarray tuple (actually a single dim array) containing data values
		that should correspond to timeEntries - element by element.
		"""
		if not dataEntries is None:
			# data generator uses a single dimension array, so it's safe to flatten
			self.dataEntries = dataEntries.flatten()
			logging.info("dataEntries tuple. Array Size: %s  ND Size: %s  Dimensions: %s  Shape: %s  Type: %s", self.dataEntries.size, dataEntries.size, dataEntries.ndim, dataEntries.shape, dataEntries.dtype)
		
def main():
	"""
	Main function definition for running as an application.
	
	"""
	logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level = logging.INFO)
	
	sensorDataGeneratorEpoch = SensorDataGenerator(useCurrentTime = False, alignGeneratorToDay = True)
	
	# run generic example - 1 second samples over 24 hours - start time will be this system's Epoch
	sensorDataSet = sensorDataGeneratorEpoch.generateDailySensorDataSet(noiseLevel = 10, startHour = 0, endHour = 24, minValue = 10, maxValue = 20, useSeconds = True)
	sensorDataGeneratorEpoch.generateOnScreenGraph(dataSet = sensorDataSet)
	
	sensorDataGenerator = SensorDataGenerator(alignGeneratorToDay = True)
	
	# run indoor temp example - 1 minute samples over 24 hours - start time will be this system's current time
	sensorDataSet = sensorDataGenerator.generateDailyIndoorTemperatureDataSet(noiseLevel = 15, minValue = SensorDataGenerator.LOW_NORMAL_INDOOR_TEMP, maxValue = SensorDataGenerator.HI_NORMAL_INDOOR_TEMP)
	sensorDataGenerator.generateOnScreenGraph(chartTitle = "Indoor Temp", chartXLabel = "Hour", chartYLabel = "Temp (C)", dataSet = sensorDataSet)
	
	# run humidity example - 1 minute samples over 24 hours - start time will be this system's current time
	sensorDataSet = sensorDataGenerator.generateDailyEnvironmentHumidityDataSet(noiseLevel = 10, minValue = SensorDataGenerator.LOW_NORMAL_ENV_HUMIDITY, maxValue = SensorDataGenerator.HI_NORMAL_ENV_HUMIDITY)
	sensorDataGenerator.generateOnScreenGraph(chartTitle = "Humidity", chartXLabel = "Hour", chartYLabel = "Relative %", dataSet = sensorDataSet)
	
	# run pressure example - 1 minute samples over 24 hours - start time will be this system's current time
	sensorDataSet = sensorDataGenerator.generateDailyEnvironmentPressureDataSet(noiseLevel = 1, minValue = SensorDataGenerator.LOW_NORMAL_ENV_PRESSURE, maxValue = SensorDataGenerator.HI_NORMAL_ENV_PRESSURE)
	sensorDataGenerator.generateOnScreenGraph(chartTitle = "Pressure", chartXLabel = "Hour", chartYLabel = "Millibars", dataSet = sensorDataSet)
	
if __name__ == '__main__':
	"""
	Attribute definition for when invoking as app via command line
	
	"""
	main()
	