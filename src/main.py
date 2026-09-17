# Library imports
from vex import *

# ===================== Device setup ======================

brain=Brain()  # screen size: 480 x 240
controller=Controller()

# =================== Drivetrain motors ===================

# Left-side motors
motor_left_front=Motor(Ports.PORT1,GearSetting.RATIO_18_1,False)
motor_left_back=Motor(Ports.PORT2,GearSetting.RATIO_18_1,False)
motors_left=MotorGroup(motor_left_back,motor_left_front)

# Right-side motors
# Reversed because they are mirror-mounted relative to the left-side motors.
motor_right_front=Motor(Ports.PORT3,GearSetting.RATIO_18_1,True)
motor_right_back=Motor(Ports.PORT4,GearSetting.RATIO_18_1,True)
motors_right=MotorGroup(motor_right_back,motor_right_front)

# Middle motor for sideways movement
motor_middle=Motor(Ports.PORT5,GearSetting.RATIO_18_1,False)

# ==================== Autonomous code ====================

def autonomous():
    brain.screen.clear_screen()
    brain.screen.print("autonomous code")
    while True:
        wait(20,MSEC)


# ================== Driver control code ==================

def user_control():
    brain.screen.clear_screen()
    brain.screen.print("driver control")
    while True:
        # Obtain the original joystick data
        forward_speed=controller.axis3.position()  # left joystick, vertical
        turn_speed=controller.axis1.position()     # right joystick, horizontal
        strafe_speed=controller.axis4.position()   # left joystick, horizontal

        # Calculate the speed of left and right motors
        left_speed=forward_speed+turn_speed
        right_speed=forward_speed-turn_speed

        # Constrain motor speeds to the range -100% to 100%
        left_speed=max(-100,min(100,left_speed))
        right_speed=max(-100,min(100,right_speed))
        strafe_speed=max(-100,min(100,strafe_speed))

        # Let the motors operate at the calculated speed
        motors_left.spin(FORWARD,left_speed,PERCENT)
        motors_right.spin(FORWARD,right_speed,PERCENT)
        motor_middle.spin(FORWARD,strafe_speed,PERCENT)

        # Keep the current motor commands for 20 ms before the next control update.
        wait(20,MSEC)


# ==================== Program startup ====================

# Use during a competition
# comp = Competition(user_control, autonomous)

# Use for autonomous testing 
# autonomous()

# Use for driver-control testing
user_control()