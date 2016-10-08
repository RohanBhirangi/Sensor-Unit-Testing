import sys
import seash_dictionary
import command_callbacks
import seash_helper

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

def execute_experiment(filename,environment_dict):
	input_dict=seash_dictionary.parse_command('start dylink.r2py encasementlib.r2py sensor_layer.r2py '+filename+'.r2py')
	command_callbacks.start_remotefn_arg(input_dict,environment_dict)

def show_log(environment_dict):
	input_dict=seash_dictionary.parse_command('show log')
	command_callbacks.show_log(input_dict,environment_dict)

def download_file(filename,environment_dict):
	input_dict=seash_dictionary.parse_command('download '+filename+'.txt')
	command_callbacks.download_filename(input_dict,environment_dict)

def open_file(filename,environment_dict):
	file = open(filename+'.txt', 'r')
	x_value=0.0
	y_value=0.0
	z_value=0.0
	for line in file:
	    values= line.split()
	    x_value=values[0]
	    y_value=values[1]
	    z_value=values[2]
	print (x_value)
	print (y_value)
	print (z_value)

if __name__ == '__main__':
	filename='accelerometer'
	keyname='rohan'
	environment_dict=initialize()
	update_time()
	loadkeys_browse(keyname,environment_dict)
	if len(sys.argv)>1:
		upload_sensorlib(environment_dict)
	upload_experiment(filename,environment_dict)
	execute_experiment(filename,environment_dict)
	download_file(filename,environment_dict)
	open_file(filename,environment_dict)