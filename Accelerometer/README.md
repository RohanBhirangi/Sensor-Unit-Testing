# Accelerometer

Setup Steps:
1: Upload the sevopy.ino to the Arduino board (using Arduino software).
2: Follow the build steps of Seattle and extract the Runnable folder (All files will be executed from this folder).
3: Copy ut_accelerometer.py (and other files) to the above mentioned folder.
4: Make sure the Sensibility Testbed app is running on your smartphone and execute ut_accelerometer.py from your machine.
Note: Some changes might be required in the ut_accelerometer.py file according to your local path, filenames etc.

Experiment 1: Place the smartphone flat on a table.
Observation: The value of the acceleration vector is around 9.8.

Experiment 2: Place the smartphone on the turntable rotating in clockwise direction.
Observation: The z-axis acceleration remains constant. The x-axis and y-axis acceleration change.

Experiment 3: Place the smartphone on the turntable rotating in anti-clockwise direction.
Observation: The z-axis acceleration remains constant. The x-axis and y-axis acceleration change.

Experiment 4: Place the smartphone on the turntable which switches between clockwise and anti-clockwise motion every 3 seconds.
Observation: The value of the acceleration vector is around 9.8

Contact: Rohan (rkb332@nyu.edu)
Note: Raw Data of the experiments can be found in the data folder.
