# inclue code to help us talk to the robot
import libhousy
from more_itertools import first
 

def main(robot: libhousy.robot):
    # Here is where your recurring code will go
    if robot.rDriveEncoder.Reset():
        robot.lDriveEncoder.Reset()
    

    if robot.rDriveEncoder.Get() >125:
        error = 0.0 - robot.rDriveEncoder.Get()
        speed = error * -0.25
        robot.rDrive.Set(-0.25)
    elif robot.rDriveEncoder.Get() <115:
        error = 0.0 - robot.rDriveEncoder.Get()
        speed = error * 0.25
        robot.rDrive.Set(0.25)

    else: 
        robot.rDrive.Set(0)

    if robot.lDriveEncoder.Get() >125:
        error = 0.0 - robot.lDriveEncoder.Get()
        speed = error * -0.25
        robot.lDrive.Set(-0.25)
    elif robot.lDriveEncoder.Get() <115:
        error = 0.0 - robot.lDriveEncoder.Get()
        speed = error * 0.25
        robot.lDrive.Set(0.25)
    else:
        robot.lDrive.Set(0)
    #return libhousy.DONE


    
    # After everything is done, we tell the main program to stop us
    