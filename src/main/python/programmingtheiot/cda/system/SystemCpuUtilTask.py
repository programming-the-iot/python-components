#####
# 
# This class is part of the Programming the Internet of Things project.
# 
# It is provided as a simple shell to guide the student and assist with
# implementation for the Programming the Internet of Things exercises,
# and designed to be modified by the student as needed.
#

import logging
import psutil
from programmingtheiot.common import ConfigConst

from programmingtheiot.cda.system.BaseSystemUtilTask import BaseSystemUtilTask

class SystemCpuUtilTask(BaseSystemUtilTask):
	"""
	Shell representation of class for student implementation.
	
	"""

	def __init__(self):
		super(SystemCpuUtilTask, self).__init__(\
			name = ConfigConst.CPU_UTIL_NAME,\
			typeID = ConfigConst.CPU_UTIL_TYPE)
	
	def getTelemetryValue(self) -> float:
		return psutil.cpu_percent()
		