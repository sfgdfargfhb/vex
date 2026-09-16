# Library imports
from vex import *
import old
#devices set up
brain=Brain() # screen size: 480 x 240
controller=Controller()
# motor_1=Motor(Ports.PORT1)
# motor_2=Motor(Ports.PORT2)
# motors=MotorGroup(motor_1,motor_2)

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