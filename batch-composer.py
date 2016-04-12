#!/usr/bin/python

# Import python modules
import json
import time
import shutil
import subprocess
from pprint import pprint

# Get real composer.json
with open('composer.json') as data_file:    
    current_composer = json.load(data_file)

# This only makes sense if exist key require in dictionary
# meaning if our composer has packages to install else skip everything
if 'require' in current_composer:
	# Clone from real composer.json and save an other empty in required packages
	tmp_composer = current_composer
	del tmp_composer['require']
	with open('composer-tmp/composer-schema.json', 'w') as no_data_file:
		json.dump(tmp_composer, no_data_file)
	
	# Switch directories of both composers
	shutil.move('composer.json', 'composer-tmp/composer.json')
	shutil.move('composer-tmp/composer-schema.json', 'composer.json')
	
	# For each item dictionary require dependency by defined version
	#for dependency, version in data['require'].iteritems():
	#	requiredDependency = "composer require " + dependency + ":" + version
	#	print requiredDependency	
	#	subprocess.Popen(requiredDependency, stdout=subprocess.PIPE, shell=True)
	#	time.sleep(60)
	
# Regenerate composer-schema.json
open('composer-tmp/composer-schema.json', 'a').close()
