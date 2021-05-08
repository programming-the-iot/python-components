#####
# 
# This class is part of the Programming the Internet of Things
# project, and is available via the MIT License, which can be
# found in the LICENSE file at the top level of this repository.
# 
# Copyright (c) 2020 by Andrew D. King
# 

class Singleton(type):
	"""
	Metaclass definition for sub-classes that must be Singleton instances.
	
	"""
	_instances = {}
	
	def __call__(c, *args, **kwargs):
		# check if the instance exists - if not, create it and add it to _instances
		if c not in c._instances:
			c._instances[c] = super(Singleton, c).__call__(*args, **kwargs)
			
		return c._instances[c]
	