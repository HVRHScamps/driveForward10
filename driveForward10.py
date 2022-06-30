# inclue code to help us talk to the robot
import libhousy

def main(robot: libhousy.robot):
    # Here is where your recurring code will go
    if robot.lDriveEncoder.Get() >125:
        robot.lDrive.Set(-0.3)
    
    elif robot.lDriveEncoder.Get() <115:
        robot.lDrive.Set(0.3)
        
    else: 
        robot.lDrive.Set(0)

    if robot.rDriveEncoder.Get() >125:
        robot.rDrive.Set(-0.3)

    elif robot.rDriveEncoder.Get() <115:
        robot.rDrive.Set(0.3)
    else:
        robot.rDrive.Set(0)
    #return libhousy.DONE


    
    # After everything is done, we tell the main program to stop us
    