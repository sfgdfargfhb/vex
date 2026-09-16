"""This is the code from last year's project which works on a different robot, placed here for references"""

#region VEXcode Generated Robot Configuration
from vex import *
# import urandom
import math

# Brain should be defined by default
brain=Brain()

# Robot configuration code
controller_1 = Controller(PRIMARY)
finalintake16 = Motor(Ports.PORT16, GearSetting.RATIO_18_1, False)
motor_11 = Motor(Ports.PORT11, GearSetting.RATIO_18_1, False)
motor_12 = Motor(Ports.PORT12, GearSetting.RATIO_18_1, False)
motor_13 = Motor(Ports.PORT13, GearSetting.RATIO_18_1, False)
Mainintake_motor_a = Motor(Ports.PORT14, GearSetting.RATIO_18_1, False)
Mainintake_motor_b = Motor(Ports.PORT15, GearSetting.RATIO_18_1, False)
Mainintake = MotorGroup(Mainintake_motor_a, Mainintake_motor_b)
motor_group_17_motor_a = Motor(Ports.PORT17, GearSetting.RATIO_18_1, True)
motor_group_17_motor_b = Motor(Ports.PORT18, GearSetting.RATIO_18_1, False)
motor_group_17 = MotorGroup(motor_group_17_motor_a, motor_group_17_motor_b)


# wait for rotation sensor to fully initialize
wait(30, MSEC)


# Make random actually random
def initializeRandomSeed():
    wait(100, MSEC)
    random = brain.battery.voltage(MV) + brain.battery.current(CurrentUnits.AMP) * 100 + brain.timer.system_high_res()
    # urandom.seed(int(random))

# Set random seed 
initializeRandomSeed()


def play_vexcode_sound(sound_name):
    # Helper to make playing sounds from the V5 in VEXcode easier and
    # keeps the code cleaner by making it clear what is happening.
    print("VEXPlaySound:" + sound_name)
    wait(5, MSEC)

# add a small delay to make sure we don't print in the middle of the REPL header
wait(200, MSEC)
# clear the console to make sure we don't have the REPL in the console
print("\033[2J")

#endregion VEXcode Generated Robot Configuration


# ------------------------------------------
# Custom Robot Code
# ------------------------------------------

from vex import *

brain = Brain()
controller = Controller(PRIMARY)

# Drive motors
left_motor_a = Motor(Ports.PORT11, GearSetting.RATIO_18_1, False)
left_motor_b = Motor(Ports.PORT17, GearSetting.RATIO_18_1, False)
right_motor_a = Motor(Ports.PORT12, GearSetting.RATIO_18_1, True)
right_motor_b = Motor(Ports.PORT18, GearSetting.RATIO_18_1, True)

left_drive = MotorGroup(left_motor_a, left_motor_b)
right_drive = MotorGroup(right_motor_a, right_motor_b)

# Middle strafe wheel
middle_motor = Motor(Ports.PORT13, GearSetting.RATIO_18_1, False)

# Intake motors
main_intake_vertical = Motor(Ports.PORT14, GearSetting.RATIO_18_1, False)
main_intake_horizontal = Motor(Ports.PORT15, GearSetting.RATIO_18_1, True)
upper_intake = Motor(Ports.PORT16, GearSetting.RATIO_18_1, False)

# Constants
DRIFT_CORRECTION_FACTOR = 1.35
INTAKE_SPEED = 50
STRAFE_SPEED = 100


def clamp_motor_value(value):
    return max(min(value, 100), -100)


# -------------------------
# AUTONOMOUS ROUTINE
# -------------------------
def autonomous():
    brain.screen.clear_screen()
    brain.screen.print("Running autonomous")

    # --- DRIVE FORWARD 2 FEET ---
    # 2-inch radius → 4-inch diameter → 12.566-inch circumference
    # 24 inches / 12.566 ≈ 1.91 rotations
    wheel_rotations = 1.91

    left_drive.reset_position()
    right_drive.reset_position()

    left_drive.spin_for(DirectionType.FORWARD, wheel_rotations, RotationUnits.REV, 50, VelocityUnits.PERCENT)
    right_drive.spin_for(DirectionType.FORWARD, wheel_rotations, RotationUnits.REV, 50, VelocityUnits.PERCENT)

    # --- RUN INTAKE FOR 30 ROTATIONS ---
    main_intake_vertical.spin_for(DirectionType.FORWARD, 30, RotationUnits.REV, INTAKE_SPEED, VelocityUnits.PERCENT)
    main_intake_horizontal.spin_for(DirectionType.REVERSE, 30, RotationUnits.REV, INTAKE_SPEED, VelocityUnits.PERCENT)
    upper_intake.spin_for(DirectionType.REVERSE, 30, RotationUnits.REV, INTAKE_SPEED, VelocityUnits.PERCENT)

    brain.screen.clear_screen()
    brain.screen.print("Auton complete")


# -------------------------
# DRIVER CONTROL
# -------------------------
def user_control():
    brain.screen.clear_screen()
    brain.screen.print("driver control")

    while True:
        forward = controller.axis3.position()
        turn = controller.axis1.position()

        left_speed = (forward + turn) * DRIFT_CORRECTION_FACTOR
        right_speed = (forward - turn)

        left_drive.spin(DirectionType.FORWARD, clamp_motor_value(left_speed), VelocityUnits.PERCENT)
        right_drive.spin(DirectionType.FORWARD, clamp_motor_value(right_speed), VelocityUnits.PERCENT)

        # Strafing
        if controller.buttonL1.pressing():
            middle_motor.spin(DirectionType.FORWARD, STRAFE_SPEED, VelocityUnits.PERCENT)
        elif controller.buttonR1.pressing():
            middle_motor.spin(DirectionType.REVERSE, STRAFE_SPEED, VelocityUnits.PERCENT)
        else:
            middle_motor.stop()

        # Intake
        if controller.buttonL2.pressing():
            main_intake_vertical.spin(DirectionType.REVERSE, INTAKE_SPEED, VelocityUnits.PERCENT)
            main_intake_horizontal.spin(DirectionType.FORWARD, INTAKE_SPEED, VelocityUnits.PERCENT)
            upper_intake.spin(DirectionType.FORWARD, INTAKE_SPEED, VelocityUnits.PERCENT)
        elif controller.buttonR2.pressing():
            main_intake_vertical.spin(DirectionType.FORWARD, INTAKE_SPEED, VelocityUnits.PERCENT)
            main_intake_horizontal.spin(DirectionType.REVERSE, INTAKE_SPEED, VelocityUnits.PERCENT)
            upper_intake.spin(DirectionType.REVERSE, INTAKE_SPEED, VelocityUnits.PERCENT)
        elif controller.buttonUp.pressing():
            main_intake_vertical.spin(DirectionType.FORWARD, INTAKE_SPEED, VelocityUnits.PERCENT)
            main_intake_horizontal.spin(DirectionType.REVERSE, INTAKE_SPEED, VelocityUnits.PERCENT)
        elif controller.buttonDown.pressing():
            main_intake_vertical.spin(DirectionType.REVERSE, INTAKE_SPEED, VelocityUnits.PERCENT)
            main_intake_horizontal.spin(DirectionType.FORWARD, INTAKE_SPEED, VelocityUnits.PERCENT)
        else:
            main_intake_vertical.stop()
            main_intake_horizontal.stop()
            upper_intake.stop()

        wait(20, MSEC)


# Competition setup
comp = Competition(user_control, autonomous)

brain.screen.clear_screen()