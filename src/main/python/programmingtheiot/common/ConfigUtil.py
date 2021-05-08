#####
# 
# This class is part of the Programming the Internet of Things
# project, and is available via the MIT License, which can be
# found in the LICENSE file at the top level of this repository.
# 
# Copyright (c) 2020 by Andrew D. King
# 

import configparser
import logging
import os
import traceback

from pathlib import Path

from programmingtheiot.common.Singleton import Singleton

import programmingtheiot.common.ConfigConst as ConfigConst

class ConfigUtil(metaclass = Singleton):
	"""
	A simple utility wrapper around the built-in Python
	configuration infrastructure.
	
	Implemented as a Singleton using the Singleton metaclass.
	
	"""

	configFile   = ConfigConst.DEFAULT_CONFIG_FILE_NAME
	configParser = configparser.ConfigParser()
	isLoaded	 = False
	
	def __init__(self, configFile: str = None):
		"""
		Constructor for ConfigUtil.
		
		@param configFile The name of the configuration file to load.
		"""
		if (configFile != None):
			self.configFile = configFile
			
		self._loadConfig()
		logging.info("Created instance of ConfigUtil: " + str(self))
	
	#
	# public methods
	#
	def getConfigFileName(self) -> str:
		"""
		Returns the name of the configuration file.
		
		@return The name of the config file.
		"""
		return self.configFile

	def getCredentials(self, section: str) -> dict:
		"""
		Attempts to load a separate configuration 'credential' file comprised
		of simple key = value pairs. The assumption with this call is that
		the credential file key is the same across all sections, so the
		only parameter requires is the section.
		
		If the credential file key has an entry (e.g. the file where the
		credentials are stored in key = value form), the file will be
		loaded if possible, and a dict object will be returned
		to the caller. No caching of the data is made, except within the
		returned dict object.
		
		NOTE: The key case IS preserved.
		
		@param section
		@return dict The dictionary of properties, or None if non-existent.
		"""
		if (self.hasSection(section)):
			credFileName = self.getProperty(section, ConfigConst.CRED_FILE_KEY);
			
			try:
				if os.path.exists(credFileName) and os.path.isfile(credFileName):
					logging.info("Loading credentials from section " + section + " and file " + credFileName)
					
					# read cred data and dump it into a custom section for parsing
					fileRef  = Path(credFileName)
					credData = "[" + ConfigConst.CRED_SECTION + "]\n" + fileRef.read_text()
					
					# create unique ConfigParser that preserves key case
					credParser = configparser.ConfigParser()
					credParser.optionxform = str
					
					# read the stringified file data and generate / return
					# a dict for the section we just created
					credParser.read_string(credData)
					credProps = dict(credParser.items(ConfigConst.CRED_SECTION))
					
					return credProps
				else:
					logging.warn("Credential file doesn't exist: " + credFileName)
			except Exception as e:
				traceback.print_exc()
				logging.warn("Failed to load credentials from file: " + credFileName + ". Exception: " + str(e))
		
		return None
	
	def getProperty(self, section: str, key: str, defaultVal: str = None, forceReload: bool = False):
		"""
		Attempts to retrieve the value of 'key' from the config.
		
		@param section The name of the section to parse.
		@param key The name of the key to lookup in 'section'.
		@param forceReload Defaults to false; if true will reload the config.
		@return The property associated with 'key' in 'section'.
		"""
		return self._getConfig(forceReload).get(section, key, fallback = defaultVal)
	
	def getBoolean(self, section: str, key: str, forceReload: bool = False):
		"""
		Attempts to retrieve the boolean value of 'key' from the config.
		If not found, or not True, False will be returned.
		
		@param section The name of the section to parse.
		@param key The name of the key to lookup in 'section'.
		@param forceReload Defaults to false; if true will reload the config.
		@return The boolean associated with 'key' in 'section', or false.
		"""
		return self._getConfig(forceReload).getboolean(section, key, fallback = False)
		
	def getInteger(self, section: str, key: str, defaultVal: int = 0, forceReload: bool = False):
		"""
		Attempts to retrieve the integer value of 'key' from the config.
		
		@param section The name of the section to parse.
		@param key The name of the key to lookup in 'section'.
		@param defaultVal The default value if section, key, or value doesn't exist (or is invalid).
		@param forceReload Defaults to false; if true will reload the config.
		@return The property associated with 'key' in 'section'.
		"""
		return self._getConfig(forceReload).getint(section, key, fallback = defaultVal)
	
	def getFloat(self, section: str, key: str, defaultVal: float = 0.0, forceReload: bool = False):
		"""
		Attempts to retrieve the float value of 'key' from the config.
		
		@param section The name of the section to parse.
		@param key The name of the key to lookup in 'section'.
		@param defaultVal The default value if section, key, or value doesn't exist (or is invalid).
		@param forceReload Defaults to false; if true will reload the config.
		@return The property associated with 'key' in 'section'.
		"""
		return self._getConfig(forceReload).getfloat(section, key, fallback = defaultVal)
	
	def hasProperty(self, section: str, key: str) -> bool:
		"""
		Checks if a given 'key' exists in the named section of the loaded config.
		
		@param section The name of the section to search.
		@param key The name of the key to lookup in 'section'.
		@return True if 'key' is found in 'section'; False otherwise.
		"""
		return self._getConfig().has_option(section, key)
		
	def hasSection(self, section: str) -> bool:
		"""
		Checks if a given 'section' exists in the loaded config.
		
		@param section The name of the section to search.
		@return True if 'section' exists and has parameters; false otherwise.
		"""
		return self._getConfig().has_section(section)
		
	def isConfigDataLoaded(self) -> bool:
		"""
		Simple boolean check if the config data is loaded or not.
		
		@return boolean True on success; False otherwise.
		"""
		return self.isLoaded
	
	#
	# private methods
	#
	
	def _loadConfig(self):
		"""
		Attempts to load the config file using the name passed into
		the constructor.
		 
		"""
		if (os.path.exists(self.configFile)):
			logging.info("Loading config: %s", self.configFile)
			
			self.configParser.read(self.configFile)
			self.isLoaded = True
		else:
			logging.info("Can't load %s. Trying default: %s", self.configFile, ConfigConst.DEFAULT_CONFIG_FILE_NAME)
			
			self.configFile = ConfigConst.DEFAULT_CONFIG_FILE_NAME
			self.configParser.read(self.configFile)
			self.isLoaded = True
		
		logging.debug("Config: %s", str(self.configParser.sections()))

	def _getConfig(self, forceReload: bool = False) -> configparser:
		"""
		Returns the entire configuration object. If the config file hasn't
		yet been loaded, it will be loaded.
		
		@param forceReload Defaults to false; if true, will reload the config.
		@return The entire configuration file.
		"""
		if (self.isLoaded == False or forceReload):
			self._loadConfig()
		
		return self.configParser
	