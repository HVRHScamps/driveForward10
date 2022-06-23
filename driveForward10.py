import libhousy
#You can define helper functions here, make sure to but them *above* the main function
first = True
def main(robot: libhousy.robot):
    global first
    if first:
        robot.lDriveEncoder.Reset()
        robot.rDriveEncoder.Reset()
        first=False

    robot.rDrive.Set(0.8)
    robot.lDrive.Set(0.8)

    if robot.rDriveEncoder.Get() > 120:
        robot.rDrive.Set(0)

    if robot.lDriveEncoder.Get() > 120:
        robot.rDrive.Set(0)

    # This tells the robot we're done and it can move on
    return libhousy.DONE
