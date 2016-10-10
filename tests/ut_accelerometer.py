import sys
import seash_dictionary
import seash_global_variables
import command_callbacks
import seash_helper
import time
import math

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

def update_time():
	seash_helper.update_time()

def loadkeys_browse(keyname,environment_dict):
	input_dict=seash_dictionary.parse_command('loadkeys '+keyname+'')
	command_callbacks.loadkeys_keyname(input_dict,environment_dict)
	input_dict=seash_dictionary.parse_command('as '+keyname+'')
	command_callbacks.as_keyname(input_dict, environment_dict)
	input_dict=seash_dictionary.parse_command('browse')
	command_callbacks.browse(input_dict,environment_dict)
	input_dict=seash_dictionary.parse_command('on %1')
	command_callbacks.on_target(input_dict,environment_dict)

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

def upload_experiment(filename,environment_dict):
	input_dict=seash_dictionary.parse_command('upload '+filename+'.r2py')
	command_callbacks.upload_filename(input_dict, environment_dict)

def show_files_ontarget(filename,environment_dict):
	input_dict=seash_dictionary.parse_command('show files')
	command_callbacks.show_files(input_dict,environment_dict)

def show_ip_ontarget():
	for longname in seash_global_variables.targets[environment_dict['currenttarget']]:
		thisnodeIP = seash_global_variables.vesselinfo[longname]['IP']
	return thisnodeIP

def execute_experiment(filename,environment_dict):
	input_dict=seash_dictionary.parse_command('start dylink.r2py encasementlib.r2py sensor_layer.r2py '+filename+'.r2py')
	command_callbacks.start_remotefn_arg(input_dict,environment_dict)

def show_log(environment_dict):
	input_dict=seash_dictionary.parse_command('show log')
	command_callbacks.show_log(input_dict,environment_dict)

def download_file(filename,environment_dict):
	input_dict=seash_dictionary.parse_command('download '+filename+'.txt')
	command_callbacks.download_filename(input_dict,environment_dict)

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
	if len(sys.argv)>1:
		upload_sensorlib(environment_dict)
	upload_experiment(filename,environment_dict)
	execute_experiment(filename,environment_dict)
	time.sleep(20)
	download_file(filename,environment_dict)
	open_file(filename,ip,environment_dict)













