# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       jlyne                                                        #
# 	Created:      11/11/2024, 11:51:50 AM                                       #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *

# Brain should be defined by default
brain=Brain()

# Robot configuration code
# Add in your motors and drivetrain

# wait for rotation sensor to fully initialize
wait(30, MSEC)

# Configure variables and values before automonous starts.  
# Setting sensors values, heading base values, etc....
def config_starting_values():
    global myVariable
    pass

# custom automonous code called by the auton function
def onauton_autonomous():
    global myVariable
    pass

# custom driver code called by the drive control function
def ondriver_drivercontrol():
    global myVariable
    while True:
        wait(5, MSEC)

# create a function for handling the starting and stopping of all autonomous tasks
def vexcode_auton_function():
    # Start the autonomous control tasks
    auton_task = Thread( onauton_autonomous )
    # wait for the driver control period to end
    while( competition.is_autonomous() and competition.is_enabled() ):
        # wait 10 milliseconds before checking again
        wait( 10, MSEC )
    # Stop the autonomous control tasks
    auton_task.stop()

# Drive control function.
def vexcode_driver_function():
    # Start the driver control tasks
    driver_control_task = Thread( ondriver_drivercontrol )

    # wait for the driver control period to end
    while( competition.is_driver_control() and competition.is_enabled() ):
        # wait 10 milliseconds before checking again
        wait( 10, MSEC )
    # Stop the driver control tasks
    driver_control_task.stop()


# register the competition functions
# First parameter is the name of the drive control function
# Second paramete ris the name of the autonomous control function 
competition = Competition( vexcode_driver_function, vexcode_auton_function )


config_starting_values()


        
