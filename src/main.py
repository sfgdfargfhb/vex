# Library imports
from vex import *

# devices set up
brain=Brain() # screen size: 480 x 240
controller=Controller()
# drivetrain motors
motor_left_front=Motor(Ports.PORT1,GearSetting.RATIO_18_1,False)
motor_left_back=Motor(Ports.PORT2,GearSetting.RATIO_18_1,False)
motors_left=MotorGroup(motor_left_back,motor_left_front)
motor_right_front=Motor(Ports.PORT3,GearSetting.RATIO_18_1,True)
motor_right_back=Motor(Ports.PORT4,GearSetting.RATIO_18_1,True)
motors_right=MotorGroup(motor_right_back,motor_right_front)
motor_middle=Motor(Ports.PORT5,GearSetting.RATIO_18_1,False)

def autonomous():
    brain.screen.clear_screen()
    brain.screen.print("autonomous code")
    while True:
        wait(20,MSEC)

def user_control():
    brain.screen.clear_screen()
    brain.screen.print("driver control")
    while True:
        if controller.buttonL1.pressing():
            # motors.spin(FORWARD,100,PERCENT)
            pass
        elif controller.buttonR1.pressing():
            # motors.spin(REVERSE,100,PERCENT)
            pass
        else:
            # motors.stop()
            pass
        wait(20,MSEC)

# actions to do when the program starts
# comp = Competition(user_control, autonomous)
# autonomous()
user_control()