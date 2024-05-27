Code developed by Nathan Van Damme, ID:210820414

to run the package:
1) unzip the ar_week10_test in your catkin workspace;
2) run in terminal:
	$ roscore
3) in a new terminal, setup rViz:
	$roslaunch panda_moveit_config demo.launch
4) in a new terminal, navigate to the catkin_ws folder and build the catkin environment using: 
	$ catkin_make
5) run in terminal:
	$ roslaunch ar_week10_test ar_week10_test.launch

Alternatively, you can run the scripts and rqt_plot manually in separate terminals. You might have to source the catkin_ws folder when doing this:
	$ source ./devel/setup.bash

In case of permission errors, navigate to the ar_week10_test folder in the terminal and make the nodes executable using:
	$ chmod +x scripts/<script_name>.py
