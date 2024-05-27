Code developed by Nathan Van Damme, ID:210820414

to run the package:
1) unzip the ar_week5_test in your catkin workspace;
2) run in terminal:
	$ roscore
3) navigate to the ar_week5_test folder in the terminal and make the nodes executable using:
	$ chmod +x scripts/<script_name>.py
   check the scripts folder for the names of all the scripts;
4) in a new terminal, navigate to the catkin_ws folder and build the catkin environment using: 
	$ catkin_make
5) source the environment using:
	$ source ./devel/setup.bash
6) navigate to the catkin environment and run the launch file using:
	$ roslaunch ar_week5_test cubic_traj_gen.launch
7) in the rqt_plot GUI, add the topics 'position', 'velocity' and 'acceleration' to visualise them;

to visualise the graph, run in terminal:
	$ rosrun rqt_graph rqt_graph
