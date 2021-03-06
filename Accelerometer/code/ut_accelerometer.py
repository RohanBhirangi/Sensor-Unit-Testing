"""
This python script performs all necessary seash commands
required to run a repy script on the smartphone..

The main goal is to automate the entire seash process
(loadkeys, browse, add, upload, execute) using this
python script.
So that the user just has to run this single program
to test the sensor api calls.

If we are running Sensibility on a smartphone for the
frist time, we need to uplaod the sensor library.
To do this, just pass any random argument to this python
program and it uploads the entire sensor library.
"""

import sys
import seash_dictionary
import seash_global_variables
import command_callbacks
import seash_helper
import time
import math

#environment dictionary to hold the state of the process
def initialize():
	environment_dict = {
	    'host': None, 
	    'port': None, 
	    'expnum': None,
	    'filename': None,
	    'cmdargs': None,
	    'defaulttarget': None,
	    'defaultkeyname': None,
	    'currenttarget': None,
	    'currentkeyname': None,
	    'autosave': False,
	    'handleinfo': {},
	    'showparse': True,
	    }
	return environment_dict

#needed to access seash functionality
def update_time():
	seash_helper.update_time()

#perform loadkeys, browse, on %1
def loadkeys_browse(keyname,environment_dict):
	input_dict=seash_dictionary.parse_command('loadkeys '+keyname+'')
	command_callbacks.loadkeys_keyname(input_dict,environment_dict)
	input_dict=seash_dictionary.parse_command('as '+keyname+'')
	command_callbacks.as_keyname(input_dict, environment_dict)
	input_dict=seash_dictionary.parse_command('browse')
	command_callbacks.browse(input_dict,environment_dict)
	input_dict=seash_dictionary.parse_command('on %1')
	command_callbacks.on_target(input_dict,environment_dict)

#uploads the sensor library. better way would be to use 'uploaddir sensorlib' but
#I can't access the uploaddir module as of now
def upload_sensorlib(environment_dict):
	print ('Uploading sensorlib')
	input_dict=seash_dictionary.parse_command('upload ~/Downloads/sensibility-testbed-demokit/sensorlib/dylink.r2py')
	command_callbacks.upload_filename(input_dict, environment_dict)
	input_dict=seash_dictionary.parse_command('upload ~/Downloads/sensibility-testbed-demokit/sensorlib/encasementlib.r2py')
	command_callbacks.upload_filename(input_dict, environment_dict)
	input_dict=seash_dictionary.parse_command('upload ~/Downloads/sensibility-testbed-demokit/sensorlib/getsensor.r2py')
	command_callbacks.upload_filename(input_dict, environment_dict)
	input_dict=seash_dictionary.parse_command('upload ~/Downloads/sensibility-testbed-demokit/sensorlib/sensor_layer.r2py')
	command_callbacks.upload_filename(input_dict, environment_dict)
	input_dict=seash_dictionary.parse_command('upload ~/Downloads/sensibility-testbed-demokit/sensorlib/sensorlib.r2py')
	command_callbacks.upload_filename(input_dict, environment_dict)
	input_dict=seash_dictionary.parse_command('upload ~/Downloads/sensibility-testbed-demokit/sensorlib/unicode_scrubber.r2py')
	command_callbacks.upload_filename(input_dict, environment_dict)
	input_dict=seash_dictionary.parse_command('upload ~/Downloads/sensibility-testbed-demokit/sensorlib/wrapper.r2py')
	command_callbacks.upload_filename(input_dict, environment_dict)

#upload the repy file on to the smartphone
def upload_experiment(filename,environment_dict):
	input_dict=seash_dictionary.parse_command('upload '+filename+'.r2py')
	command_callbacks.upload_filename(input_dict, environment_dict)

#show all the files on the target machine
def show_files_ontarget(filename,environment_dict):
	input_dict=seash_dictionary.parse_command('show files')
	command_callbacks.show_files(input_dict,environment_dict)

#get the IP of the target
def show_ip_ontarget():
	for longname in seash_global_variables.targets[environment_dict['currenttarget']]:
		thisnodeIP = seash_global_variables.vesselinfo[longname]['IP']
	return thisnodeIP

#execute the repy file on the smartphone. better way would be to use 'execute file.r2py' but
#I can't access the execute module as of now
def execute_experiment(filename,environment_dict):
	input_dict=seash_dictionary.parse_command('start dylink.r2py encasementlib.r2py sensor_layer.r2py '+filename+'.r2py')
	command_callbacks.start_remotefn_arg(input_dict,environment_dict)

#show the seash log
def show_log(environment_dict):
	input_dict=seash_dictionary.parse_command('show log')
	command_callbacks.show_log(input_dict,environment_dict)

#download a file from the smartphone the the laptop
#the file gets stored as [filename].txt.[destIP]_1224_v1
def download_file(filename,environment_dict):
	input_dict=seash_dictionary.parse_command('download '+filename+'.txt')
	command_callbacks.download_filename(input_dict,environment_dict)

#read the file from the laptop to access sensor values from it
def open_file(filename,ip,environment_dict):
	file = open(filename+'.txt.'+ip+'_1224_v1', 'r')
	average=0
	i=0
	for line in file:
		i=i+1
		sline=line.split()
		x2=math.pow(float(sline[0]),2)
		y2=math.pow(float(sline[1]),2)
		z2=math.pow(float(sline[2]),2)
		vector_length=math.sqrt(x2+y2+z2)
		average=average+vector_length
	average = average/i
	if (average>=9.5) and (average<=10.1):
		print 'OKAY! The acceleration values are as expected'
	else:
		print 'BAD! The acceleration values are not as expected'

if __name__ == '__main__':
	filename='accelerometer'
	keyname='rohan'
	environment_dict=initialize()
	update_time()
	loadkeys_browse(keyname,environment_dict)
	ip=show_ip_ontarget()
	#if we are running this test on a smartphone for the first time,
	#we need to upload the sensorlib. For this pass any random argument while
	#running this script for eg. python ut_accelerometer.py 1
	if len(sys.argv)>1:
		upload_sensorlib(environment_dict)
	upload_experiment(filename,environment_dict)
	execute_experiment(filename,environment_dict)
	time.sleep(20)
	download_file(filename,environment_dict)
	open_file(filename,ip,environment_dict)













