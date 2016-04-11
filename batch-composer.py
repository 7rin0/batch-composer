#!/usr/bin/python

# Import python modules
import json
import subprocess
import time
from pprint import pprint

# Parse composer.json
with open('composer.json') as data_file:    
    data = json.load(data_file)

# For each dict type item require dependency allong their version
for dependency, version in data['require'].iteritems():
	requiredDependency = "composer require " + dependency + ":" + version
	print requiredDependency	
	subprocess.Popen(requiredDependency, stdout=subprocess.PIPE, shell=True)
	time.sleep(60)
